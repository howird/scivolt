---
tags:
  - note
  - ai/rl/policy-eval
  - ai/rl/control
aliases:
  - policy evaluation
  - control
status: todo
---
# Control vs Policy Evaluation in RL

- **Policy Evaluation** and **Control** are two distinct **tasks** in reinforcement learning, and many algorithms integrate both of them
- Policy evaluation can be viewed as a sub-task of control, where the value of the current policy is estimated in order to improve it iteratively toward an optimal policy

## Policy Evaluation
- **TASK**: estimate the [value function](2_concepts/value%20functions.md) $V^pi (s)$ or $Q^pi (s, a)$ for a given policy $\pi$
    - i.e. "How good is it to follow this policy $\pi$ from a given state or state-action pair?"
  
- **Goal**: To determine the expected cumulative reward when the agent follows a specific policy
- Examples:
    - [Temporal Difference](2_concepts/temporal%20difference%20policy%20evaluation.md) methods like **TD(0)**
    - [Monte Carlo](2_concepts/monte%20carlo%20policy%20evaluation.md) methods
    - Dynamic Programming methods for policy evaluation (Bellman expectation equation)

## Control
- **TASK**: **improve** the policy, aiming to find the **optimal policy** that maximizes long-term rewards
    - evaluates the current policy
    - ALSO updates it iteratively to become more optimal
  
- **Goal**: To find the best policy $\pi^*$ that maximizes the expected reward.
- Examples that combine policy evaluation and policy improvement. In these control algorithms, the value function is updated, and the policy is improved simultaneously:
    - [q learning](2_concepts/q%20learning.md)
    - [SARSA](2_concepts/SARSA.md)

### Relationship Between Policy Evaluation and Control:
In many reinforcement learning algorithms, **policy evaluation** and **control** are combined into a single process. Control algorithms often include both evaluation and improvement steps:

- **Policy Iteration**: This is a classic algorithm that explicitly separates policy evaluation and control (policy improvement). It alternates between:
  1. **Policy evaluation**: Evaluates the current policy.
  2. **Policy improvement**: Updates the policy to improve it based on the current value estimates.
  
  These steps are repeated until convergence to the optimal policy.

- **Value Iteration**: This is a control algorithm that effectively combines policy evaluation and policy improvement in each step. It updates the value function using the Bellman optimality equation without explicitly evaluating a policy. The process inherently improves the policy as the value function is updated.

- **SARSA and Q-learning**: These TD-based control methods integrate both tasks. They evaluate the current policy by updating the value function and implicitly improve the policy through exploration-exploitation strategies.
