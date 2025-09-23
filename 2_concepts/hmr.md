---
tags:
  - paper
status: todo
year: 2018/06
authors: Angjoo Kanazawa, Michael J. Black, David W. Jacobs, Jitendra Malik
citekey: kanazawaEndtoendRecoveryHuman2018
---
# HMR: End-to-end Recovery of Human Shape and Pose

## Objective: Robust Recovery of 3D Human Body Mesh from a Single RGB Image

- **Approach**: infer 3D mesh parameters directly from image features
- **IN:** Cropped Images of People $I$
- **OUT:** 3D human pose and shape at each frame $\Theta_t = \{ \beta, \theta, \Pi \}$
    - Pose: $\theta \in \mathbb{R}^{3K}$ ($K=23$ joints, axis-angle representation)
    - Shape: $\beta \in \mathbb{R}^{10}$ (PCA-based shape space)
    - Orthographic Projection, $\Pi$, parameterized by:
        - Rotation: $R \in \mathbb{R}^{3 \times 3}$ (axis-angle)
        - Translation: $t \in \mathbb{R}^2$
        - Scale: $s \in \mathbb{R}$

- **Existing Dependencies:**
    - **[SMPL Model](2_concepts/smpl.md):** enables us to learn low dimensional, semantically significant, representations for Human Meshes ($\beta, \theta$) rather than learn the actual mesh
    - **(Image, 2D pose, Per-Joint Visibility) datasets:** LSP, LSP-extended, MPII, MS COCO
    - **(Image, 3D pose, SMPL) datasets:** Human3.6M and MPIINF-3DHP
        - Images without SMPL parameters were labelled with MoSh
    - **3D mesh (SMPL) datasets:** CMU, Human3.6M (train set), PosePrior
    - **ImageNet trained ResNet:** Used to get image features


## Challenges

- **CHALLENGE 1**: How can we supervise training of a regression model for 3D pose with (mostly) 2D pose labels?
    - **Hypothesis:** 3D labels are not (necessarily) needed - we can regress 3D pose by using the error between 2D labels and 3D pose projected to 2D as our loss
    
- **CHALLENGE 2**: How can we estimate the correct 3D pose and shape parameters when there are many possible 3D body configurations for a given 2D projection?
    - **Hypothesis:** We can use a [GAN](2_concepts/GAN.md) to discriminate incorrect but (mathematically) possible configurations because:
        - they are not anthropomorphically reasonable due to impossible joint angles or extremely skinny bodies
        - they are too large/small which can solve scale ambiguity between the size of the person and the camera distance

## Method

![HMR main diagram](2_concepts/media/hmr.png)


### Stage 1: Training the Adversarial Discriminator

- Discriminator trained on dataset before training main regression task

- $D_\beta$: two fully-connected layers with 10, 5, and 1 neurons
- $f_{\text{embed } \theta}$:
    - For pose, $\Theta$ is first converted to K many $3 \times 3$ rotation matrices via the Rodrigues formula
    - Each rotation matrix is sent to a common embedding network of two fully-connected layers with 32 hidden neurons
- $D_{\theta \text{ all}}$ The discriminator for overall pose distribution concatenates all $K \times 32$
- $D_{\theta i\in [1, K=23]}$: 2 fully-connected layers of 1024 neurons each and finally outputs a 1D value

- All layers use ReLU activations except the final layer. The learning rates of the encoder and the discriminator network are set to $1 \times 10^{−5}$ and $1\times 10^{−4}$ respectively. We use the Adam solver and train for 55 epochs


### Stage 2: Training the Regressor

#### 0. Preprocessing

- **IN**: RGB Image $I \in \mathbb{R}^{H \times W \times 3}$

- Resizing: All images are scaled to 224 × 224 preserving the aspect ratio s.t. the diagonal of the tight bounding box is roughly 150px
- Augmentations: Randomly scaled, translated, and flipped
- Mini-batch size is 64
    - when paired 3D supervision is employed each mini-batch is balanced such that it consists of half 2D and half 3D samples

- **OUT**: RGB Image $I \in \mathbb{R}^{224 \times 224 \times 3}$

#### 1. Image Encoding

- **IN**: RGB Image $I \in \mathbb{R}^{224 \times 224 \times 3}$
- ResNet-50 (pre-trained on ImageNet), average pooled, flattened
- **OUT**: Feature vector $\phi \in \mathbb{R}^{2048}$

#### 2. Iterative 3D Regression

- **IN**: 
    - Feature vector $\phi \in \mathbb{R}^{2048}$
    - Current estimate $\Theta_t$, where:
        - $\Theta_0 = \bar{\Theta}$ (mean pose & shape parameters from train set)
    
- for $t$ in $T=3$:
    - $\Delta \Theta_t := f_{\text{regressor}}(\phi, \Theta_t)$
    - two fully-connected layers with 1024 neurons each with a dropout layer in between, followed by a final layer of 85
    - $\Theta_{t+1}: = \Theta_t + \Delta\Theta_t$
- $\Theta = \Theta_T$

- **OUT**: Estimated parameters $\Theta = \{ \theta, \beta, R, t, s \}$

- note: for a single forward pass, the entire loop ($t, ..., T$) of [iterative error feedback](2_concepts/iterative%20error%20feedback.md) occurs

#### 3. Weak-Perspective Projection

- **IN**: Estimated 3D keypoints $X(\theta, \beta)$
- Apply weak perspective transformation:
$$
\hat{x} = s \Pi(R X(\theta, \beta)) + t
$$
- where:
    - Orthographic Projection, $\Pi$, parameterized by:
        - Rotation: $R \in \mathbb{R}^{3 \times 3}$ (axis-angle)
        - Translation: $t \in \mathbb{R}^2$
        - Scale: $s \in \mathbb{R}$
    - SMPL Mesh to Joint regressor $X: \theta \times \beta \rightarrow \hat x \in \mathbb{R}^{3 \times P}$
- **OUT**: Projected 2D keypoints $\hat{x} \in \mathbb{R}^{2 \times P}$

#### 4. Reprojection Loss Computation

- **IN**:
    - Projected keypoints $\hat{x}$
    - Ground-truth 2D keypoints $x$
    - Visibility mask $v$
    
- Reprojection Loss (ensuring 3D joints match 2D projections):
$$
L_{\text{reproj}} = \sum_i ||v_i (x_i - \hat{x}_i)||_1
$$
- where:
    - $x_i$ = ground truth 2D joint locations
    - $\hat{x}_i$ = projected 3D joint locations
    - $v_i$ = visibility indicator (1 if visible, 0 otherwise)

- 3D Loss (if available):
$$
L_{\text{3D}} = L_{\text{3D joints}} + L_{\text{3D smpl}}
$$
- where:
$$
L_{\text{3D joints}} = ||(X_i - \hat{X}_i)||_2^2
$$
$$
L_{\text{3D smpl}} = ||[\beta_i, \theta_i] - [\hat{\beta}_i, \hat{\theta}_i]||_2^2
$$

- **OUT**: Loss value


#### 5 Adversarial Loss

- **IN**:
    - Pose $\theta$
    - Shape $\beta$
    - Pre-trained discriminators:
        - Per-joint pose discriminator $D_{\theta}$
        - Overall shape discriminator $D_{\beta}$
    
- Computes probability of realism:
$$
L_{\text{adv}} = \sum_i D_i(E(I))
$$
- **OUT**: Adversarial loss value


- Adversarial Loss (ensuring realistic human body configurations):
$$
L_{\text{adv}} = \sum_i \mathbb{E}_{\Theta \sim p_E} [(D_i(E(I)) - 1)^2]
$$
where:
- $D_i$ is the discriminator for pose/shape.
- $E(I)$ is the encoder output for image $I$

- Total Loss:
$$
L = \lambda (L_{\text{reproj}} + 1 L_{\text{3D}}) + L_{\text{adv}}
$$


#### 6. Backpropagation & Model Update
- **IN**:
    - Total loss $L = \lambda (L_{\text{reproj}} + 1 L_{\text{3D}}) + L_{\text{adv}}$
        - $\lambda$ is a weighting factor
- Process:
    - Update weights using Adam optimizer
i
- **OUT**: Updated model weights



### Final Outputs
- Full 3D human mesh $M(\theta, \beta) \in \mathbb{R}^{3 \times 6980}$
- Estimated 3D pose $\theta \in \mathbb{R}^{3K}$
- Estimated shape $\beta \in \mathbb{R}^{10}$
- Projected 2D keypoints $\hat{x} \in \mathbb{R}^{2 \times P}$

This provides real-time human shape recovery from a single image.


## Results

- 2 protocols
    - downsample all videos from 50fps to 10fps to reduce redundancy


### Does it do 3D pose good?

- P1: is trained on 5 subjects (S1, S5, S6, S7, S8) and tested on 2 (S9, S11)
    - measures 3D joint error
- note they use [procrustes analysis](2_concepts/procrustes%20analysis.md) when calculating MPJPE

![protocol 1 results](2_concepts/media/Pasted%20image%2020250312211117.png)

### Does it do 2D pose good?

![protocol 2 results](2_concepts/media/Pasted%20image%2020250312211144.png)

- P2: uses the same train/test set, but is tested only on the frontal camera (camera 3) and reports reconstruction error
    - measures 3D to 2D projection error

### Can it translate to segmentation?
![segmentation results](2_concepts/media/Pasted%20image%2020250312211331.png)

- comparable to the SMPLify oracle, which uses ground truth segmentation and keypoints as the optimization targe
- note: that HMR is also real-time given a bounding box

### Does it do good without 3D training loss, just 2D projection?

- all previous methods rely on 3D loss, and when training on just 2D data it gets close (its called unpaired when 3D is not used)