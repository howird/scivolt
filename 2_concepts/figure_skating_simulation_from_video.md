---
tags:
  - 'paper'
status: backlog
year: '2019/01'
authors: 'Ri Yu, Hwangpil Park, Jehee Lee'
citekey: 'yuFigureSkatingSimulation2019'
---
# Figure Skating Simulation from Video



## Background

#### Recommendations for Prerequisite Knowledge
- Familiarity with:
    - Trajectory optimization and the use of B-splines for motion smoothing.
    - Deep Reinforcement Learning (specifically Proximal Policy Optimization).
    - Non-holonomic constraints in physics simulations.
- Related works providing foundational insights:
    - Al Borno et al., 2013: Trajectory optimization techniques.
    - Peng et al., 2018: DRL for imitating human motions.

### Problem

- Proposes a system for simulating figure skating movements using a physically simulated human-like character
- Focuses on achieving realistic skating motions by replicating blade dynamics and human movement on ice
- Utilizes a combination of pose estimation from videos, trajectory optimization, and reinforcement learning to overcome challenges in motion capture and dynamic simulations

#### Key Challenges Addressed
- **Lack of Data**:
    - Figure skating motions are too fast and dynamic to capture with conventional motion capture systems
    - Large areas required for motion capture setups in ice rinks add logistical and financial constraints
- **Blade-Ice Dynamics**:
    - Simulating the interaction between a skate blade and a slippery ice surface with non-holonomic constraints
    - Modeling the precise mechanics of turning and gliding, especially with the unique blade geometry
- **Dynamic Motion Simulation**:
    - Handling complex and high-speed movements like jumps, spins, and transitions with physics-based models
    - Ensuring robustness against perturbations and variability in motion speed

### Goals / Contributions

- **Novel Data Acquisition**:
    - Introduces the use of Human Mesh Recovery (HMR) to extract 3D poses from 2D skating videos.
    - Highlights manual refinement and pose editing as a crucial step to improve data quality.

- **Multi-Step Optimization**:
    - Applies trajectory optimization using cubic B-splines and window-based objectives for smooth motion generation.
    - Demonstrates a modular approach for skill-specific optimizations (e.g., jumps, crossovers).

- **Robustness via Deep Reinforcement Learning (DRL)**:
    - Extends optimized motion sequences into robust controllers capable of handling variable speeds and external perturbations.
    - Achieves generalizable control for figure skating motions under diverse conditions.


### Past Work

- 

## Methodology

#### Tools and Frameworks
1. **Libraries**:
   - HMR for pose estimation.
   - CMA-ES for optimization.
   - PyTorch for DRL implementation.
2. **Physics Engine**:
   - DART for dynamics simulation.

#### Overview
- **Objective**: Simulate figure skating motions of a human-like character on ice using keyframes from videos, trajectory optimization, and reinforcement learning
- **Components**:
    - Data acquisition from video frames
    - Trajectory optimization
    - Robust control design using reinforcement learning
- **Outputs**: Physically simulated figure skating skills (e.g., crossover, three-turn, jump)

#### Data Acquisition
##### Input
- Source: YouTube figure skating videos.
- Selection: Identify and extract key frames manually to represent key poses in the skating sequence.

##### Pose Estimation
- Method: Use Human Mesh Recovery (HMR) to infer 3D poses from video frames.
- Output: 3D human mesh with joint positions.
- Limitation: Manually correct inaccuracies in poses caused by occlusion or dynamic actions.

#### Trajectory Optimization
##### Objective
Generate smooth, physically plausible reference motions from key poses.

##### Process
1. **Initialization**:
    - Represent key poses as a sequence: $Sq = \{q_1, q_2, ..., q_T\}$.
    - Incorporate high-level objectives such as maintaining balance and generating required motion patterns.

2. **Optimization Framework**:
    - Algorithm: Covariance Matrix Adaptation Evolution Strategy (CMA-ES).
    - Basis: Key poses are interpolated using cubic B-splines for smoothness.

3. **Windows of Optimization**:
    - Divide motion into multiple windows (e.g., preparation, in-air, and landing for a jump).
    - Define objective functions for each window, such as center-of-mass height, angular momentum, and velocity.

##### Outputs
- A complete trajectory for the figure skating motion.
- Inputs for the controller design.

#### Controller Design Using Deep Reinforcement Learning (DRL)
##### Approach
1. **Framework**:
   - Use a DRL-based control system to mimic reference trajectories.
   - Algorithm: Proximal Policy Optimization (PPO).
2. **Inputs**:
   - Phase variables, body link positions, velocities, and angular momenta.
3. **Policy Learning**:
   - Objective: Learn robust controllers capable of handling perturbations and varying speeds.
   - Output: Displacement vectors for pose tracking via proportional-derivative (PD) control.

#### Simulation and Testing
##### Skater Model
- Parameters: 1.5 m height, 50 kg weight, and a blade with specific dimensions.
- Environment: Low-friction coefficient (0.02) to simulate ice.

##### Skills Demonstrated
- **Forward Stroking**: Alternate propelling and gliding.
- **Crossover**: Turning using crossed legs.
- **Three-Turn**: Switching between forward and backward skating.
- **Jump**: Simulate double Salchow with multiple in-air phases.
## Results

### Evaluation

1. **Robustness Testing**:
   - Perturbations: Apply external forces and evaluate recovery
   - Speed Variations: Test controllers at different motion speeds
2. **Performance Metrics**:
   - Smoothness of motion
   - Robustness to disturbances

## Comments and Implications

### Limitations and Future Work
1. **Pose Estimation**:
    - Improve automatic detection accuracy using datasets with dynamic and acrobatic poses.
1. **Realistic Blade Modeling**:
    - Enhance blade design to simulate edge effects and spins accurately.
2. **Integration**:
    - Combine trajectory optimization and policy learning for better performance.

#### Limitations Highlighted
- Manual intervention required for pose correction due to inaccuracies in existing 3D pose estimation techniques.
- Simplified blade geometry and interaction models limit the precision of simulated edge-based movements (e.g., spins).
- Lacks integration of self-collision detection and handling during complex motions.
- Spin simulation remains challenging due to current friction modeling limitations.