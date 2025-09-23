---
tags:
  - note
  - ai/rl/model-based
  - ece750
  - ai/rl/control
  - ai/rl/on-policy
  - ai/rl/td-method
status: review
---
# SARSA

- An on-policy [control](2_concepts/control-policy-evaluation.md) algorithm based on [TD policy evaluation](2_concepts/temporal-difference-policy-evaluation.md)
- Chooses an action, not necessarily the best one, sees the result, then updates it’s value function with that knowledge
- will converge eventually, but more slowly than [q-learning](2_concepts/q-learning.md)

## Algorithm

- Initialize the action-value function $Q(s, a)$ for all state-action pairs arbitrarily, except for terminal states where $Q(s_{\text{terminal}}, \cdot) = 0$
- For each episode:
    - Initialize the starting state $S$
    - choose an action $A$ based on the current policy derived from $Q(s, a)$
    - For each step within the episode:
        - Take action $A$, observe the reward $R$ and the next state $S'$
        - Choose the next action $A'$ from the new state $S'$ using the policy
        - $Q(S, A) \leftarrow Q(S, A) + \alpha \left( R + \gamma Q(S', A') - Q(S, A) \right)$
        - Update the state $S \leftarrow S'$ and action $A \leftarrow A'$

- note:
    - we update $Q(S, A)$ with the same $Q(S, A)$ choose actions

# Expected Sarsa

- A variation of the SARSA algorithm, where instead of using the **sampled value of the next state-action pair**, it uses the **expected value** of the next state-action value function
- This method calculates the expected return by taking into account all possible actions in the next state and weighting them according to the policy.

## Algorithm:

- Initialize the action-value function $Q(s, a)$ for all state-action pairs arbitrarily, except for terminal states where $Q(terminal-state, \cdot) = 0$
- For each episode:
    - Initialize the starting state $S_t$
    - Choose an action $A_t$ based on the current policy derived from $Q(s, a)$
    - For each step within the episode:
        - Take action $A_t$, observe the reward $R_{t+1}$ and the next state $S_{t+1}$
        - $Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha \left[ R_{t+1} + \gamma \sum_a \pi(a|S_{t+1})Q(S_{t+1}, a) - Q(S_t, A_t) \right]$

        - Update the state $S_t \leftarrow S_{t+1}$ and action $A_t \leftarrow A'$

## Comparison:

- **SARSA:** Updates based on the actual next action taken
- **Expected Sarsa:** Updates based on the expected value of all actions at the next state, weighted by the policy probabilities.
- **Performance:** Expected Sarsa typically performs better than SARSA in terms of stability and convergence speed, though it involves more computation as it requires calculating the expected value over all actions.
