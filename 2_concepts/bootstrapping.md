---
tags:
  - note
  - math/stats
status: todo
---
# Bootstrapping

## Bootstrapping in Statistics

- **Concept**: Bootstrapping in statistics is a **resampling technique** where you repeatedly sample **with replacement** from an observed dataset to create multiple "new" datasets
    - These resampled datasets are used to estimate properties like the mean, variance, or confidence intervals of a statistic
- **Why it's useful**: It helps approximate the sampling distribution of a statistic when the true distribution is unknown, especially when the dataset is small.
- **Key property**: It does not rely on assumptions about the underlying population distribution

## Bootstrapping in Reinforcement Learning
- **Concept**: In RL, bootstrapping refers to the idea that an estimate of the value function is updated using another estimate of the value function
    - That is, instead of waiting until the actual return (cumulative reward) is observed, we use the current estimates to update future estimates
- **Why it's useful**: It enables **efficient learning** by leveraging prior knowledge, reducing the need for full rollouts of an episode before updating the value function.
- **Key property**: It relies on the assumption that previous estimates are reasonably accurate, even though they might be biased or incomplete

- in RL, bootstrapping is linked to [dynamic programming](2_concepts/dynamic%20programming%20rl.md)
- In [Temporal Difference (TD) Learning](2_concepts/temporal%20difference%20policy%20evaluation.md), for example, the value of a state $V(s)$ is updated using the value of the next state $V(s')$, rather than waiting for the actual return:

$$
V(s) \leftarrow V(s) + \alpha (r + \gamma V(s') - V(s))
$$

- This is an example of bootstrapping because we're using an **existing estimate** ($V(s')$) rather than actual future rewards.

- in RL, bootstrapping is less about resampling (as in statistics) and more about **estimating values using other estimates**
- While statistical bootstrapping is used for **uncertainty estimation**, RL bootstrapping is used for **efficient learning** via the Bellman equation
