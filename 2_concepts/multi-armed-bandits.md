## Multi-armed Bandits

- suppose you form estimates $Q_t(a)=q\_*(a)$
  $$
  A^*\_t = argmax Q_t(a)
  $$

- if the sample average estimates converge to the true values if the action is taken an infinite number of times

- in greedy, you always exploit

- in eps-greedy you take the greedy action usually, but with probability $\\epsilon$, you instead pick an action at random (possibly the greedy action again)

- this is the simplest way to balance exploration and exploitation

- standard stochastic approximation convergence conditions

- suppose the true action

- upper confidence bound action selection

  - clever way of reducting exploration over time
  - stimate an upper bound on the true action values
  - select the action with the largest (estimate) upper bound
  - sqrt term measures the uncertainty or variance
  - c>0 controls level of exploration determince confidence level
  - log t: increases get smaller over time but nver go away
  - N_t(a) = 0: infinity so a is maximized, goes down as more data is collected

- gradient bandit algorithms
