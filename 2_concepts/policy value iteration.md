---
date: August 27, 2024
status: doing
tags:
  - ai/rl/model-based
  - note
  - ece750
aliases:
  - policy iteration
  - value iteration
  - dynamic programming
---
# Policy Iteration and Value Iteration

> [!info] Background
> - From [Value Functions](2_concepts/value%20functions.md), we have the following formulations for $V^*(s)$ and $\pi^*(s)$:
>
> $$
> \begin{aligned}
> V^*(s) &= \max_\pi V(s) \\
> &= \max_\pi\mathbb{E}\big[ \sum_{t=0}^H \gamma^t R_{t+1}(S_t, A_t, S_{t+1}) | \pi, s_0=s \big] \\
> \pi^*(s) &= \arg\max_\pi V(s)\\
> &= \arg\max_\pi\mathbb{E}\big[ \sum_{t=0}^H \gamma^t R_{t+1}(S_t, A_t, S_{t+1}) | \pi, s_0=s \big] \\
> \end{aligned}
> $$
> 
> - similarly to how we were able to split up the equation for the [return function](2_concepts/return%20function.md) $G$ to: $G_t = R_{t+1} + \gamma G_{t+1}$, we can do the same for $V(s)$:
> $$
> V^*(s) = \max_\pi\mathbb{E}\big[ R_1 + \sum_{t=1}^H \gamma^t R_{t+1} \big]
> $$

## Overview

- The goal of either of these methods is to find the **optimal policy** $\pi^*$ maximizes the expected return from any state
- These are examples of [dynamic programming rl algorithms](2_concepts/dynamic%20programming%20rl.md)
- They are guaranteed to have monotonic improvement
- They are only for tabular methods since we must update our estimates for each state in our environment
- They require the environment dynamics

## Value Iteration

- Calculates the **exact, optimal** policy over a specific, finite horizon
- As $H\rightarrow\infty$, the value function should converge to the overall optimal policy

- Iteratively update the value function using the Bellman optimality equation:
$$
V_{k+1}(s) = \max_a \left[ R(s, a) + \gamma \sum_{s'} P(s'|s, a) V_k(s') \right]
$$

- Once $V(s)$ converges, the optimal policy is:
$$
\pi^*(s) = \text{argmax}_a \left[ R(s, a) + \gamma \sum_{s'} P(s'|s, a) V(s') \right]
$$

## Policy Iteration

- Start with an estimate of the optimal policy and iterate upon it to improve it
- Alternates between policy evaluation (updating $V^\pi(s)$ estimate) and policy improvement (updating $\pi(s)$):

- **Policy Evaluation**: For all for all $s \in \mathbb S$, compute $V^\pi(s)$ for a given policy $\pi$
$$
V_{k+1}(s) = \sum_{a} \pi(a|s) \left[ R(s, a) + \gamma \sum_{s'} P(s'|s, a) V_k(s') \right]
$$

- **Policy Improvement**: For all for all $s \in \mathbb S$, update the policy by choosing the action that maximizes the state-action value function:
$$
\pi_{i+1}(s) = \arg \max_a \left[ R(s, a) + \gamma \sum_{s'} P(s'|s, a) V^\pi(s') \right]
$$

## Matrix Form

For a finite state space, the Bellman equation for an MDP can be written in matrix form. Let:
- $V$ be the value function vector
- $R_a$ be the reward vector for action $a$
- $P_a$ be the transition matrix for action $a$

The Bellman equation for **policy evaluation** becomes:
$$
V^\pi = R_\pi + \gamma P_\pi V^\pi
$$

Where:
- $R_\pi(s) = \sum_a \pi(a|s) R(s, a)$ is the reward vector under policy $\pi$.
- $P_\pi(s'|s) = \sum_a \pi(a|s) P(s'|s, a)$ is the transition matrix under policy $\pi$.

For **value iteration**, the optimal Bellman equation is:
$$
V_{k+1}(s) = \max_a \left[ R(s, a) + \gamma \sum_{s'} P(s'|s, a) V_k(s') \right]
$$
In matrix form, this becomes:
$$
V_{k+1} = \max_a \left( R_a + \gamma P_a V_k \right)
$$