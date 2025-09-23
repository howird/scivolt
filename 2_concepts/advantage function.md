---
tags:
  - note
  - ai/rl
  - ece750
status: review
aliases:
  - Advantage
  - Advantage Function
---
# Advantage Function

#todo : https://danieltakeshi.github.io/2017/03/28/going-deeper-into-reinforcement-learning-fundamentals-of-policy-gradients/

- The **advantage function** quantifies how much better or worse a specific action $a$ is compared to the average action taken in a given state $s$

- It helps in deciding which action to take or improves the estimate of the expected outcome for actions

- defined as the difference between the [state-action value function](2_concepts/value%20functions.md) $Q_\pi(s, a)$ and the [state value function](2_concepts/value%20functions.md) $V_\pi(s)$:
$$
A_\pi(s, a) = Q_\pi(s, a) - V_\pi(s)
$$
- By comparing these, the advantage function tells us whether a __particular__ action is better or worse than the __typical__ action in that state

- [TD Learning](2_concepts/temporal%20difference%20policy%20evaluation.md) concepts such as TD Target and TD Error ($\delta_t$) are related to how well we estimate future rewards

$$
\delta_t = \underbrace{R_t + \gamma E_{a \sim \pi} Q(s_{t+1}, a)}_{\text{TD Target}} - Q(s_t, a) \approx A_\pi(S_t, A_t)
$$

This error gives feedback on how much the action's expected value differs from the observed reward, refining the agent's policy.