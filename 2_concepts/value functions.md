---
date: August 27, 2024
status: doing
tags:
  - note
  - ai/rl/model-based
  - ece750
aliases:
  - value function
  - state value function
  - quality function
  - state-action value function
---
# Value Function

> [!background]
> - Recall  the [return function](2_concepts/return%20function.md), $G$, is not especially meaningful or tangible - it is more of a theoretical formulation - we cannot know the sum of future rewards without taking the actions $\implies$ thus we would need to know the future to calculate it
> - Instead, we can only calculate a probabilistic estimate (__expected__, $E[\cdot]$) future rewards __starting a specific state__ and following a __specific policy__
>

- A value function $V(s)$ is the expected sum of discounted rewards when starting from state $s$ and acting under a policy $\pi$

$$
V(s) = \mathbb{E}\big[ \sum_{t=0}^H \gamma^t R_{t+1}(S_t, A_t, S_{t+1}) | \pi,s_0=s \big]
$$

- An __optimal__ value function $V^*(s)$ is the expected sum of discounted rewards when starting from state $s$ and acting under an __optimal__ policy $\pi$
    - the optimal policy is defined as the policy which maximizes the value function
$$
\begin{aligned}
V^*(s) &= \max_\pi V(s) \\
&= \max_\pi\mathbb{E}\big[ \sum_{t=0}^H \gamma^t R_{t+1}(S_t, A_t, S_{t+1}) | \pi, s_0=s \big] \\
\pi^*(s) &= \arg\max_\pi V(s)\\
&= \arg\max_\pi\mathbb{E}\big[ \sum_{t=0}^H \gamma^t R_{t+1}(S_t, A_t, S_{t+1}) | \pi, s_0=s \big] \\
\end{aligned}
$$

- given this mathematical formulation, we must determine $V(s)$ using either the [value iteration or policy iteration](2_concepts/policy%20value%20iteration.md) algorithms (in the tabular setting)

### Types of Value Functions

1. **State-Value Function $V^\pi(s)$**:
   - The expected return (cumulative discounted reward) starting from state $s$ and following policy $\pi$.
   - It is defined as:
$$
V^\pi(s) = E^\pi \left[ G_t | s_t = s \right] = E^\pi \left[ r_t + \gamma r_{t+1} + \gamma^2 r_{t+2} + \cdots | s_t = s \right]
$$
   
2. **State-Action Value Function $Q^\pi(s, a)$**:
   - The expected return from taking action $a$ in state $s$ and then following policy $\pi$
   - Defined as:
$$
     Q^\pi(s, a) = E^\pi \left[ r_t + \gamma V^\pi(s_{t+1}) | s_t = s, a_t = a \right]
$$

