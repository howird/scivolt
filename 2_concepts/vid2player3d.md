---
tags:
  - paper
  - ai/rl
status: backlog
year: 2023/08
authors: Haotian Zhang, Ye Yuan, Viktor Makoviychuk, Yunrong Guo, Sanja Fidler, Xue Bin Peng, Kayvon Fatahalian
citekey: zhang2023vid2player3d
aliases:
  - vid2player3d
---
# Learning physically simulated tennis skills from broadcast videos

## Overview

### Background and Motivation

- Tennis is a highly dynamic sport requiring precise coordination, diverse skills, and strategic decision-making.
- Traditional motion capture (mocap) methods to generate lifelike animations are limited by:
    - High costs.
    - Difficulty in capturing large datasets for specific athletic activities.
- Broadcast sports videos provide a vast, accessible source of real-world motion data but are challenging to utilize due to:
    - Low-quality motion estimation.
    - Absence of explicit skill annotations.
    - Lack of 3D context in most cases.

### Problem Statement

- Can we create a system that learns diverse and realistic tennis skills directly from unstructured broadcast video data?
- How do we address the noisy, incomplete, and kinematically implausible data extracted from video sources?
- Can the system synthesize physically plausible tennis motions and control characters for extended rally play?

### Contributions

- **Hierarchical Motion Learning:**
    - Combines low-level imitation for tracking video-based motion data with high-level planning for long-term goals.
- **Physics-Corrected Motion Reconstruction:**
    - Corrects noisy motions using physics-based constraints and reinforcement learning.
- **Skill Generalization Without Annotations:**
    - Learns complex tennis strokes (e.g., topspin, slices) without explicit labeling in the source data.
- **Player-Specific Styles:**
    - Captures distinctive traits of professional players (e.g., Federer’s one-handed backhand, Nadal’s left-handed play).
- **Two-Player Interaction:**
    - Simulates extended rallies with plausible racket and ball dynamics.

### Key Insights

- Large-scale video data is sufficient to train controllers for sophisticated physical simulations.
- Physics-based corrections significantly enhance the quality and plausibility of noisy kinematic data.
- High-level controllers can generalize diverse tennis skills from noisy embeddings, enabling strategic gameplay.

### Potential Applications

- **Sports Analytics:**
    - Evaluate and model player performance and styles.
- **Game Development:**
    - Generate lifelike, interactive character behaviors for tennis games.
- **Animation and Film:**
    - Automate the creation of realistic sports animations without requiring mocap studios.

### Limitations and Challenges

- Nuanced motion traits of professional athletes (e.g., wrist pronation, subtle timing adjustments) remain difficult to capture.
- Low-quality video data introduces artifacts that require advanced corrections and constraints.
- Simulating player strategies and decision-making (e.g., point-winning tactics) is not addressed.

### Recommended Prerequisites

- Understanding of physics-based character animation and reinforcement learning:
    - **SimPoE: Simulated Policy Optimization for Example-based Motion Imitation.**
    - **Motion VAE: Generative Models for Learning Motion Embeddings.**
- Basics of monocular motion estimation and human dynamics:
    - **HybrIK: Hybrid Inverse Kinematics for Human Pose Estimation.**

### Unique Perspectives Missing from the Abstract

- A thorough exploration of the scalability of motion reconstruction pipelines when applied to sports other than tennis.
- The implications of integrating residual force correction with player-specific style capture.
- Broader applications in learning strategies for team sports using competitive self-play.

### Project Pipeline for "Learning Physically Simulated Tennis Skills from Broadcast Videos"

#### Overview

The project demonstrates a system that learns physically simulated tennis skills from broadcast videos using hierarchical models. It consists of four stages: video annotation, low-level imitation policy training, motion embedding, and high-level motion planning. Below is the detailed pipeline.

---

### Video Annotation

#### Data Collection

- Collect broadcast tennis videos, focusing on specific players.
- Extract 2D and 3D player poses using off-the-shelf detection models (e.g., YOLO4 and ViTPose).
- Employ HybrIK to estimate body shape and pose parameters for SMPL.

#### Global Trajectory and Camera Estimation

- Use Perspective-N-Point algorithms and court line detection to compute camera transformations.
- Map root position and orientation into global court coordinates.

#### Manual Annotations

- Annotate ball contact frames and player identities to aid phase modeling of tennis motions.

---

### Low-Level Imitation Policy

#### Purpose

- Correct physically implausible motions from video data (e.g., jitter, foot sliding).
- Enable a simulated character to track reference motions in a physically consistent manner.

#### Implementation

- Model imitation as a Markov Decision Process (MDP) and train using deep reinforcement learning.
- Input: Joint positions, velocities, and rotations.
- Action: Target joint angles for proportional derivative (PD) controllers and residual forces for fine corrections.
- Rewards: Measure alignment with reference motion while minimizing energy expenditure.

#### Training

1. Pre-train using high-quality mocap data.
2. Fine-tune using kinematic tennis motions to better adapt to noisy data.
3. Output physically corrected motions.

---

### Motion Embedding

#### Purpose

- Encode corrected motion data into a compact, low-dimensional latent space.
- Facilitate high-level control for generating diverse tennis motions.

#### Method

- Utilize a conditional Variational Autoencoder (VAE) with:
    - Input: Pose in global court coordinates, velocities, and joint rotations.
    - Output: Next pose and motion phase.
- Employ autoregressive decoding to predict long-term motion sequences.
- Represent tennis phases cyclically (e.g., shot preparation, ball contact, recovery).

#### Training

- Train with scheduled sampling to stabilize autoregressive predictions.
- Optimize KL divergence to balance flexibility and plausibility of generated motions.

---

### High-Level Motion Planning Policy

#### Purpose

- Generate kinematic target motions to perform tasks like hitting tennis balls to specific court locations.

#### State and Action Representation

- State: Character pose, ball trajectory predictions, and task objectives.
- Action: Latent codes for MVAE and joint corrections for the swing arm.

#### Rewards

- Pre-contact: Minimize racket-ball distance.
- Post-contact: Align ball bounce position with the target while ensuring spin direction.

#### Training

1. **Curriculum Learning:**
    - Begin with simplified tasks to explore motion embedding.
    - Progress to complex tasks with higher precision requirements.
2. Train using PPO and refine control strategies for long-term planning.

#### Hybrid Control

- Overwrite MVAE-generated wrist motions with direct corrections from the high-level policy to ensure accurate racket positioning.

---

### Physics Modeling

#### Racket and Grip

- Simulate racket as rigid cylinders with realistic restitution and friction.
- Configure grip orientation to reflect player-specific styles.

#### Ball Dynamics

- Simulate air drag and Magnus forces to model spin-induced trajectory changes.
- Incorporate accurate physics for racket-ball interaction.

---

### Results and Analysis

#### Task Performance

- Evaluate hit rate, bounce-in rate, and bounce position error across multiple simulated sessions.
- Demonstrate ability to handle diverse shot types and extended rallies.

#### Motion Quality

- Measure physical plausibility using metrics like jitter and foot sliding.
- Show improvement over raw motion data through physics correction and MVAE embedding.

#### Player-Specific Styles

- Train separate controllers to capture distinct styles (e.g., one-handed vs. two-handed backhands, handedness).

---

### Summary

This project combines video imitation, physics-based corrections, and reinforcement learning to generate controllers capable of playing tennis in simulated environments. The approach emphasizes leveraging large-scale, unannotated video data to model complex athletic motions with high fidelity.

## Background


### Problem

- 

### Goals / Contributions

- 

### Past Work

- 

## Methodology

> [!abstract]

- 

## Results

> [!abstract]

- 

## Comments and Implications

- 
