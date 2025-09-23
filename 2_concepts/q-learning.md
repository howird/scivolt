---
tags:
  - note
  - ai/rl/model-based
  - ece750
status: todo
aliases:
  - Q learning
  - Double Q learning
---
# Q Learning

- An off-policy [control](2_concepts/control-policy-evaluation.md) algorithm based on [TD policy evaluation](2_concepts/temporal-difference-policy-evaluation.md)
- Unlike [SARSA](2_concepts/SARSA.md), Q-learning's off-policy nature
- Q-learning updates the action-value function $Q(s, a)$ using the **maximum** future value, regardless of the action taken by the current policy
- This allows the algorithm to converge faster towards the **optimal policy**
    
## Algorithm

- Initialize the action-value function $Q(s, a)$ for all state-action pairs arbitrarily, except for terminal states where $Q(terminal-state, \cdot) = 0$
- For each episode:
    - Initialize the starting state $S$
    - For each step within the episode:
        - choose an action $A$ based on the current policy derived from $Q(s, a)$
        - take action $A$, observe the reward $R$ and the next state $S'$
        - Choose the next action $A'$ from the new state $S'$ using the policy
        - $Q(S, A) \leftarrow Q(S, A) + \alpha \left( R + \gamma \max_a Q(S', a) - Q(S, A) \right)$
        - Update the state $S \leftarrow S'$

## Double Q-Learning

- A variant of Q-learning designed to mitigate the overestimation bias in Q-learning by decoupling action selection from action evaluation.
- Instead of using one Q-value function, Double Q-Learning trains two independent Q-value functions, $Q_1$ and $Q_2$.

### Algorithm

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
