---
tags:
  - paper
status: todo
year: 2021/11
authors: Jathushan Rajasegaran, Georgios Pavlakos, Angjoo Kanazawa, Jitendra Malik
citekey: rajasegaranTrackingPeople3D2021
---
# HMAR: Tracking People with 3D Representations

* **Key Findings:**
    * 3D representations (appearance, pose, location) are shown to be more effective for tracking than their 2D counterparts, particularly in handling occlusions and viewpoint changes
    * The approach achieves state-of-the-art performance on datasets like Posetrack, MuPoTs, and AVA, including videos with shot changes
    * Ablation studies confirm the importance of all three 3D cues (appearance, pose, location) and the spatio-temporal aggregation provided by the transformer

## Objective: Robust Recovery of 3D Human Body Mesh and Appearance  from Video

- **Previous Work**:
    - **[HMR](2_concepts/hmr.md):** given a cropped RGB image of a human ($I$), predicts 3D mesh (SMPL) parameters ($\theta$, $\beta$), and camera parameters

* **Problem:** Traditional methods for tracking multiple people in videos predominantly rely on 2D representations, which struggle with occlusions and variations in viewpoint and pose
* **Proposed Solution:** This paper introduces a novel tracking approach leveraging 3D representations of people[cite: 1, 2].
    * It utilizes a model called Human Mesh and Appearance Recovery (HMAR)[cite: 3, 23]. HMAR extends existing methods (like HMR [cite: 17, 22]) to extract not only the 3D mesh (geometry using SMPL model [cite: 3, 48]) but also the 3D appearance as a texture map applied to the mesh[cite: 3, 21, 23]. This texture map provides a viewpoint and pose-invariant appearance representation[cite: 4, 16, 77].
    * For each detected person (bounding box) in a video frame, HMAR extracts 3D appearance, 3D pose, and 3D location information[cite: 5, 24, 28, 54, 86, 109].
    * These extracted 3D features (embeddings) are then processed by a transformer model
        * The transformer performs spatio-temporal aggregation, allowing information to diffuse across detections over time and space based on similarity (attention)
    * Finally, the similarity between the aggregated representations is used for association, linking detections across frames to form tracklets

- **Approach**: 
- **IN:** 
- **OUT:** 
    - 
    - 

- **Existing Dependencies:**
    - **Model:** The method assumes that initial bounding box detections for people are provided by an external, off-the-shelf detector
        * The focus is purely on the association task using the proposed 3D representations.
    - **(, , ) datasets:** 

Okay, here is a detailed outline of the problem formulation for the project described in the paper "Tracking People with 3D Representations":

**I. Overall Goal**

- To track multiple people in a monocular video sequence by assigning a consistent identity (tracklet ID) to each person's detection across different frames.
- To leverage 3D representations (geometry and appearance) to improve tracking robustness, especially against occlusion, viewpoint changes, and pose variations, compared to traditional 2D methods.

**II. Input**

- A monocular video sequence.
- A set of bounding box detections for each frame t, denoted as {$B_{t,i}$​}, where i indexes the detected person in frame t. These are assumed to be provided by an external detector.

**III. Output**

- A set of tracklets $T=\{Tr_j\}$, where each tracklet $Tr_j$​ is a sequence of bounding box detections $(B_{t,i}​,t)$ assigned to the same unique identity $j$ across time $t$.

**IV. Key Steps & Formulations**

1. **3D Feature Extraction (per detection)**
    
    - For each input bounding box $B_{t,i}$​, use the Human Mesh and Appearance Recovery (HMAR) model to extract 3D features.
    - **3D Appearance (a):**
        - HMAR predicts a texture map Itex​ representing appearance in a viewpoint/pose invariant UV space.
        - This texture map is encoded into a compact embedding vector a∈R512 using an autoencoder.
    - **3D Pose (p​):**
        - Represented by the embedding p​∈R2048 from the pose head of the underlying HMR architecture, capturing the body pose parameters.
    - **3D Location & Keypoints (s):**
        - Approximate global 3D translation T in camera coordinates is calculated from bounding box center $[c_x​,c_y​]$, size $b$, predicted camera parameters $[s,t_x​,t_y​]$, and assumed focal length $f$: $T=[t_x + \frac{2c_x​−W}{sb}​,t_y​+\frac{2c_y​−H}{sb}​,\frac{2f}{sb}​]$
        - 3D keypoints are extracted from the recovered mesh and positioned using the translation $T$.
        - These keypoints, along with temporal information, form a space-time representation $s\in\mathbb{R}^{90}$
2. **Spatio-Temporal Aggregation (across detections)**

- Combine the extracted features for each detection $(t,i)$ into a single vector: $h_{t,i}=[\bar a^T,\bar p^​T,\bar s^T]^T \in \mathbb{R}^{2650×1}$

- Input these vectors $h_{t,i}$ for all detections across $T$ frames and $P$ max people per frame into a transformer model
- The transformer uses a modified self-attention mechanism where attention is calculated separately for appearance, pose, and location, then combined:
$$
\mathcal{A}(t,i),(t',i')=\sum_{att\in \{app,pose,loc\}} \beta_{att} \text{softmax} (\frac{q_{att}^{t,i}​(k_{att}^{t',i'}​)^T}{\sqrt{dim_{att}}}
$$
- where qatt​,katt​ are query/key vectors for each attribute, βatt​ are weights).
- The transformer output h^t,i for detection (t,i) aggregates information from other detections based on this attention mechanism.
- **Training Objective (ReID Loss):** The transformer is trained to make embeddings $\mathcal D = \{\hat h^{t,i}\}$ for the same person across different frames similar, and embeddings for different people dissimilar, using a contrastive loss:

$$
\mathcal L_{ReID}​ = \sum_{t,t'∼[1..T]} \bigg( d(\hat h ^{t,i}, \hat h^{t',i'}) + \max \big(0, m−d(\hat h^{t,i}, \hat h^{t',j'})\big) \bigg) 
$$

- where
    - $(t,i)$, $(t',i')$: detections of the same person
    - $(t,i)$, $(t',j')$ detections of different people
    - $d$ is $L_2$​ distance, m is a margin ).

1. **Association (Online Tracking)**
    
    - Process frames sequentially (t=1,2,...,T).
    - For the current frame t, calculate an affinity matrix A between the embeddings D={h^t,i} of current detections and the embeddings associated with existing active tracklets T={Trj​}.
    - Affinity is based on the minimum distance d between the current detection embedding h^t,i and the recent history (e.g., last 20) embeddings stored for tracklet Trj​.
    - Use the Hungarian algorithm to find the optimal assignment M of detections to tracklets based on minimizing the total distance in the affinity matrix.
    - Update tracklets with assigned detections, create new tracklets for unassigned detections (new people), and manage tracklet lifecycle (e.g., remove tracks inactive for >20 frames).

## Challenges

- **CHALLENGE 1**: 
    - **Approach:** 
    - **Hypothesis:** 
- **CHALLENGE 2**: 
    - **Approach:** 
    - **Hypothesis:** 

## Method

![](2_concepts/media/Pasted%20image%2020250430215900.png)



**Stage 1: Person Detection (Preprocessing)**

- **Description:** Identifies the locations of people in each video frame. While the paper assumes detections are given, this is the necessary first step. The paper mentions using detections from an off-the-shelf detector like Faster R-CNN.
- **Input:**
    - Video Frame at time t: An image tensor, typically shape [H×W×3], where H is height, W is width.
- **Output:**
    - Set of Bounding Boxes {Bt,i​} for frame t: A list of bounding boxes, where each box Bt,i​ can be represented as [xmin​,ymin​,xmax​,ymax​] coordinates. The number of boxes varies per frame.

---

**Stage 2: HMAR Feature Extraction**

- **Description:** For each detected bounding box, extract 3D appearance, pose, and location features using the Human Mesh and Appearance Recovery (HMAR) model.
- **Input:**
    - Cropped Image Patch It,i​: The region defined by bounding box Bt,i​ from the original frame, typically resized to a fixed input size for the network (e.g., [224×224×3]).
- **Internal Processing (within HMAR):**
    - Regresses SMPL pose (θ) and shape (β) parameters.
    - Regresses camera parameters [s,tx​,ty​].
    - Predicts a texture flow field F via the Appearance Head.
    - Generates a texture map Itex​ by sampling the input patch It,i​ using F. (Shape might be e.g., [U×V×3], where U,V are UV map dimensions).
    - Encodes Itex​ into appearance embedding a using a separate trained autoencoder.
    - Extracts pose embedding p​ from an intermediate layer of the HMR backbone/pose head.
    - Calculates global 3D translation T (using Eq. 1).
    - Extracts 3D keypoints from the SMPL mesh, positions them using T, and combines with temporal information to get location embedding s.
- **Output:**
    - Combined Feature Vector ht,i: The concatenation of the three embeddings for detection i in frame t. ht,i=[aT,p​T,sT]T Shape: [2650×1] (or just 2650 if viewed as a flat vector), derived from 512 (appearance) + 2048 (pose) + 90 (location).

---

**Stage 3: Spatio-Temporal Aggregation (Transformer)**

- **Description:** Processes the raw feature vectors {ht,i} from multiple detections across time and space using a transformer model to refine the features, incorporating broader context.
- **Input:**
    - Batch of Raw Feature Vectors {ht,i}: A collection of feature vectors from detections within a temporal window (e.g., T frames) and potentially padded/limited to a maximum number of people P per frame.
    - Tensor Shape (Example): [(T×P)×2650]. The first dimension represents the total number of detection "tokens" being processed together.
- **Processing:**
    - Pass the batch through multiple transformer blocks.
    - Each block contains a modified multi-head self-attention layer (calculating attention separately for appearance, pose, location before combining, see Eq. 3) and feed-forward layers.
- **Output:**
    - Batch of Aggregated Feature Vectors {h^t,i}: Refined feature vectors incorporating spatio-temporal context.
    - Tensor Shape: Same as input, e.g., [(T×P)×2650]. Each output vector h^t,i corresponds to an input vector ht,i.

---

**Stage 4: Online Association (Tracking Algorithm)**

- **Description:** Assigns identity labels to the current frame's detections by matching them to existing tracklets based on the similarity of their aggregated features. This is typically done frame-by-frame.
- **Input:**
    - Aggregated Features for Current Frame t: {h^t,i} for all i detections in frame t. Shape: [Nt​×2650], where Nt​ is the number of detections in frame t.
    - Active Tracklet Data Tactive​: Information about ongoing tracks, including the history of aggregated features (e.g., last 20 embeddings) for each active tracklet Trj​.
- **Processing:**
    - Calculate Affinity Matrix A: Compute the distance (e.g., L2​ distance d) between each current detection feature h^t,i and the feature history of each active tracklet Trj​. Shape: [Nt​×∣Tactive​∣].
    - Matching: Apply the Hungarian algorithm to A to find the optimal assignment M that minimizes the total distance between matched detections and tracklets.
    - Tracklet Update:
        - Assign matched detections to their corresponding tracklets, updating the tracklet's feature history.
        - Initialize new tracklets for unassigned detections.
        - Manage tracklet status (e.g., increment age for unmatched tracklets, terminate tracks inactive for too long).
- **Output:**
    - Updated Tracklets T: The set of all tracklets (active and potentially terminated), where each tracklet Trj​ maps a unique ID j to a sequence of assigned bounding boxes (Bt,i​,t) over time.

### Stage 1: 

#### 0. TODO

- **IN**: RGB Image $I \in \mathbb{R}^{H \times W \times 3}$

- 

- **OUT**: RGB Image $I \in \mathbb{R}^{224 \times 224 \times 3}$

### Stage 2: Training the Regressor

#### 0. TODO


- **IN**: RGB Image $I \in \mathbb{R}^{H \times W \times 3}$

- 

- **OUT**: RGB Image $I \in \mathbb{R}^{224 \times 224 \times 3}$

#### 1. TODO

- **IN**: RGB Image $I \in \mathbb{R}^{H \times W \times 3}$

- 

- **OUT**: RGB Image $I \in \mathbb{R}^{224 \times 224 \times 3}$

## Results

- 

## Comments and Implications

* **Limitations**:
    * **Image Resolution**: The approach implicitly relies on sufficient image resolution for the 3D reconstruction (HMAR) to work effectivel
        * It is noted that the method is not evaluated on low-resolution datasets like MOTChallenge for this reason
    * **Assumption - Single Camera:** The method is designed and evaluated for monocular (single camera) video input
