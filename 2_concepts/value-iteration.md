---
date: August 27, 2024
status: doing
tags:
  - '#reinforcement-learning/model-based'
  - '#note/algorithm'
---

# Value Iteration

- But how do we even get values... If each

$$
V^*_k(s) = \max_a \sum_{t=0}^H P(s'|s,a)  \bigg(R(s, a, s') + \gamma_t V^*_{k+1}(s')\bigg)
$$
