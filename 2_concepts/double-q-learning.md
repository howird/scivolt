---
tags:
  - note
  - ai/rl/model-based
  - ece750
status: todo
aliases:
  - Double Q-Learning
  - Overestimation Bias
---
# Double Q-Learning

- A variant of [Q-Learning](2_concepts/q-learning.md) designed to mitigate the overestimation bias in Q-learning by decoupling action selection from action evaluation.
- Instead of using one Q-value function, Double Q-Learning trains two independent Q-value functions, $Q_1$ and $Q_2$.

## Algorithm

- Initialize two action-value functions $Q_1(s, a)$ and $Q_2(s, a)$ arbitrarily, except for terminal states where $Q_1(terminal, \cdot) = Q_2(terminal, \cdot) = 0$.
- **For each episode**:
    - Initialize the starting state $S_t$
    - For each step within the episode:
        - Choose action $A_t$ based on $Q(s, a) = Q_1(s, a) + Q_2(s, a)$
            - Take action $A_t$, observe reward $R_{t+1}$, and transition to the next state $S_{t+1}$
        - Update either $Q_1$ or $Q_2$ with equal probability
            - If updating $Q_1$, use $Q_2$ for the next state's value $Q_1(S_t, A_t) \leftarrow (1 - \alpha)Q_1(S_t, A_t) + \alpha (R_{t+1} + \gamma Q_2(S_{t+1}, \arg \max_a Q_1(S_{t+1}, a))$
            - If updating $Q_2$, use $Q_1$ for the next state's value: $Q_2(S_t, A_t) \leftarrow (1-\alpha)Q_2(S_t, A_t) + \alpha (R_{t+1} + \gamma Q_1(S_{t+1}, \arg \max_a Q_2(S_{t+1}, a)))$
        - Update the state $S \leftarrow S'$

## Overestimation Bias

![](2_concepts/media/Pasted%20image%2020250520184931.png)