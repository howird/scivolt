---
tags:
  - note
  - ece750
  - ai/rl
status: done
---
# Epsilon-Greedy Policies in Reinforcement Learning

## Epsilon-Greedy Policy

- The $\epsilon$-greedy policy balances exploration (trying new actions) and exploitation (choosing the best-known actions)

- Exploration occurs with probability $\epsilon$: where the agent chooses a random action
- Exploitation occurs with probability $1 - \epsilon$, where the agent chooses the action that maximizes the current estimated value

### Definition
$$
\pi(a|s) =
\begin{cases}
1 - \epsilon + \frac{\epsilon}{|A(s)|}, & \text{if } a = \arg\max_{a'} Q(s, a') \\
\frac{\epsilon}{|A(s)|}, & \text{otherwise}
\end{cases}
$$
- Where:
    - $\pi(a|s)$ is the probability of taking action $a$ in state $s$
    - $Q(s, a')$ is the estimated value of action $a'$ in state $s$
    - $|A(s)|$ is the number of available actions in state $s$
    - $\epsilon$ is a small probability (e.g., 0.1) controlling the exploration

## Greedy Policy

- a greedy policy always selects the action with the highest estimated value. It is deterministic

### Definition
  $$
  \pi(a|s) =
  \begin{cases}
  1, & \text{if } a = \arg\max_{a'} Q(s, a') \\
  0, & \text{otherwise}
  \end{cases}
  $$
- This policy does not explore and can get stuck in local optima because it never tries suboptimal actions that could lead to better long-term rewards.


## Epsilon-Soft-Greedy Policy

- The $\epsilon$-soft greedy policy is a variation on $\epsilon$-greedy where non-greedy actions are selected with a small probability, but in a more **probabilistically informed** manner
- Rather than selecting any non-greedy action with uniform probability, the agent __selects non-greedy actions based on their value estimates__
- Thus, even during exploration, better actions are still more likely to be chosen

### Definition
$$
\pi(a|s) =
\begin{cases}
1 - \epsilon, & \text{if } a = \arg\max_{a'} Q(s, a') \\
\epsilon \cdot f(Q(s, a)), & \text{otherwise}
\end{cases}
$$
- Where: $f(Q(s, a))$ is a function that assigns probabilities to actions based on their value estimates
    - Often, this is done using [softmax](2_concepts/softmax.md) or another distribution, so better actions get slightly higher probabilities than worse actions.
