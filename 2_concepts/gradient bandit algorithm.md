---
tags:
  - note
  - ece750
  - ai/rl
status: review
---
# Gradient-Bandit Algorithm

- As an introduction to [Policy Approximation](2_concepts/policy%20approximation.md), we discuss this algorithm as a simple example of optimizing a policy to learn decision making

- __Stateless__: only applicable to **stateless problems** (like [multi armed bandit](2_concepts/multi%20armed%20bandit.md))
    - Methods like **SARSA** and **Q-learning** incorporate both states and actions, allowing for more flexibility in environments where action choices depend on states.

- __Action Preferences__: unike value-based methods that store $Q_t(a)$, the gradient-bandit algorithm stores **action preferences** $H_t(a)$
    - These preferences indicate how desirable an action is, without needing to estimate future rewards explicitly
    
- **Action Selection**: $H_t(a)$ values are treated like logits and put through a [softmax](2_concepts/softmax.md) to get a probability distribution of an action

- __Update equation__:
$$
H_{t+1}(a) = H_t(a) + \alpha (R_t - \bar{R}_t) \left( \mathbb{1}_{a= A_t} - \pi_t(a) \right)
$$

- where:
    - $H_t(a)$: The action preference for action $a$ at time step $t$.
    - $\alpha$: The step size or learning rate, which controls how much to update the preference.
    - $R_t$: The reward received at time $t$
    - $\bar{R}_t$: The sample average of rewards up to time $t$
    - $\mathbb{1}_{a=A_t}$: 1 if action $a$ was taken at time $t$, otherwise 0
        - when $a \ne A_t$, $H_t$ moves away from the error by $-\pi \alpha$
    - $\pi_t(a)$: The probability of selecting action $a$ at time $t$, computed using the softmax function.
