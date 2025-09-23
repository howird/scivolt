---
tags:
  - note
  - ai/rl
  - ece750
status: doing
---
# Dynamic Programming in Reinforcement Learning

- The main methods for dynamic programming in RL are [policy and value iteration](2_concepts/policy%20value%20iteration.md)
- These methods are useful only in **model-based, tabular settings** with perfect knowledge of the environment
    - **they assume full knowledge of the environment's dynamics**, i.e., the transition probabilities $P(s'|s,a)$ and rewards $R(s,a)$
- These methods use initial estimates of a Value function and improve these estimates using [bootstrapping](2_concepts/bootstrapping.md)
- Like most other value based methods, these algorithms rely on the Markovian property

- Temporal Difference learning sits in between **Monte Carlo (no bootstrapping)** and **DP (full bootstrapping with known model)**.
- TD methods **use bootstrapping like DP**, but **without requiring a model of the environment**, so they can be used in **model-free** settings.
