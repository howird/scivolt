---
tags:
  - note
  - ece750
  - ai/rl
  - ai/dl
aliases:
  - Policy Approximation
status: doing
---
# Policy Approximation

- In reinforcement learning, **policy approximation** addresses the challenge of representing policies in environments with large or continuous action spaces
- Approximates policies using models (e.g., neural networks) since exact representation is infeasible
- Necessary for handling large or continuous action spaces

- __Policy-Based Methods__ directly optimize the policy (a mapping from states to actions) without using value functions
    - Ideal for **continuous actions**, unlike value-based methods (e.g., Q-learning)

- **Policy-Gradient Methods** learn a stochastic policy, updating parameters via **gradient ascent**
    - Includes **actor-critic methods**, which learn both policy (actor) and value function (critic)
