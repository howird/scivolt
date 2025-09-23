---
date: August 27, 2024
status: done
tags:
  - ai/rl
  - note
aliases:
  - MDP
---
# Markov Decision Process

- A __Markov Decision Process (MDP)__ extends a [Markov Reward Process](2_concepts/markov%20reward%20process.md), with actions that influence the state transition
    - A state transition in an MDP is now conditioned on an action
    - In the case of a discrete MDP, the transition matrix adds a dimension for actions

- Markov Decision Process: $MDP(S, A, P, R, \gamma[, H])$:
    - Set of states $S$
        - the state at each time step is $s_t \in S$
        - the start state, $s_0$, is distributed over $s_0 \sim \rho_0(\cdot)$
        - Set of actions $A$
    - Dynamics/Transition function $P(s'|s, a)$
        - Sometimes $\cal T$ (for transition) is used instead of $P$
    - Reward function $R(s, a, s')$
    - Discount factor $\gamma \in [0,1]$
        - Optional: Horizon $H$, sometimes known as $T$

> [!question] Points of Confusion
>
> 1. Alignment of the state actions and rewards at each time step:
>
>       - $S_t$ is the state at the __current time step__
>       - $R_t$ is the reward we received when we transition__ed__, from the previous state to the current state ($S_{t-1}\rightarrow S_t$) via the previous action $A_{t-1}$
>         - BUT: it is better to think of it as the reward received for simply being in the new state
>       - $A_t$ is the action we __will__ take to transition from $S_t\rightarrow S_{t+1}$
>    
>     - Thus, the function above can be clarified by changing $R \rightarrow R_{t+1}$
>    
>       - note: $R_t$ does not exist in the equation since, it doesn't matter anymore
>
> 2. Why is $S_{t+1}$ an __input__ to the reward function $R$ (not just $S_t$ and $A_t$)?
>       - sometimes $S_{t+1}$ is just omitted from the equation
>      - Since the transition function is probabilistic, we cannot know what the next state will be with just $S_t$ and $A_t$, and the reward received at the next step $R_{t+1}$ cannot be known with out the next state $S_{t+1}$
>

### Policy:
A **policy** $\pi(s)$ is a strategy that specifies what action the agent should take in each state. It can be:
- **Deterministic**: $\pi(s) = a$, always takes the same action $a$ in state $s$.
- **Stochastic**: $\pi(a|s) = P(a|s)$, provides a probability distribution over actions for each state.

### Transition Matrix for Action $a_1$:

$$
P_{a_1} = \begin{pmatrix}
P(s_1 | s_1, a_1) & P(s_2 | s_1, a_1) & \dots & P(s_n | s_1, a_1) \\
P(s_1 | s_2, a_1) & P(s_2 | s_2, a_1) & \dots & P(s_n | s_2, a_1) \\
\vdots & \vdots & \ddots & \vdots \\
P(s_1 | s_n, a_1) & P(s_2 | s_n, a_1) & \dots & P(s_n | s_n, a_1)
\end{pmatrix}
$$

### Transition Matrix for Action $a_2$:

$$
P_{a_2} = \begin{pmatrix}
P(s_1 | s_1, a_2) & P(s_2 | s_1, a_2) & \dots & P(s_n | s_1, a_2) \\
P(s_1 | s_2, a_2) & P(s_2 | s_2, a_2) & \dots & P(s_n | s_2, a_2) \\
\vdots & \vdots & \ddots & \vdots \\
P(s_1 | s_n, a_2) & P(s_2 | s_n, a_2) & \dots & P(s_n | s_n, a_2)
\end{pmatrix}
$$

### Reward Vector for Action $a_1$:

$$
R_{a_1} = \begin{pmatrix}
R(s_1, a_1) \\
R(s_2, a_1) \\
\vdots \\
R(s_n, a_1)
\end{pmatrix}
$$

### Reward Vector for Action $a_2$:

$$
R_{a_2} = \begin{pmatrix}
R(s_1, a_2) \\
R(s_2, a_2) \\
\vdots \\
R(s_n, a_2)
\end{pmatrix}
$$


