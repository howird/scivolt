---
tags:
  - note
  - ai/rl
---
# Linear-Exponential Policies (Discrete Actions)

- An extension of the [gradient bandit algorithm](2_concepts/gradient-bandit-algorithm.md), that uses the __preference__, $h$ but now adds state and action: $h(s,a)$
- Although $h$ now resembles a [state-action value function](2_concepts/value-functions.md), it differs since:
    - it simply represents the "desirability" or "intensity", its just a logit for softmax activation
    - it not directly tied to expected future rewards like $Q$ or $V$
    
- **Linear preferences**: Action preferences $h(s, a, \theta)$ are modeled as a linear combination of parameters $\theta$ and a state-action feature vector $x(s, a)$
$$
h(s, a, \theta) = \theta^\top x(s, a)
$$

- **Action probability**: The probability of selecting an action $a$, $\pi(a|s, \theta)$, follows a [softmax](2_concepts/softmax.md) distribution based on the preferences, $h$:
$$
\pi(a|s, \theta) = \frac{\exp(h(s, a, \theta))}{\sum_b \exp(h(s, b, \theta))}
$$
- note: here we use $b$ as the action we are iterating over (within the set of actions we are able to take from $s$)

## Policy Update

- The policy gradient (or **eligibility vector**) is given by:
  $$
  \nabla_\theta \ln \pi(a|s, \theta) = x(s, a) - \sum_b \pi(b|s, \theta) x(s, b)
  $$
- In **linear-exponential policies**, the update involves adjusting the parameters $\theta$ based on the gradient of the log-probability of the action taken

- This is more sophisticated than the gradient-bandit algorithm, as it incorporates feature vectors and takes into account the influence of all actions in the state, not just the selected one


### Example of Stochastic Policies:

#todo : idk where this belongs

![](2_concepts/media/Pasted%20image%2020241024224836.png)

- **Short Corridor Problem**: Demonstrates that deterministic policies (e.g., $\varepsilon$-greedy) can perform poorly in certain environments, like a short corridor with switched actions
- Optimal performance is achieved with a **stochastic policy**, which requires actions to be selected with specific probabilities (e.g., probability of right action).
- This reinforces the need for **stochastic policies**, as linear-exponential methods can handle such problems better than deterministic approaches.

