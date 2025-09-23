---
tags:
  - paper
status: todo
year: 2021/12
authors: Jathushan Rajasegaran, Georgios Pavlakos, Angjoo Kanazawa, Jitendra Malik
citekey: rajasegaranTrackingPeoplePredicting2021
---
# Tracking People by Predicting 3D Appearance, Location & Pose

## Objective: Track people in monocular videos by lifting 2D detections to 3D representations and predicting these representations into the future for robust association

* **Motivation:** Argues that tracking in 3D is advantageous over 2D tracking, especially for handling occlusions, as objects persist in 3D space

**Methodology:**

* **3D Lifting:** Uses a modified HMAR network to extract 3D pose, 3D location (in camera coordinates), and 3D appearance (texture map on a canonical UV surface) from single-frame 2D detections (bounding boxes and masks)[cite: 2, 3, 38, 39, 83, 85].
    * HMAR is modified to use segmentation masks to improve robustness in crowded scenes[cite: 87, 88].
* **Tracklet Representation:** Aggregates the single-frame 3D observations over time for each tracked person (tracklet)[cite: 4, 32, 40].
* **Temporal Prediction Models:**
    * **Appearance:** Aggregates appearance using a weighted average of UV maps over time. Predicts future appearance using the most recent aggregated map (assumes slow appearance change)[cite: 41, 98, 100, 107, 108].
    * **Pose:** Uses a transformer-based model (inspired by HMMR) to aggregate pose embeddings over time and predict future pose embeddings[cite: 42, 75, 125, 126, 132].
    * **Location:** Predicts future 3D location using independent linear regression on past observations in a modified space: $(x, y, n)$, where $(x, y)$ are image coordinates and $n$ is nearness ($log(1/Z)$)[cite: 43, 111, 113, 117, 119]. Prediction intervals ($\delta_x, \delta_y, \delta_n$) are also estimated[cite: 120, 122].
* **Association:**
    * Calculates the similarity between the *predicted* 3D state of a tracklet and the *observed* 3D state of new detections in a probabilistic framework[cite: 7, 47, 130].
    * Models the conditional probability of a match given the distance for each attribute:
        * Appearance distance ($\Delta_a$): Cauchy distribution, $\mathcal{P}_{A} \propto \frac{1}{1+\beta_{a}\Delta_{a}}$[cite: 145].
        * Pose distance ($\Delta_p$): Cauchy distribution, $\mathcal{P}_{P} \propto \frac{1}{1+\beta_{p}\Delta_{p}}$[cite: 146, 148].
        * 2D Location distance ($\Delta_{xy}$): Exponential distribution, $\mathcal{P}_{XY} \propto \frac{1}{\beta_{xy}}exp(\frac{-\Delta_{xy}}{\beta_{xy}\delta_{xy}})$ (distance normalized by prediction interval $\delta_{xy}$)[cite: 150, 152].
        * Nearness distance ($\Delta_n$): Exponential distribution, $\mathcal{P}_{N} \propto \frac{1}{\beta_{n}}exp(\frac{-\Delta_{n}}{\beta_{n}\delta_{n}})$ (distance normalized by prediction interval $\delta_n$)[cite: 150, 153].
    * Combines probabilities (assuming independence) and converts to a cost ($-\log(\mathcal{P})$) for the Hungarian algorithm to solve the assignment problem[cite: 8, 48, 158, 160, 161].
    * Parameters ($\beta_a, \beta_p, \beta_{xy}, \beta_n, \beta_{th}$) are optimized using empirical risk minimization[cite: 162, 163, 164].
* **Tracklet Update:** Matched detections are used to update the temporal models of their respective tracklets[cite: 8, 49, 12].
* **Shot Change Handling:** Can adapt to shot changes (detected externally) by removing the location component from the similarity calculation[cite: 51, 166, 168, 169].

**Key Assumptions:**

* Availability of reliable 2D person detections and segmentation masks from an external source (e.g., Mask-RCNN)[cite: 58, 82, 172, 193].
* The underlying 3D human mesh recovery model (HMAR) provides accurate enough single-frame 3D lifting[cite: 193, 194].
* Human appearance does not change drastically over short time periods for the appearance prediction to be effective[cite: 103, 107].
* Short-term human motion can be reasonably approximated by linear regression in the $(x, y, \text{nearness})$ space[cite: 62, 113, 115].
* Appearance, pose, and location cues are independent for probabilistic association[cite: 158].

**Prerequisite Knowledge (Recommended):**

* **HMAR:** Understanding the Human Mesh and Appearance Recovery model used as the feature backbone
* [SMPL](2_concepts/smpl.md) Familiarity with the Skinned Multi-Person Linear model, the parametric body model used by HMAR[cite: 41, 70].
* [HMMR](2_concepts/hmmr.md) Knowledge of the Human Mesh and Motion Recovery model, as the pose prediction module builds on its principles[cite: 42, 75, 124].
* **Tracking-by-Detection:** General concept of detecting objects in each frame and then associating detections across frames.
* **Hungarian Algorithm:** Standard algorithm for solving the assignment problem used in the association step


- **Approach**: 
- **IN:** 
- **OUT:** 
    - 
    - 

- **Existing Dependencies:**
    - **Model:** 
    - **(, , ) datasets:** PoseTrack, MuPoTS and AVA

## Challenges

- **CHALLENGE 1**: 
    - **Approach:** 
    - **Hypothesis:** 
- **CHALLENGE 2**: 
    - **Approach:** 
    - **Hypothesis:** 

## Method

METHOD PIPELINE DIAGRAM

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

- 

