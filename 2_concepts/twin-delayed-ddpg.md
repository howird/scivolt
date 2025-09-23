---
tags:
  - paper
  - "#ai/rl"
status: doing
year: 2018/10
authors: Scott Fujimoto, Herke van Hoof, David Meger
citekey: fujimotoAddressingFunctionApproximation2018
aliases:
  - TD3
  - Twin Delayed Deep Deterministic Policy Gradient
---
# TD3: Addressing Function Approximation Error in Actor-Critic Methods

### Key Contribution 1: Addressing Overestimation Bias

#### A. Double Q-Learning

- In [DQN](2_concepts/deep-q-networks.md), two sets of parameters are used for the Deep Q Network, giving a "Prediction Network" and a "Target Network" to avoid __maximization bias__
- The "Prediction" parameters were updated each batch as per standard practice, while the policy was evaluated using the "Target" parameters, which are a delayed copy of the "Prediction" parameters which is periodically synchronized
- This method was called Double DQN, not to be confused with [Double Q-learning](2_concepts/double-q-learning.md)
- Unfortunately, due to the slow-changing policy in an actor-critic setting, the current and target value estimates remain too similar to avoid maximization bias


#### B. Clipped Double Q-Learning

- While Double Q-Learning allows for a less biased value estimation, even an unbiased estimate with high variance can still lead to future overestimations in local regions of state space, which in turn can negatively affect the global policy
- Double Q-learning is more effective, it does not entirely eliminate the overestimation, to improve this __clipping__ was introduced
- In original [Double Q-learning](2_concepts/double-q-learning.md), the two Q functions are used to update each other in their TD error updates, here, we further avoid overestimation bias by taking the $\min$ between both estimates

$$
y_1 = r + \gamma \min_{i\in \{1, 2\}}Q_i(s', \pi_{\phi_1}(s'))
$$

- In implementation, computational costs can be reduced by using a single actor optimized with respect to $Q_{\theta_1}$, and use the same target $y_2 = y_1$ for $Q_{\theta_2}$
- If $Q_{\theta_2} \gt Q_{\theta_1}$
    - the update is identical to the standard update and induces no additional bias
- else:
    - overestimation has occurred and the value is reduced by clipping

### Key Contribution 2: Addressing Variance

#### A. Delayed
