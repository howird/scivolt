---
tags:
  - note
  - ai/rl
  - math/prob/markov-chains
  - ece750
status: todo
aliases:
  - MRP
---
# Markov Reward Process (MRP)

- A **Markov Reward Process (MRP)** is an extension of a [Markov Chain](2_concepts/markov-chain.md) where the addition of rewards for each state

- $M R P(S, P, R, gamma)$:
    - $S$: A finite set of states
    - $P(s'|s)$: Transition probability matrix, where $P(s'|s)$ is the probability of transitioning from state $s$ to state $s'$
    - $R(s)$: Reward function, which gives the expected reward received upon entering state $s$
    - $gamma$: Discount factor, $gamma in [0, 1]$

## DP Solution of Bellman Equation for MRP

- For an MRP, the [value function](2_concepts/value-functions.md), $V(s)$, represents the expected return (cumulative discounted rewards) starting from state $s$
- [Bellman equation](2_concepts/bellman-equations.md) for the value function is:
$$
V(s) = R(s) + gamma sum_(s') P(s'|s) V(s')
$$
- This is a recursive equation that expresses the value of state $s$ as the immediate reward plus the discounted sum of expected future rewards.

### Algorithm

- for $s in SS$
    - $V_0(s) := 0$
- for $k:=1$ until convergence:
    - $V_k (s) : = R(s) + gamma sum_(s' in S) P(s'|s) V_(k - 1)(s')$

## Analytic Solution of Bellman Equation

- In matrix form, the Bellman equation for all states can be written as:
$$
V = R + gamma P V
$$
- Where:
    - $V$ is the **value function vector** (of size $N times 1$, where $N$ is the number of states).
    - $R$ is the **reward vector** (of size $N times 1$).
    - $P$ is the **state transition matrix** (of size $N times N$), where each element $P(s'|s)$ represents the transition probability from state $s$ to state $s'$.

## Analytic Solution for the Value Function

- Given:
- **Transition matrix** $P$:
    - row $i$: $S_i -> S_n in upright(bold(S))$
    - column $j$: $S_n in upright(bold(S)) -> S_j$
    - $P$ is a stochastic matrix, thus its [eigenvalues](2_concepts/eigenvectors.md) will always $<= 1$

$$
P = mat(P(s_1 |s_1), P(s_2 |s_1), ..., P(s_n |s_1);
        P(s_1 |s_2), P(s_2 |s_2), ..., P(s_n |s_2);
             dots.v,      dots.v, dots.down, dots.v;
        P(s_1 |s_n), P(s_2 |s_n), ..., P(s_n |s_n))
$$

- **Reward vector** $R$:

$$
R = mat(R(s_1);
R(s_2);
dots.v;
R(s_n))
$$

- **Value function vector** $V$:
$$
V = mat(V(s_1);
V(s_2);
dots.v;
V(s_n))
$$
- For a finite, discrete state MRP we can express $V(s)$ with a matrix equation

$$
V = R + gamma P V \
V - gamma P V = R \
(I - gamma P) V = R \
V = (I - gamma P)^(-1) R
$$

- note: $P$ is a stochastic matrix, thus its [eigenvalues](2_concepts/eigenvectors.md) will always $<= 1$
    -  if $gamma < 1$ then $(I - gamma P)$ will always be invertable
### Complexity:

- Solving the matrix equation directly requires inverting $(I - gamma P)$, which has a time complexity of $O(N^3)$, where $N$ is the number of states.
