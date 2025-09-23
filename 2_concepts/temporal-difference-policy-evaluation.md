---
tags:
  - note
  - ece750
  - ai/rl/td-method
  - ai/rl/model-free
  - ai/rl/off-policy
aliases:
  - TD Learning
status: doing
---

# Temporal Difference Learning (Policy Evaluation)

> [!info] Background
> - from [MC Policy Evaluation](2_concepts/monte-carlo-policy-evaluation.md), we have the algorithm:
>     - Initialization
>     - For each episode, $i$: $[(s_{i,1}, a_{i,1}, r_{i,1}), (s_{i,2}, a_{i,2}, r_{i,2}), \dots, (s_{i,T}, a_{i,T}, r_{i,T_i})]$.
>         - For each (state $s$ encountered for the first time in the episode __OR__ time step $t$)
>          - Update:
>             - let $G_{i,t} = r_t + \gamma r_{i, t+1} + \gamma^2 r_{i, t+2} + \dots + \gamma^{T_i-1} r_{i, T_i}$
>             - $N(s) = N(s) + 1$ (increment the counter for state $s$).
>             - $G(s) = G(s) + G_t$ (add the return to the total return for $s$).
>         - Value estimate: $V(s) = V(s) + \alpha(G_{i,t}-V(s))$ where $\alpha=1/N(s)$
> - However:
>     - can only be applied to episodic MDPs
>         - averaging over returns from a complete episode
>         - episode must end before its data can be used to update the value function
> - this is because it does not bootstrap

- TD learning is a [model free](2_concepts/model-free.md) method for **policy evaluation** that combines ideas from **Monte Carlo** methods and **dynamic programming**
- It updates value estimates incrementally, using the current reward and the value of the next state, without requiring complete episodes.

## Key Idea

- **[Bootstrapping](2_concepts/bootstrapping.md)**: Unlike Monte Carlo methods, which wait until the end of an episode to calculate the return, TD learning updates the value estimate $V(s)$ after each state transition

## TD(0) Learning Algorithm

- Algorithm:
    - Initialize: $V(s) = 0$ for all $s \in S$
    - Loop (until convergence):
        - sample $(s_t, a_t, r_t, s_{t+1})$
         - $V(s_t) \leftarrow V(s_t) + \alpha \overbrace{(\underbrace{r_t + \gamma V(s_{t+1})}_{\text{TD Target}} - V(s_t))}^{\delta_t \text{, TD Error}}$

- very similar to q-learning except we are fixing a policy here
- generally you sample in order

### Key Concepts:

1. **TD Target**, $r_t + \gamma V(s_{t+1})$
    - estimated return for the current state $s_t$ after observing the next state $s_{t+1}$. It combines the immediate reward $r_t$ and the discounted estimate of the value of the next state $V(s_{t+1})$
    - Normally, the TD target would be the expected value of $V(s_{t+1})$, however, we bootstrap by using the previous estimation
        - We don't have the transition model so we cannot easily calculate the previous estimation

2. **TD Error**: $\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$
    - The TD error measures the difference between the current value estimate $V(s_t)$ and the updated target
    - The error is used to adjust the value estimate
    - TD Error doesn't necessarily go to zero, since it is a sample, and not the expectation
        - it only goes to zero when the transition is deterministic

3. **Incremental Update**:
   - The value estimate $V(s_t)$ is updated after each transition, using the TD error and learning rate $\alpha$.
$$
V(s_t) \leftarrow V(s_t) + \alpha \delta_t
$$
   - The learning rate $\alpha$ determines how much to adjust the value based on the TD error

### Characteristics of TD Learning:

- **Model-Free**: TD learning does not require knowledge of the MDP’s dynamics (i.e., transition probabilities or reward function), only the immediate experience
- **Bootstrapping**: TD learning updates the value estimates based on other estimated values (i.e., using $V(s_{t+1})$), rather than waiting for a complete return as in Monte Carlo methods
- **On-Policy**: The value function is learned under the policy that is currently being followed (though there are off-policy TD methods like Q-learning)

### Advantages of TD Learning

- **Data Efficiency**: TD learning updates value estimates after every transition, making it more data-efficient than Monte Carlo methods, which require waiting until the end of an episode
- **Can be used in continuous tasks**: TD learning works well in tasks without terminal states, whereas Monte Carlo requires episodes to end
- **Low variance**: TD learning typically has lower variance than Monte Carlo because it updates more frequently and uses bootstrapped estimates
    - bootstrapping estimates makes it more 

### Disadvantages

- **Bias**: Since TD updates are based on current value estimates, there can be bias in early estimates, especially if the initialization of $V(s)$ is poor

## Comparison to MC

- Monte Carlo in batch settings converges to minimizing [MSE](2_concepts/mean-squared-error.md)
    - minimize loss wrt observed returns
- TD(0) converges to DP policy $V^\pi$ for the MDP with the maximum likelihood model estimates #TODO : explain based on lecture 3 stanford end
