---
tags:
  - note
  - ece750
  - ai/rl
  - ai/dl
aliases:
  - Policy Gradient
status: doing
---
# Policy Gradient

- __GOAL__: find the parameters ($\theta$) of the policy function $\pi(a|s, \theta) = \pi_\theta$ that maximize the expected returns following the policy ($V^{\pi_\theta}$)

- This is an optimization problem thus, we need an **Objective Function**:
    - to maximize the expected reward $J(\theta)$, where $J(\theta) \approx v_{\pi_\theta}(s_0)$, which corresponds to the value of the policy starting from the initial state $s_0$

- We optimize the $J$ using stochastic gradient ascent:
$$
\Delta \theta \approx \alpha \nabla_\theta V(\theta)
$$

- Here, $\alpha$ is the learning rate and $\nabla J(\theta_t)$ is the gradient of the objective function with respect to the policy parameters

- **Policy Gradient Theorem**
- The gradient of the objective $\nabla J(\theta)$ is proportional to the sum over all states $s$ and actions $a$, weighted by the on-policy distribution $\mu(s)$ and the action-value function $q_\pi(s, a)$:
$$
\nabla J(\theta) \propto \sum_s \mu(s) \sum_a q_\pi(s, a) \nabla_\theta \pi(a|s, \theta)
$$
- where: $\mu(s)$ is the stationary distribution of states under policy $\pi$



### Properties

- We can use Policy Gradient __whenever__ we can calculate how small changes in some parameters influence the probability of taking different actions in a given state
- We do not need access to an estimate of the dynamics


## Algorithms

- 