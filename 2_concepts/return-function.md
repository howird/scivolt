---
tags:
  - note
  - ai/rl
  - ece750
status: review
---
> [!info] Background
> - In [RL](REINFORCEMENT-LEARNING.md), our goal is to take actions which maximize our rewards, given a [Markov decision process](markov-decision-process.md)
> - To do so, we must be able to predict our future rewards

# Return Function

- The return is defined as some specific function of the reward sequence, in the simplest case the sum of all future rewards up until termination ($H$):

$$
G_t = sum_(k=1)^H R_(t+k)
$$

- We can further generalize the return to __discount rewards__ found farther in the future with a discount factor, $\gamma$
    - note: when $\gamma=1$, we get the previous equation
- Additionally we show that $G_t = R_{t+1} + \gamma G_{t+1}$:

$$
\begin{aligned}
G_t &= \sum_{k=0}^H \gamma^k R_{t+k+1} \\
&= \gamma^0 R_{t+1} + \sum_{k=0}^H \gamma^{(k+1)} R_{t+k+2} \\
&= \gamma^0 R_{t+1} + \gamma \bigg(\sum_{k=0}^H \gamma^{k} R_{(t+1)+k+1}\bigg) \\
&= R_{t+1} + \gamma G_{t+1} \\
\end{aligned}
$$

- This is true for all time steps $t < T$ even if termination occurs at the next time step, if we define $G_H = 0$,  $\because G_{H-1} = R_H + 0$

> [!note]
> - The return, $G$, is not especially useful because it is not a probabilistic expectation, it is the determined sum of future rewards
> - we cannot know the sum of future rewards without taking the actions, therefore we must know the future in order to determine it
>     - the types of algorithms that use it are often called [monte carlo policy evaluation](2_concepts/monte-carlo-policy-evaluation.md)
> - Instead, we often use an estimate of the __expected__ future rewards __starting a specific state__ and following a __specific policy__ aka the [value function](2_concepts/value-functions.md)
