---
tags:
  - paper
  - "#ai/rl"
  - "#ai/rl/model-free"
status: review
year: 2019/07
authors: Timothy P. Lillicrap, Jonathan J. Hunt, Alexander Pritzel, Nicolas Heess, Tom Erez, Yuval Tassa, David Silver, Daan Wierstra
citekey: lillicrapContinuousControlDeep2019
aliases:
  - DDPG
---
# DDPG: Continuous control with deep reinforcement learning

![DQN vs DDPG](2_concepts/media/Pasted%20image%2020250520114233.png)

- DDPG is the spiritual successor to [DQN](2_concepts/deep%20q%20networks.md), but adds an explicit actor for control which is essential for continuous action spaces

### Algorithm

![DDPG algorithm](2_concepts/media/Pasted%20image%2020250520114946.png)


- For the critic parameter update, $\theta^Q$ is updated with the $\text{MSE}$ loss of $Q$'s [TD Error](2_concepts/temporal%20difference%20policy%20evaluation.md) with the state and actions as inputs and the gradient update done with respect to the parameters

- For the actor parameter update, $\theta^\mu$ is updated with the policy's, $\mu$, gradient with respect to the parameters however, it is scaled by $Q$'s gradient with respect to the action chosen by $\mu$

- Additionally, the parameter updates for both models are 'soft' updates, to improve stability
- DDPG is an off-policy algorithm, the replay buffer can be large, allowing the algorithm to benefit from learning across a set of uncorrelated transitions
- BatchNorm is used for better generalization

- Noise from an Ornstein-Uhlenbeck process is introduced to the policy to generate temporally correlated exploration for exploration efficiency in physical control problems with inertia

- As in [DQN](2_concepts/deep%20q%20networks.md) action repeats were used:
    - For each timestep of the agent, we step the simulation 3 timesteps, repeating the agent’s action and rendering each time
    - Thus the observation reported to the agent contains 9 feature maps (the RGB of each of the 3 renderings) which allows the agent to infer velocities using the differences between frames

- The frames were downsampled to 64x64 pixels and the 8-bit RGB values were converted to floating point scaled to $\in [0, 1]$