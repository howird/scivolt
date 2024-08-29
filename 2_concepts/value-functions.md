---
date: August 27, 2024
status: doing
tags:
  - '#ai/rl/model-based'
  - '#type/theory'
---

# Rewards and Value Functions

> \[!info\] Background
> [markov-decision-process](markov-decision-process.md)

## Return

- The return is defined as some specific function of the reward sequence, in the simplest case the sum of all future rewards up until termination ($H$):

$$
G_t = \sum_{k=1}^HR_{t+k}
$$

- We can further generalize the return to __discount rewards__ found farther i__n the future__ by including: $\gamma$
  - note: this is a generalization since when $\gamma=1$, we get the previous equation
- Additionally we show that $G_t = R_{t+1} + \gamma G_{t+1}$:

$$
\begin{aligned}
G_t &= \sum_{k=0}^H \gamma^k R_{t+k+1} \\
&= \gamma^0 R_{t+1} + \sum_{k=0}^H \gamma^{(k+1)} R_{t+k+2} \\
&= \gamma^0 R_{t+1} + \gamma \bigg(\sum_{k=0}^H \gamma^{k} R_{(t+1)+k+1}\bigg) \\
&= R_{t+1} + \gamma G_{t+1} \\
\end{aligned}
$$

- This is true for all time steps $t\<T$ even if termination occurs at the next time step, if we define $G_H = 0$,  $\because G_{H-1} = R_H + 0$

## Value Function

- The return, $G$, is not especially meaningful or tangible because we don't want to know the __sum__ of future rewards

- Instead, we want the know the __expected__ future rewards __starting a specific state__, following a __specific policy__

- A value function $V(s)$ is the expected sum of discounted rewards when starting from state $s$ and acting under a policy $\pi$
  $$
  V(s) = \mathbb{E}\big\[ \sum_{t=0}^H \gamma^t R_{t+1}(S_t, A_t, S_{t+1}) | \pi,s_0=s \big\]
  $$

- An __optimal__ value function $V^\*(s)$ is the expected sum of discounted rewards when starting from state $s$ and acting under an __optimal__ policy $\pi$

  - the optimal policy is defined as the policy which maximizes the value function
    $$
    \begin{aligned}
    V^*(s) &= \max_\pi\mathbb{E}\big\[ \sum_{t=0}^H \gamma^t R_{t+1}(S_t, A_t, S_{t+1}) | \pi, s_0=s \big\] \\\
    \pi^*(s) &= \arg\max_\pi V(s)\\
    &= \arg\max_\pi\mathbb{E}\big\[ \sum_{t=0}^H \gamma^t R_{t+1}(S_t, A_t, S_{t+1}) | \pi, s_0=s \big\] \\
    \end{aligned}
    $$

## Value Iteration

- But how do we even get values... If each

$$
V^*_k(s) = \max_a \sum_{t=0}^H P(s'|s,a)  \bigg(R(s, a, s') + \gamma_t V^*_{k+1}(s')\bigg)
$$
