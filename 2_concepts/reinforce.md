---
tags:
  - note
  - ai/rl
  - ai/dl
aliases:
  - REINFORCE
status: doing
---
# REINFORCE Algorithm

- The REINFORCE algorithm with baseline is a [monte carlo](2_concepts/monte-carlo-policy-evaluation.md) [policy gradient](2_concepts/policy-gradient.md) method used for optimizing policies directly in **on-policy** and **model-free** environments

- The incorporation of a baseline significantly reduces the variance in gradient estimates, resulting in more stable learning.


##  REINFORCE Algorithm

> [!info] Background
> - **Policy Gradient methods** are a class of algorithms in Reinforcement Learning (RL) used to optimize policies directly.
>  - The **policy gradient theorem** gives the gradient of the objective:
> $$
> \nabla_\theta J(\theta) \propto \sum_s \mu(s) \sum_a q_\pi(s, a) \nabla_\theta \pi(a | s, \theta)
> $$
> - where $q_\pi(s, a)$ is the action-value function, and $\mu(s)$ is the on-policy state distribution


- The **REINFORCE** algorithm is a **Monte Carlo** policy gradient method. It uses **full returns** from episodes to compute the gradient.

- The **policy parameter update** without a baseline is:
$$
\theta_{t+1} \approx \theta_t + \alpha G_t \frac{\nabla_\theta \pi(A_t | S_t, \theta_t)}{\pi(A_t | S_t, \theta_t)}
$$
where $G_t$ is the return from the current episode, $\alpha$ is the learning rate, and $S_t, A_t$ are the state and action at time $t$.

#### 3. **REINFORCE with Baseline**
To reduce the high variance in the REINFORCE algorithm, a **baseline** function $b(s)$, typically the **value function** $v_\pi(s)$, can be subtracted from the action-value function $q_\pi(s, a)$. This subtraction centers the gradient updates around the advantage function $A_\pi(s, a) = q_\pi(s, a) - v_\pi(s)$, making updates more stable.

- The **policy gradient with baseline** becomes:
$$
\nabla_\theta J(\theta) \propto \sum_s \mu(s) \sum_a \left( q_\pi(s, a) - b(s) \right) \nabla_\theta \pi(a | s, \theta)
$$
- Subtracting $b(s)$ reduces variance without introducing bias because:
$$
\sum_a b(s) \nabla_\theta \pi(a | s, \theta) = 0
$$
- The **update rule** with baseline:
$$
\theta_{t+1} \approx \theta_t + \alpha \left( G_t - b(S_t) \right) \frac{\nabla_\theta \pi(A_t | S_t, \theta_t)}{\pi(A_t | S_t, \theta_t)}
$$
Here, $b(S_t)$ can be any state-dependent baseline, commonly chosen as the **state value estimate** $\hat{v}(S_t, \mathbf{w})$.

### REINFORCE Algorithm

The steps for **REINFORCE with Baseline** are:

1. **Initialize** policy parameters $\theta$.
2. **For each episode**:
    - Generate an episode: $S_0, A_0, R_1, S_1, \dots, S_T$ by following the policy $\pi(a|s, \theta)$.
    - For each time step $t$ in the episode:
        - Compute the return $G_t$.
        - Update the policy parameters:
$$
\theta_{t+1} \leftarrow \theta_t + \alpha (G_t - b(S_t)) \frac{\nabla_\theta \pi(A_t | S_t, \theta)}{\pi(A_t | S_t, \theta)}
$$
1. **Repeat** until convergence.

### Relationship to Monte Carlo and Temporal-Difference (TD) Learning

- **Monte Carlo (MC) Methods**: 
- REINFORCE is a Monte Carlo method because it relies on the **full returns** from complete episodes to compute updates. This means it requires episodes to finish before updating the policy.
- MC methods have **high variance** due to the reliance on full episodic returns but are **unbiased**.

- **Temporal-Difference (TD) Learning**: 
- TD methods, such as **Actor-Critic**, address the high variance of Monte Carlo methods by updating the policy using **bootstrapped estimates** of the return (e.g., using $V(s)$ or $Q(s, a)$).
- In TD methods, an **actor** (policy) and a **critic** (value function) work together. The critic estimates the value function to update the actor's policy. TD learning can work online and doesn’t need full episodes, making it **lower variance** but **biased**.

- **Advantage Function**: 
- In REINFORCE with a baseline, the term $G_t - b(S_t)$ resembles the **advantage** $A_\pi(S_t, A_t) = Q_\pi(S_t, A_t) - V_\pi(S_t)$. This similarity reduces variance by grounding updates around the baseline, analogous to how **advantage actor-critic** methods work in TD learning.

### Properties of REINFORCE with Baseline

1. **On-Policy**: 
- REINFORCE is an **on-policy** algorithm, meaning it learns and improves the policy that it is currently using to interact with the environment. The updates are based on returns collected by following the current policy $\pi_\theta$

2. **Model-Free**:
- It is a **model-free** method, as it doesn't require any model of the environment (i.e., it doesn't need to know the transition probabilities or the reward function in advance).

3. **Variance and Bias**: 
- **High variance**, especially without a baseline, because it uses the full return from episodes. However, introducing a baseline reduces this variance.
- The algorithm is **unbiased**, as it relies on the true returns from sampled trajectories.

# REINFORCE Algorithm

- The REINFORCE algorithm with baseline is a [monte carlo](2_concepts/monte-carlo-policy-evaluation.md) [policy gradient](2_concepts/policy-gradient.md) method used for optimizing policies directly in **on-policy** and **model-free** environments

##  Description

> [!info] Background
> - **Policy Gradient methods** are a class of algorithms in Reinforcement Learning (RL) used to optimize policies directly.
>  - The **policy gradient theorem** gives the gradient of the objective:
> $$
> \nabla_\theta J(\theta) \propto \sum_s \mu(s) \sum_a q_\pi(s, a) \nabla_\theta \pi(a | s, \theta)
> $$
> - where $q_\pi(s, a)$ is the action-value function, and $\mu(s)$ is the on-policy state distribution

- **REINFORCE** (Monte-Carlo policy gradient) relies on an estimated return by Monte-Carlo methods using episode samples to update the policy parameter $\theta$
- REINFORCE works because the expectation of the sample gradient is equal to the actual gradient:

$$
\begin{aligned}
\nabla_\theta J(\theta)
&= \mathbb{E}_\pi [Q^\pi(s, a) \nabla_\theta \ln \pi_\theta(a \vert s)] & \\
&= \mathbb{E}_\pi [G_t \nabla_\theta \ln \pi_\theta(A_t \vert S_t)] & \scriptstyle{\text{; Because } Q^\pi(S_t, A_t) = \mathbb{E}_\pi[G_t \vert S_t, A_t]}
\end{aligned}
$$

- Therefore we are able to measure $G_t$ from real sample trajectories and use that to update our policy gradient
- It relies on a full trajectory and that’s why it is a Monte-Carlo method

1. Initialize the policy parameter θ at random.
2. Generate one trajectory on policy $S_1, A_1, R_2, S_2, A_2, \dots, S_T$
3. For t=1, 2, … , T:
    1. Estimate the the return $G_t$
    2. Update policy parameters: $\theta \leftarrow \theta + \alpha \gamma^t G_t \nabla_\theta \ln \pi_\theta(A_t \vert S_t)$

- A widely used variation of REINFORCE is to subtract a baseline value from the return $G_t$ to _reduce the variance of gradient estimation while keeping the bias unchanged_ (Remember we always want to do this when possible)
- For example, a common baseline is to subtract state-value from action-value, and if applied, we would use [Advantage](2_concepts/advantage-function.md) $A(s, a) = Q(s, a) - V(s)$ in the gradient ascent update

## Properties

- **On-Policy**: it learns and improves the policy that it is currently using to interact with the environment. The updates are based on returns collected by following the current policy $\pi_\theta$.
-  **Model-Free**: no $P$ required
- Like MC methods:
    - **High variance**: because it uses the full return from episodes
        - introducing a baseline reduces this variance
    - **unbiased**: as it relies on the true returns from sampled trajectories.
