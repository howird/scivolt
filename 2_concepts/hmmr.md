---
tags:
  - paper
status: todo
year: 2019/09
authors: Angjoo Kanazawa, Jason Y. Zhang, Panna Felsen, Jitendra Malik
citekey: kanazawaLearning3DHuman2019
---
# HMMR: Learning 3D Human Dynamics from Video

![HMMR](2_concepts/media/Pasted%20image%2020250306103708.png)



## Objective: Robust Recovery of 3D Human Body Mesh over time from Video

- **Previous Work**:
    - **[HMR](2_concepts/hmr.md):** given a cropped RGB image of a human ($I$), predicts 3D mesh (SMPL) parameters ($\theta$, $\beta$), and camera parameters

- **Approach:**
    - **WANT:** $\text{HMMR}: V \rightarrow {\Theta}$
    - **IN:** Video sequence $V = \{I_t\}_{t=1}^{T}$ of length $T$
    - **OUT:** 3D human pose and shape at each frame $\Theta_t = \{ \beta, \theta, \Pi \}$
        - $\beta$: SMPL Shape parameters
        - $\theta$: SMPL Pose parameters (joint rotations)
        - $\Pi$: Weak-perspective camera parameters
            - Rotation: $R \in \mathbb{R}^{3 \times 3}$ (axis-angle)
            - Translation: $t \in \mathbb{R}^2$
            - Scale: $s \in \mathbb{R}$

- **Existing Dependencies:**
    - **[SMPL Model](2_concepts/smpl.md):** enables us to learn low dimensional, semantically significant, representations for Human Meshes ($\beta, \theta$) rather than learn the actual mesh
    - **(RGB Video, 2D pose, Per-Joint Visibility) datasets:**
        - Penn Action: 15 sports actions, with 1257 training videos and 1068 test. We set aside 10% of the test set as validation
        - NBA (self-collected): videos of basketball players attempting 3-point shots in 16 basketball games. Each sequence contains one set of 2D annotations for a single player
    - **(RGB Video, 3D pose, SMPL) dataset:** Human3.6M
    - **(RGB Video,)  unlabeled datasets:**
        - **VLOGpeople:**, a subset of the VLOG lifestyle dataset
        - **InstaVariety:** self-collected from Instagram using 84 hashtags such as instruction, swimming, and dancing
    - **OpenPose:** model that generates 2D pose pseudo-ground truth
        - For videos that contain multiple people, we form our pseudo-ground truth by linking the per-frame skeletons from OpenPose using the Hungarian algorithm-based tracker from Detect and Track
    - **3D mesh (SMPL) dataset:** CMU, Human3.6M (train set), PosePrior
    - **ImageNet trained ResNet:** Used to get image features

## Challenges

- **CHALLENGE 1**: How can we ensure that our model encodes the temporal information of human dynamics?
    - **WHY:**
        - (1) Having temporal context will reduce ambiguity in 3D pose, shape, and viewpoint, resulting in a temporally smooth 3D mesh reconstruction
        - (2) Temporal info could also be useful for downstream tasks that can take advantage of it
    - **Hypothesis:** 
        - (1) Instead of having a single frame, $I_t$, as our model input, we can also include the frames within $\pm \Delta t$
        - (2) We can train pose regressors, $f_{-\Delta t}$ and $f_{+\Delta t}$, which predict the pose at the 

    - **IN:** $\{\phi_i\}_{i = t-\Delta t}^{t+\Delta t}$ set of individual latent representations of centered symmetrically about a time step, $t$
    - **OUT:** $\Phi_t$, latent representation of a set frames centered about $t$, aka latent movie strip
    - **WANT:** $f_{\text{movie}}: \phi_t \rightarrow {\Phi_t}$

- **CHALLENGE 2**: Will [HMR](2_concepts/hmr.md) translate to our temporally-aware latent representations?
    - **Hypothesis:** (1)
    - **IN:** $\Phi_t$, latent representation of a set frames centered about $t$, aka latent movie strip
    - **OUT**: latent representation of the current frame containing some understanding of the frames before and after, $\Phi_t$
    - **WANT**: $f_{\text{3D}}: \Phi_t \rightarrow {\Theta_t}$
    - can we learn 3D human dynamics from video using a temporal encoding of image features

- CHALLENGE B: Train in a semi-supervised manner using both labeled and pseudo-labeled data

1. **Projection to 2D:**

- Given 3D joints $X \in \mathbb{R}^{k \times 3}$ (extracted from the mesh), 2D projections are:
$$
x = \Pi(X(\beta, \theta))
$$
- where $\Pi = [s, t_x, t_y]$ is the weak-perspective camera.

3. **Losses:**
- **Reprojection loss:** Minimize 2D joint error
$$
L_{2D} = ||v_t (x_t - \hat{x}_t)||^2
$$
- **3D pose loss:** When available
$$
L_{3D} = ||\Theta_t - \hat{\Theta}_t||^2
$$
- **Adversarial loss:** Ensures plausible human poses
$$
L_{adv} = \sum_k (D_k(\Theta) - 1)^2
$$
- **Shape consistency loss:** Enforces shape continuity
$$
L_{\text{shape}} = \sum_{t=1}^{T-1} ||\beta_t - \beta_{t+1}||
$$
- **Hallucination loss:** Predicts temporal representation from a single frame
$$
L_{\text{hall}} = ||\Phi_t - \tilde{\Phi}_t||^2
$$
- **Total loss:**
$$
L = L_{\text{temporal}} + L_{\text{hall}} + L_t(\tilde{\Phi}_t) + \sum_{\Delta t} L_{t+\Delta t}(\tilde{\Phi}_t)
$$

---

## Method

### Training Regressor + Hallucinator

#### 0. Preprocessing + Augmentations

- **IN**: RGB Image $I \in \mathbb{R}^{H \times W \times 3}$

- Resizing: All images are scaled to 224 × 224 preserving the aspect ratio s.t. the diagonal of the tight bounding box is roughly 150px
- Augmentations: Randomly scaled, translated, and flipped
- Mini-batch size is 64
    - when paired 3D supervision is employed each mini-batch is balanced such that it consists of half 2D and half 3D samples

- **OUT**: RGB Image $I \in \mathbb{R}^{224 \times 224 \times 3}$

#### 1. Image Encoding

- **IN:** Image sequence $V = \{I_t\}^T$
    - where: $I_t \in \mathbb{R}^{224 \times 224 \times 3}$ is an RGB image

- ResNet-50 (pre-trained on ImageNet), average pooled, flattened
- Each frame ($I_t$) is passed into the ResNet individually

- **OUT**: Feature vector $\{\phi_t\}^T \in \mathbb{R}^{T\times2048}$
    - where: $\phi_t \in \mathbb{R}^{2048}$

- note: this is done ahead of time since video takes a lot of compute

#### 2. 3D Pose & Shape Estimation

- **IN:** Temporal representation $\Phi_t$

- $f_{\text{3D}}: \Phi_t \rightarrow \Theta_t$ (see methodology introduced in [hmr](2_concepts/hmr.md), this function signature omits iterative feedback details)

- **OUT:** 3D human mesh and future motion $\Theta_t$

#### 4. Hallucination Module (Single-Frame Inference)

- **IN:** Single image feature $\phi_t$.

- Predict past and future pose changes via $f_{\Delta t}$
- Use a **fully connected network** to predict hallucinated temporal representation $\tilde{\Phi}_t$.
- **OUT:** Hallucinated 3D motion from a single image.

#### **5. Loss Computation**
- **IN:** Ground-truth 2D pose, 3D pose (if available).
- Compute $L_{2D}$, $L_{3D}$, $L_{\text{adv}}$, $L_{\text{hall}}$.
- **OUT:** Optimized model parameters.

#### **6. Training on Unlabeled Video**
- **IN:** Videos without ground truth 3D annotations.
- **Processing:**
- Generate pseudo-ground truth 2D pose using **OpenPose**.
- Train the model with 2D pose supervision.
- **OUT:** Improved 3D human dynamics model.
