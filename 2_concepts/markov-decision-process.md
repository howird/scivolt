---
date: August 27, 2024
status: done
tags:
  - '#area/ai/rl'
  - '#type/theory'
---

# Markov Decision Process

> \[!info\] Background
>
> - A __Markov chain__ is a mathematical model used to describe a system that transitions from one state to another within a set of possible states, $S$
> - __Markov Property__: the probability of transitioning to any future state depends only on the current state and not on the sequence of events that preceded it
> - Usually represented by a matrix of transition probabilities, where each entry in the matrix represents the probability of moving from one state to another

- A Markov Decision Process (MDP) is an extension of a Markov chain that incorporates decision-making

- A state transition in an MDP is now conditioned on an action

  - in the case of a discrete MDP, the transition matrix adds a dimension for actions

- $MDP(S, A, T, R, \\gamma, H)$:

  - Set of states $S$
  - Set of actions $A$
  - Transition function $T(s'|s, a)$
  - Reward function $R(s, a, s')$
    - note: the reward at
  - Start state $s_0$
  - Discount factor $\\gamma \\in \[0,1\]$
  - Horizon $H$

- __Reinforcement Learning__ (RL) defines the state to encapsulate an agent and environment

  - __Agent__: learns and selects actions
  - __Environment__: responds to actions by providing the next state and a reward

![MarkovDecision Process Diagram](Pasted%20image%2020240821184927.png)

- Goal of RL is to learn a policy, $\\pi$, that will maximize the (discounted) expected reward:
  $$
  \\pi(s) = \\arg\\max\_\\pi E\[\\sum\_{t=0}^H\\gamma_tR(S_t, A_t, S\_{t+1}|\\pi)\]
  $$
- note: the policy $\\pi(s)$ returns a probability distribution over all possible actions

> \[!question\]
>
> - (1) One confusing aspect is the alignment of the state actions and rewards at each time step:
>
>   - $S_t$ is the state at the current time step
>   - $R_t$ is the reward we received when we transition\_\_ed\_\_, from the previous state to the current state ($S\_{t-1}\\rightarrow S_t$) via the previous action $A\_{t-1}$
>   - $A_t$ is the action we __will__ take to transition from $S_t\\rightarrow S\_{t+1}$
>
> - Thus, the function above can be clarified by changing $R \\rightarrow R\_{t+1}$
>
>   - note: $R_t$ does not exist in the equation since, it doesn't matter anymore
>
> - (2) Why is $S\_{t+1}$ an __input__ to the reward function $R$ (not just $S_t$ and $A_t$)?
>
>   - Since the transition function is probabilistic, we cannot know what the next state will be with just $S_t$ and $A_t$, and the reward received at the next step $R\_{t+1}$ cannot be know with out the next state $S\_{t+1}$
