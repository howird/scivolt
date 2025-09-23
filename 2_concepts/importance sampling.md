---
tags:
  - note
  - ece750
  - ai/rl
---
# Importance Sampling

> [!info] Background
> - Recall in [off policy](2_concepts/on%20off%20policy.md) methods, the objective is to learn the value of a target policy  using experiences gathered by following a different behavior policy 
>  - **Coverage Condition**: The behavior policy $b$ must provide sufficient coverage, meaning that if $\pi(a|s) > 0$, then $b(a|s) > 0$ should also hold true
>      - This ensures that the target policy $\pi$ is represented adequately in the behavior policy’s experiences.

#### Importance Sampling:
- **Motivation**: When off-policy learning is used, the experiences are generated from one policy but evaluated using another. Since the policies differ, we need to adjust the estimates accordingly
- **Idea**: Importance sampling is a method that allows us to estimate the target policy's value by weighting the returns using the ratio of the probabilities of the trajectories under the two policies, $\pi$ and $b$

- The **importance sampling ratio** is defined as:

$$
    \rho_{t:T-1} = \prod_{k=t}^{T-1} \frac{\pi(A_k|S_k)}{b(A_k|S_k)}
$$
- Where:
    - $A_k$ is the action taken at step $k$,
    - $S_k$ is the state at step $k$,
        - $\pi(A_k|S_k)$ and $b(A_k|S_k)$ represent the probabilities of action $A_k$ under the policies $\pi$ and $b$, respectively

- This ratio serves as a correction factor to account for the difference between the policies
- In essence, it reweights the returns so that experiences generated from $b$ can be used to estimate the value of $\pi$

#### Expectations of Importance Sampling:
- All importance sampling ratios have an expected value of 1 when the policies $b$ and $\pi$ are aligned. Mathematically, this is expressed as:

$$
\mathbb{E} \left[\frac{\pi(A_k|S_k)}{b(A_k|S_k)} \right] = 1
$$

#### Ordinary Importance Sampling:
For estimating the value function $V(s)$ at state $s$, ordinary importance sampling estimates it as:

$$
V(s) \approx \frac{1}{|\mathcal{T}(s)|} \sum_{t \in \mathcal{T}(s)} \rho_{t:T(t)-1} G_t
$$

Where:
- $\mathcal{T}(s)$ is the set of time steps where the state $s$ was encountered,
- $G_t$ is the return from time step $t$
- $\rho_{t:T(t)-1}$ is the importance sampling ratio

#### Weighted Importance Sampling:
In weighted importance sampling, the value function estimate is adjusted to balance out the variance introduced by the importance sampling ratios:

$$
V(s) \approx \frac{\sum_{t \in \mathcal{T}(s)} \rho_{t:T(t)-1} G_t}{\sum_{t \in \mathcal{T}(s)} \rho_{t:T(t)-1}}
$$

This adjustment ensures a more stable estimate by normalizing the contributions of each return.

#### Visual Representation of Time Steps:
As shown in the second image, time steps $t$ increase across episode boundaries, and the set $\mathcal{T}(s)$ represents the specific time steps where state $s$ is encountered in different episodes. These sets are used for calculating value estimates using importance sampling techniques.

In summary, importance sampling allows reinforcement learning algorithms to effectively utilize off-policy data, enabling the learning of one policy (target policy $\pi$) using data generated from another (behavior policy $b$) by applying probability ratio corrections.