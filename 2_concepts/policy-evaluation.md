---
tags:
  - note
  - ai/rl
  - ece750
status: todo
---
# Policy

- A policy, $\pi(a | s)$, is a conditional probability of taking action $a$, given $s$:
$$
\pi(a | s) = P(a_t = a | s_t = s)
$$
- When the policy, $\pi$, is deterministic it can be represented simply as $\pi(s)$

## MDPs as MRPs
>[!info]

- A [Markov Decision Process](2_concepts/markov-decision-process.md): $MDP(S, A, P, R, \gamma)$, can actually be re-framed as a [Markov Reward Process](2_concepts/markov-reward-process.md): $MRP(S, P, R, \gamma)$, by defining 
- By $MDP(S, A, P, R, \gamma) \rightarrow MRP(S, P^\pi, R^\pi, \gamma)$ where:

$$
\displaylines{
R^\pi(s, a) = \sum_{a \in A} \pi(a | s) R(s, a) \\
P^\pi(s' | s) = \sum_{a \in A} \pi(a | s) P(s' | s, a) \\
}
$$

- meaning we can use the same methods for 

## Policy Evaluation

