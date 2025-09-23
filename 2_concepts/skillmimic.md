---
tags:
  - paper
status: doing
year: '2024/08'
authors: Yinhuai Wang, Qihan Zhao, Runyi Yu, Ailing Zeng, Jing Lin, Zhengyi Luo, Hok Wai Tsui, Jiwen Yu, Xiu Li, Qifeng Chen, Jian Zhang, Lei Zhang, Ping Tan
citekey: wangSkillMimicLearningReusable2024
---
# SkillMimic: Learning Reusable Basketball Skills from Demonstrations

## Background

### Problem

- Current SOTA methods train RL algos with [adversarial motion rewards](2_concepts/adversarial_motion_priors.md) to mimic isolated body movements, for human-like control
- These motion priors and combined with manually designed skill rewards to learn interaction skills, such as striking pillars
- Designing these skill rewards is __labor intensive__ and __difficult to generalize__ across different skills

### Goal

- Motivation:
    - most basketball players, even without formal coaching, can learn various skills by watching basketball videos and practicing diligently
    - to learn, they adjust their body movements to align with both the reference body motions and the reference ball movements they observe

- Goal:
    - Learn a motion controller that can perform tasks in basketball from human demonstrations
    - This paradigm of learning skills from demonstrations allows a basketball player to acquire a set of reusable basketball skills and flexibly combine them for further purposes

### Goals / Contributions

- SkillMimic:
    - A data-driven paradigm for learning reusable interaction skills, capable of learning diverse basketball skills in a unified manner
    - It supports joint learning and smooth switching of skills, with skill diversity and generalization improving as the dataset grows

- Contact Graph:
    - We propose a simple and general contact modeling method that applies to diverse skills, called the contact graph
    - A Contact Graph Reward (CGR) is designed to enable precise contact imitation, which proves to be critical for learning precise interaction skills

- Unified skill imitation reward:
    - We propose a set of important designs that form a unified reward configuration for imitation learning of various interaction skills
    
- A hierarchical solution for learning complex basketball tasks:
    - training a high-level controller to flexibly compose the skills acquired by SkillMimic to accomplish challenging high-level tasks
    
- BallPlay Datasets:
    - We introduce two basketball datasets to facilitate research on basketball skill learning

### Past Work

- How does this differ from [deepmimic](2_concepts/deepmimic.md) or [AMP](2_concepts/adversarial_motion_priors.md)

## Methodology

> [! abstract]

![](2_concepts/media/Pasted%20image%2020241105141127.png)
- (a) we capture real-world basketball skills to create a large Human-Object Interaction (HOI) motion dataset
- (b) train a skill policy to learn interaction skills by imitating the corresponding HOI data
    - Specifically, the policy takes as input the HOI state $s_t$ and skill label $c_j$ and predicts the action $a_t$, the new state $s_{t+1}$ is calculated by the simulator
    - A unified HOI imitation reward is designed to imitate diverse HOI state transitions
- (c) train a High-Level Controller (HLC) to reuse the learned skills for complex tasks. The HLC takes as input $s_t$ and extra task observations $h_t$
    - e.g., the basket position, and predicts the skill label ct to drives a pre-trained skill policy

#### Dataset Preparation

1. **Data Sources**
    - **BallPlay-V**: Human-object motion data estimated from monocular RGB videos.
    - **BallPlay-M**: High-fidelity human-object motion capture data with optical sensors

2. **Annotation Techniques**
    - Depth estimation and semantic segmentation for BallPlay-V.
    - Full-body skeleton tracking and basketball motion capture for BallPlay-M.

3. **Key Outputs**
    - Labelled clips for each skill (e.g., dribbling, shooting, layups).
    - Data structure includes skeleton joints, ball dynamics, and environmental context.

#### Defining Skills

1. **Human-Object Interaction (HOI)**
    - Skills are modeled as sequences of HOI state transitions.
    - Each frame represents a specific state, and transitions between states define skill execution

1. **Skill Representation**
    - Clips represent diverse examples of each skill (e.g., pickup actions at various positions).
    - Aggregated data captures both human motion and ball dynamics.


#### Imitation Learning Framework

1. **Skill Policy Training**
    - Use reinforcement learning to mimic HOI data.
    - Input: Current state and skill label.
    - Output: Actions calculated to replicate reference transitions.

2. **Reward Mechanisms**
    - Unified HOI imitation reward combines body and object motion alignment, relative motion accuracy, and contact precision.
    - Contact Graph Reward ensures realistic and precise human-ball interactions.

#### Physical Simulation and Training Environment

1. **Simulation Details**
    - Physics-based simulations using Isaac Gym.
    - High frame rates to capture dynamic interactions (60 Hz for BallPlay-V, 120 Hz for BallPlay-M)

2. **Policy Design**
    - Multi-layer perceptron networks predict actions based on input states.
    - Policies are skill-agnostic, enabling smooth switching between learned skills.

#### High-Level Controller (HLC) for Complex Tasks

1. **Task Representation**
    - Each task is a composition of learned skills, such as dribbling followed by layup.
    - HLC selects skills dynamically based on task requirements

2. **Reward Design**
    - Simplified goal-oriented rewards (e.g., maximizing ball height during throws).
    - No need for task-specific interaction rewards.

---

#### Experimental Validation

1. **Skill Learning Evaluation**
    - Metrics: Position error, contact accuracy, success rates for skill execution.
    - Dataset scaling shows improved performance with larger datasets

2. **Complex Task Demonstrations**
    - Tasks include scoring, dribbling, and circling around targets.
    - HLCs trained with simple rewards effectively combine learned skills.

#### Scalability and Generalization
1. **Zero-Shot Skill Switching**
    - Policies trained with mixed datasets exhibit robust skill transitions not present in training data 
2. **Adaptability**
    - Skills generalize across varied physical properties (e.g., ball size and density).

## Results

> [!abstract]

- 

## Comments and Implications

- 
