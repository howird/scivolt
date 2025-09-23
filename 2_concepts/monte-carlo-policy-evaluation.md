---
tags:
  - note
  - ai/rl/model-free
  - ece750
aliases:
  - MC
status: done
---
# Monte Carlo Policy Evaluation

- **Key Idea**: Estimate value functions using the average of observed returns over multiple episodes (trajectories)

- does not require MDP dynamics/rewards ([model-free](2_concepts/model-free.md))
- no [bootstrapping](2_concepts/bootstrapping.md)
- does not assume state is Markov
- can only be applied to episodic MDPs
    - averaging over returns from a complete episode
    - episode must end before its data can be used to update the value function
- generally high variance estimator
    - reducing variance can require a lot of data


- **First-Visit Monte Carlo**: Only considers the first occurrence of each state within an episode
    - this makes $V^\pi$ an __unbiased__ estimator, as each episode is [i.i.d.](2_concepts/individually-identically-distributed.md)
- **Every-Visit Monte Carlo**: Considers every occurrence of each state within an episode
    - using multiple states per episode makes $V^\pi$ a __biased__ estimator, because while each episode is independent the individual state-action-reward pairs are within an episode are not [i.i.d.](2_concepts/individually-identically-distributed.md)
    - this method is still empirically better, we can have more updates, more often

### First-Visit/Every-Visit MC Algorithms

- Initialize $V(s)$, $N(s)$, $G(s)$ to $\leftarrow 0$ for all $s \in S$
- For each episode, $i$: $[(s_{i,1}, a_{i,1}, r_{i,1}), (s_{i,2}, a_{i,2}, r_{i,2}), \dots, (s_{i,T}, a_{i,T}, r_{i,T_i})]$
    - For each ($s$ encountered for the first time in the episode __OR__ time step $t$)
        - $G_{i,t} = r_t + \gamma r_{i, t+1} + \gamma^2 r_{i, t+2} + \dots + \gamma^{T_i-1} r_{i, T_i}$
        - $N(s) = N(s) + 1$ (increment the counter for state $s$)
        - $G(s) = G(s) + G_t$ (add the return to the total return for $s$)
        - Value estimate: $V(s) = G(s)/N(s)$
            - can be rewritten as $V(s) = V(s) + \alpha(G_{i,t}-V(s))$ where $\alpha=1/N(s)$
                - when $\alpha>1/N(s)$ older values are forgotten over time

### Extension to Q Function

- When extending the original state value function $V$ to the state-action value function, $Q$, the only thing modified is that we act on state-action tuples rather than just states (obviously)
- During the policy improvement step, this lets us do $\pi = \arg \max_a Q(s, a)$

- Initialize $Q^\pi(s, a)$, $N(s, a)$, $G(s, a)$ to $\leftarrow 0$ for all $s \in S, a \in A$
- For each episode, $i$: $[(s_{i,1}, a_{i,1}, r_{i,1}), (s_{i,2}, a_{i,2}, r_{i,2}), \dots, (s_{i,T}, a_{i,T}, r_{i,T_i})]$
    - For each ($s$ encountered for the first time in the episode __OR__ time step $t$)
        - $N(s, a) = N(s, a) + 1$
        - $G(s, a) = G(s, a) + G_t$
        - Value estimate: $Q^\pi(s, a) = Q^\pi(s, a) + \alpha(G_{i,t}-Q^\pi(s, a))$
