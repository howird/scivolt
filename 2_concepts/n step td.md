---
tags:
  - note
  - ece750
  - ai/rl
status: doing
---
# N-Step Temporal Difference Learning

1. **Monte Carlo (MC) Method**:
   - The total return $R_t$ is calculated by summing all future rewards, discounted by $\gamma$ (the discount factor). 
   - Formula: $R_t = r_{t+1} + \gamma r_{t+2} + \gamma^2 r_{t+3} + \cdots + \gamma^{T-t-1} r_T$.
   - MC methods wait until the episode is complete before making any updates.

2. **1-step TD (Temporal Difference)**:
   - In 1-step TD, the return is approximated with:
     $$
     R_t^{(1)} = r_{t+1} + \gamma V_t(s_{t+1})
     $$
   - This uses the current value function $V$ to estimate the remaining return after the first step, rather than waiting for the full episode.

3. **n-step TD**:
   - **2-step return**: In this approach, we sum rewards over two steps before estimating the remaining return using the value function:
     $$
     R_t^{(2)} = r_{t+1} + \gamma r_{t+2} + \gamma^2 V_t(s_{t+2})
     $$
   - **n-step return**: The return is extended to $n$ steps:
     $$
     R_t^{(n)} = r_{t+1} + \gamma r_{t+2} + \gamma^2 r_{t+3} + \cdots + \gamma^{n-1} r_{t+n} + \gamma^n V_t(s_{t+n})
     $$
   - The more steps used, the more delayed the value estimation, but this can lead to better accuracy in return approximation.

### Slide 2: Learning with N-step Backups

1. **Backup Process**:
   - **On-line** or **off-line** updates are used to improve the value function.
   - Update rule: 
     $$
     \Delta V_t(s_t) = \alpha \left[ R_t^{(n)} - V_t(s_t) \right]
     $$
   - $\alpha$ is the learning rate, $R_t^{(n)}$ is the n-step return, and $V_t(s_t)$ is the current estimate of the value of state $s_t$.

2. **Error Reduction**:
   - The slide presents the error reduction property of n-step returns:
     $$
     \max_s \left| E_\pi \{R_t^{(n)} | s_t = s\} - V^\pi(s) \right| \leq \gamma^n \max_s \left| V(s) - V^\pi(s) \right|
     $$
   - This inequality shows that as $n$ increases, the error between the n-step return and the true value function decreases, multiplied by a factor $\gamma^n$. Therefore, n-step returns help to reduce error over time and converge to the optimal value function.

3. **Convergence**:
   - Based on this error reduction property, it can be shown that **n-step methods converge**. Larger values of $n$ generally result in a better approximation but with a trade-off in computational cost.

### Slide 3: Random Walk Examples

1. **Random Walk Setup**:
   - The diagram depicts a random walk problem where states $A$, $B$, $C$, $D$, and $E$ represent positions in the environment.
   - At the end states (left of A and right of E), terminal rewards are received (0 and 1, respectively).
   - The starting point is at state $C$, and the agent can move either left or right.

2. **Questions**:
   - **How does 2-step TD work here?**
     - In 2-step TD, the return is computed over the next two states, with the value function estimating the remaining returns. This would involve summing rewards from the next two states and updating based on that information.
   - **How about 3-step TD?**
     - In 3-step TD, the update would sum rewards over three states before using the value function to estimate the rest of the return. This typically results in a more accurate prediction than 2-step, as it incorporates more future information.
        