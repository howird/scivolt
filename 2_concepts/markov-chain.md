---
tags:
  - note
  - ai/rl
  - math/prob/markov-chains
  - ece750
status: done
---

# Markov Chain

- A __Markov chain__ is a mathematical model used to describe a system that transitions from one state to another within a set of possible states, $S$

- __Markov Property__: the probability of transitioning to any future state depends only on the current state and not on the sequence of events that preceded it

- it is parameterized by the Transition/Dynamics model, $P$ or $\cal T$, a matrix of transition probabilities, where each entry in the matrix represents the probability of moving from one state to another

- **Transition matrix** $P$:
    - row $i$: $S_i \rightarrow S_n \in \mathbf{S}$
    - column $j$: $S_n \in \mathbf{S} \rightarrow S_j$

$$
P = \begin{pmatrix}
P(s_1 | s_1) & P(s_2 | s_1) & \dots & P(s_n | s_1) \\
P(s_1 | s_2) & P(s_2 | s_2) & \dots & P(s_n | s_2) \\
\vdots & \vdots & \ddots & \vdots \\
P(s_1 | s_n) & P(s_2 | s_n) & \dots & P(s_n | s_n)
\end{pmatrix}
$$
