---
tags:
  - note
  - ai/rl
  - ece750
aliases:
  - on policy
  - off policy
status: todo
---
# On and Off Policy Learning

## On Policy Learning

- Direct experience
- Learn to estimate and evaluate a policy from experience obtained acting under that policy

## Off Policy Learning

- **Objective**: Learn the value of a target policy $\pi$ using experiences gathered by following a different behavior policy $b$
- **Example**: 
    - The target policy $\pi$ is typically the greedy or optimal policy we want to learn
    - The behavior policy $b$ is more exploratory, such as an $\epsilon$-greedy policy, which encourages exploration of state-action spaces
