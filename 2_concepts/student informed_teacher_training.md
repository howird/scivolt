---
tags:
  - paper
  - ai/rl
status: doing
year: 2024/12
authors: Nico Messikommer, Jiaxu Xing, Elie Aljalbout, Davide Scaramuzza
citekey: messikommerStudentInformedTeacherTraining2024
---
# Student-Informed Teacher Training

#### Scope and Purpose of the Paper

- Addresses limitations in privileged imitation learning, where a student learns from a teacher with access to more informative observations
- Proposes a joint training framework that adjusts the teacher's policy to be more student-friendly, ensuring learned behaviors are imitable despite the student’s limited observability
- Introduces penalty-based adjustments to encourage the teacher to consider student constraints
- Demonstrates applicability in complex real-world tasks, including vision-based quadrotor flight and robotic manipulation

#### Key Contributions

- Introduces a teacher-student co-learning framework that minimizes information asymmetry.
- Develops a joint optimization strategy for aligning teacher and student behavior.
- Implements a KL-divergence-based penalty to prevent the teacher from taking actions that the student cannot infer.
- Uses a proxy student network to approximate student actions without costly real-time student rollouts.
- Applies the method to maze navigation, quadrotor obstacle avoidance, and robotic manipulation, showing improved student performance.

#### Core Assumptions

- Privileged information leads to a gap in imitated behaviors: The teacher, trained with more complete information, may generate actions that are impossible for the student to infer
- Student observations are inherently limited: The student’s perception is typically restricted to high-dimensional inputs (e.g., images), making direct imitation non-trivial.
- Joint training can close the performance gap: By modifying the teacher’s policy based on student alignment, the framework assumes that the student will achieve higher success rates than in traditional imitation learning.
- KL-divergence can serve as a reliable penalty metric: The divergence between teacher and student action distributions is assumed to accurately reflect imitation difficulty.
- A shared action decoder benefits both teacher and student: The student and teacher can benefit from learning in a common feature space, improving generalization.

#### Perspectives Missing from the Abstract

- Computational Efficiency Considerations:
    - The framework incorporates proxy student networks to reduce computational overhead, avoiding expensive simulation rollouts.
    - This aspect is crucial for real-world applications where training efficiency matters (e.g., robotics).
- Emergent Perception-Aware Behaviors:
    - Unlike standard RL, the method induces perception-aware behaviors.
    - For example, in quadrotor navigation, the teacher adjusts its orientation to help the student detect obstacles.
- Multi-Agent and Broader Implications:
    - Could be extended beyond teacher-student settings to multi-agent learning.
    - Might benefit areas like human-robot collaboration, where real-world asymmetries in perception occur.

#### Comparison to Related Work

- Builds on traditional imitation learning methods (e.g., Behavior Cloning, DAgger) but mitigates information asymmetry by actively modifying the teacher's behavior.
- Differs from privileged reinforcement learning (PRL), which assumes privileged information is only used during training and not distilled into the teacher-student interaction.
- Improves upon methods using dual optimization (e.g., COSIL, DWBC) by explicitly integrating student-awareness into the teacher's training.

#### Potentially Relevant Related Papers

- Nguyen et al. (2023): COSIL, a method incorporating KL-divergence-based penalties, but with fixed weighting schedules rather than dynamic teacher adaptation.
- Fu et al. (2022): DHBC, which aligns student and teacher feature spaces but does not modify teacher exploration behavior based on student capabilities.
- Shenfeld et al. (2023): TGRL, an RL-based approach for guiding teacher-student learning, but without a structured policy penalty to enforce alignment.
- Warrington et al. (2021): Work on multi-agent self-play, exploring how exposing teachers to student failures can improve knowledge transfer.

These papers might be useful if the reader is familiar with imitation learning prerequisites, particularly KL-regularized imitation learning and self-supervised representation learning.

This overview adds depth beyond the abstract by highlighting assumptions, perspectives, and a selective review of related work, making it a more comprehensive entry point for the reader.


You:
can you please create a detailed outline of the problem formulation, including any relevant equations, for the project mentioned in this paper?

ChatGPT:
### Detailed Outline of Problem Formulation for "Student-Informed Teacher Training"

![](2_concepts/media/Pasted%20image%2020250210114844.png)

## 1. Problem Definition

- Goal: Improve privileged imitation learning by training a teacher policy that explicitly considers the student's observational limitations, ensuring student imitation is feasible.
- Core challenge: The teacher policy has access to privileged information, while the student policy must operate with limited or high-dimensional observations (e.g., images).
- Key bottleneck:
    - Standard privileged imitation learning does not account for teacher-student asymmetry.
    - The student may not be able to infer the teacher’s actions accurately due to partial observability.

---

## 2. Markov Decision Process (MDP) Definition

- The environment is modeled as a Markov Decision Process (MDP) defined by:
$$
M = (S, A, P, R, \gamma, \mu_0)
$$
where:
- $S$ is the state space.
- $A$ is the action space.
- $P(s' | s, a)$ is the transition probability.
- $R(s, a)$ is the reward function.
- $\gamma$ is the discount factor.
- $\mu_0$ is the initial state distribution.

- Teacher Policy: $\pi_T(a | s)$ (uses privileged information).

- Student Policy: $\pi_S(a | s)$ (uses limited information).

- Proxy Student Policy: $\hat{\pi}_S(a | s)$ (approximates the student's actions for computational efficiency).

---

## 3. Performance Gap Between Teacher and Student

- In standard imitation learning, the difference in performance between teacher and student is upper-bounded by action divergence.
- Upper bound on performance gap:
$$
J(\pi_T) - J(\pi_S) \leq \frac{2 \sqrt{2} r_{\max} \sqrt{\epsilon}}{(1 - \gamma)^2}
$$
where:
- $J(\pi_T)$, $J(\pi_S)$ are the expected returns of the teacher and student.
- $r_{\max}$ is the maximum reward.
- $\epsilon$ is the upper bound on action divergence between teacher and student.
- Action divergence is defined as the KL-Divergence:
$$
\mathbb{E}{s \sim d{\pi_T}}
$$
$$
D_{\text{KL}}(\pi_T(\cdot | s) | \pi_S(\cdot | s)) ] \leq \epsilon
$$
where $d_{\pi_T}(s)$ is the discounted stationary state distribution.

---

## 4. Reformulated Teacher Objective with Student Awareness

- Instead of training the teacher independently, the proposed framework modifies the teacher's objective to encourage student imitation.

### Modified Teacher Objective

- Introduces a regularized teacher objective that balances:
    - Task reward $R(\tau)$
    - Alignment penalty based on action divergence:
$$
J_{\text{aligned}}(\pi_T) = \mathbb{E}{\tau \sim \pi_{\theta}} \left[ R(\tau) - D_{\theta}(\tau) \right]
$$
where:
- $R(\tau) = \sum_{t} \gamma^t r(s_t, a_t)$ is the discounted return.
- $D_{\theta}(\tau) = \sum_{t} \gamma^t D_{\text{KL}}(\pi_T(\cdot | s_t) \| \pi_S(\cdot | s_t))$ measures teacher-student action divergence.

---

## 5. Joint Training Framework

- Teacher and student are trained simultaneously with three alternating phases:
1. Rollout Phase: Teacher collects data, and a KL-divergence penalty is added to the reward:
$$
r' = r - \lambda_1 D_{\text{KL}}(\pi_T | \hat{\pi}_S)
$$

1. Policy Update Phase: Teacher updates parameters using PPO while incorporating:
- KL-Divergence gradient:
$$
\nabla_{\theta} J_{\text{aligned}}(\pi_T) = \mathbb{E}{\tau} \left[ \nabla_{\theta} (R(\tau) - D_{\theta}(\tau)) \right]
$$
1. Alignment Phase: Aligns proxy student and actual student by minimizing feature discrepancies:
$$
L_{\text{align}} = || h_T(s) - h_S(s) ||_1
$$

---

## 6. Proxy Student Network

- Since rendering student observations is computationally expensive, a proxy student network $\hat{\pi}_S$ is used.
- The proxy student is trained to predict student actions using only teacher observations:
$$
L_{\text{proxy}} = || h_S(s) - h_{\hat{S}}(s) ||_1
$$

---

## 7. Implementation Components

- Shared Action Decoder:
    - A shared feature space is introduced so that the student and teacher map to the same latent representations.
- KL-Divergence Regularization:
    - The teacher's policy gradient includes an additional KL-Divergence term:
$$
D_{\text{KL}}(\pi_T, \pi_S) = \frac{1}{2} \left[ (\mu_T - \mu_S)^T \Sigma_S^{-1} (\mu_T - \mu_S) \right]
$$
- Encourages teacher exploration in states that allow better student learning.

---

## 8. Summary of Training Algorithm
![](2_concepts/media/Pasted%20image%2020250210171001.png)
1. Initialize teacher, student, and proxy student networks.
2. Rollout Phase:
    - Teacher collects experiences.
    - Student observations are recorded for alignment.
    - Action divergence penalty added to teacher reward.
3. Policy Update Phase:
    - Teacher is updated via PPO including KL-regularized loss.
4. Alignment Phase:
    - Proxy student is trained to predict student actions.
    - Student encoder is aligned with teacher encoder.
5. Repeat until convergence.

---

### 9. Expected Benefits

- Reduces information asymmetry: Teacher learns imitable behaviors rather than optimal but unlearnable ones.
- Computationally efficient: Avoids excessive student rollouts using a proxy student.
- Leads to perception-aware behaviors: Encourages the teacher to provide information in a way the student can interpret (e.g., camera-aware navigation in quadrotors).

---

### 10. Experimental Validation

- Maze Navigation: Teacher avoids taking paths that students cannot perceive.
- Quadrotor Flight: Teacher aligns camera direction with flight path for better obstacle detection.
- Robotic Manipulation: Teacher adjusts grasping position to prevent occlusions.

---

### 11. Conclusion

- The framework bridges the gap between teacher and student policies by training the teacher to be more student-aware.
- Improves success rates across vision-based robotic tasks.
- Future work may extend this to multi-agent scenarios where agents must coordinate under asymmetric information constraints.

---

This detailed formulation captures all relevant equations, theoretical justifications, and implementation steps. Let me know if you need further expansion on any section! 🚀


You:
can you please create a detailed pipeline explaining the implementation of the project mentioned in this paper?
each stage in the pipeline should have descriptions of the inputs and outputs, including their shapes if they are tensors, use latex for math

ChatGPT:
### Pipeline for Implementing Student-Informed Teacher Training

The following pipeline provides a structured breakdown of the implementation workflow for the Student-Informed Teacher Training framework, detailing each stage with inputs, outputs, and tensor shapes.

---

## 1. Initialization Stage

### Purpose

- Initialize teacher, student, and proxy student networks.
- Define shared action decoder for consistent action space representation.
- Set up experience and alignment buffers for training.

### Inputs

6. Teacher policy network $\pi_T$
- Input: $s_T \in \mathbb{R}^{d_T}$ (teacher state with privileged information)
- Output: $a_T \in \mathbb{R}^{d_A}$ (action distribution)
- Shape:
$$
s_T \in \mathbb{R}^{d_T}, \quad a_T \in \mathbb{R}^{d_A}
$$

7. Student policy network $\pi_S$
- Input: $s_S \in \mathbb{R}^{d_S}$ (student state, limited observations)
- Output: $a_S \in \mathbb{R}^{d_A}$
- Shape:
$$
s_S \in \mathbb{R}^{d_S}, \quad a_S \in \mathbb{R}^{d_A}
$$

8. Proxy student network $\hat{\pi}_S$
- Input: $s_T$ (teacher observations)
- Output: Predicted student action $\hat{a}_S$
- Shape:
$$
s_T \in \mathbb{R}^{d_T}, \quad \hat{a}_S \in \mathbb{R}^{d_A}
$$

9. Shared action decoder
- Maps encoded representations to action space
- Common layer shared by teacher, student, and proxy student
- Input: Encoded latent state $h$
- Output: $a \in \mathbb{R}^{d_A}$

### Outputs

- Initialized networks and buffers:
- $\pi_T, \pi_S, \hat{\pi}_S,$ and shared decoder.
- Experience buffer $B_{\text{exp}}$.
- Alignment buffer $B_{\text{align}}$.

---

## 2. Rollout Phase

### Purpose

- Teacher interacts with the environment and collects state-action pairs.
- Proxy student estimates student actions from teacher states.
- Alignment buffer stores paired teacher-student states for alignment phase.

### Inputs

- Current state $s_T \in \mathbb{R}^{d_T}$.
- Teacher policy $\pi_T(a_T | s_T)$ generates actions.
- Proxy student estimates student’s actions: $\hat{a}_S = \hat{\pi}_S(s_T)$.
- Environment returns:
    - Next state $s_T'$.
    - Reward $r$.

### Process

10. Sample action from teacher policy:
$$
a_T \sim \pi_T(a | s_T)
$$
11. Predict student action using proxy student:
$$
\hat{a}_S = \hat{\pi}_S(s_T)
$$
12. Compute modified reward:
$$
r' = r - \lambda_1 D_{\text{KL}}(\pi_T | \hat{\pi}_S)
$$
13. Store experience in buffer:
$$
B_{\text{exp}} \leftarrow (s_T, a_T, r', s_T')
$$
14. Render student observation $s_S$ for a subset of transitions and store in alignment buffer:
$$
B_{\text{align}} \leftarrow (s_T, s_S)
$$

### Outputs

- Experience buffer $B_{\text{exp}}$ containing:
$$
{(s_T, a_T, r', s_T')}
$$
- Alignment buffer $B_{\text{align}}$ containing:
$$
{(s_T, s_S)}
$$

---

## 3. Policy Update Phase

### Purpose

- Optimize teacher policy using modified PPO loss with KL-divergence regularization.

### Inputs

- Experience buffer $B_{\text{exp}}$.
- PPO objective function:
$$
J_{\text{PPO}} = \mathbb{E}{\tau} \left[ R(\tau) - D{\text{KL}}(\pi_T | \hat{\pi}_S) \right]
$$
- Policy gradient update:
$$
\nabla_{\theta} J_{\text{PPO}}
$$

### Process

15. Sample batch $(s_T, a_T, r', s_T')$ from $B_{\text{exp}}$.
16. Compute policy loss:
$$
L_{\text{policy}} = - \mathbb{E} \left[ A \log \pi_T(a_T | s_T) \right]
$$
17. Compute KL divergence loss:
$$
L_{\text{KL}} = \mathbb{E}{s_T} \left[ D_{\text{KL}}(\pi_T(a | s_T) | \hat{\pi}_S(a | s_T)) \right]
$$
18. Update teacher policy using:
$$
\nabla_{\theta} (L_{\text{policy}} + \lambda_2 L_{\text{KL}})
$$

### Outputs

- Updated teacher network $\pi_T$.

---

## 4. Alignment Phase

### Purpose

- Align student encoder with teacher encoder using feature similarity loss.

### Inputs

- Alignment buffer $B_{\text{align}}$.
- Feature representations from student and teacher encoders:
- $h_T = f_T(s_T)$
- $h_S = f_S(s_S)$

### Process

19. Sample paired teacher and student observations $(s_T, s_S)$ from $B_{\text{align}}$.
20. Compute feature vectors:
$$
h_T = f_T(s_T), \quad h_S = f_S(s_S)
$$

21. Compute alignment loss:
$$
L_{\text{align}} = || h_T - h_S ||_1
$$

22. Back-propagate loss to update student encoder $f_S$.

### Outputs

- Updated student encoder $f_S$.
- Updated proxy student network $\hat{\pi}_S$.

---

## 5. Execution Loop

### Purpose

- Repeat rollout, policy update, and alignment phases until convergence.

### Pipeline Flow

23. Rollout Phase: Collect experience.
24. Policy Update Phase: Train teacher with KL-regularized PPO.
25. Alignment Phase: Train student and proxy student encoders.
26. Repeat until student performance stabilizes.

---

## Final Outputs

- Trained teacher policy $\pi_T$ with student-aware behavior.
- Trained student policy $\pi_S$ capable of imitating teacher actions.
- Proxy student model $\hat{\pi}_S$ for efficient training.
- Optimized shared action decoder improving feature alignment.

---

### Conclusion

This pipeline provides a structured implementation roadmap for the Student-Informed Teacher Training framework. Each phase efficiently handles data collection, policy optimization, and feature alignment, ensuring the student learns imitable behaviors without unnecessary exploration.
