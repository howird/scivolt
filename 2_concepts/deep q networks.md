---
tags:
  - paper
  - "#ai/rl"
status: review
year: 2013/12
authors: Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, Martin Riedmiller
citekey: mnihPlayingAtariDeep2013
aliases:
  - Playing Atari with Deep RL
  - DQN
---
# Playing Atari with Deep Reinforcement Learning

## Deep Q Networks (DQN)

### Overview

- This is a #ai/rl/model-free algorithm strictly for discrete action spaces since:
- The output is a probability distribution (softmaxed logits) corresponding to each action to take, and the policy is simply the best action over the action space:

$$
\pi(s, a) = \arg \max_{a \in A} Q(s, a)
$$

- This policy would be intractable to evaluate for a continuous action space
    - See [DDPG](2_concepts/deep%20deterministic%20policy%20gradient.md) for a similar algorithm that circumvents this

### Key Contributions

#### 1. Two Networks for Q-Learning (Double DQN)

- **Prediction Network (Q-Network)**
    - Parameters: $\theta_i$ at iteration $i$
- **Target Network**
    - Parameters: $\theta_i^-$ are used to compute the target network at iteration $i$
        - These parameters are updated every $C$ steps ($\theta_i^- \leftarrow \theta_i$), holding the weights fixed between updates

#### 2. Mini-batches / Experience Replay
- **Experience Storage:** Store experiences $e_t = (s_t, a_t, r_t, s_{t+1})$
- **Experience Dataset:** Full dataset $D_t = \{e_1, e_2, \dots, e_t \}$
- **Training Q-Network:** Samples are drawn uniformly at random from the stored experiences
- Instead of updating the network with experiences as they occur (which would lead to highly correlated updates), DQN uses **experience replay** to randomly sample past experiences
    - This breaks the correlation between consecutive experiences, creating a more i.i.d.-like environment for training

#### 3. Loss Function for DQN
- The loss function is defined as (this is essentially just a simple TD update):
$$
L_i(\theta_i) = \mathbb{E}_{(s,a,r,s') \sim U(D)} \left[ \left( r + \gamma \max_{a'} Q(s', a'; \theta_i^-) - Q(s, a; \theta_i) \right)^2 \right]
$$
- Where:
    - $\theta_i$ are the parameters of the Q-network
    - $\theta_i^-$ are the target network parameters, updated periodically
    - $\mathbb{E}_{(s, a, r, s') \sim U(D)}$:  the experiences $(s, a, r, s')$ are sampled **uniformly** at random from the **replay buffer** $D$
        - This introduces an i.i.d.-like setting by breaking the temporal correlations present in the sequential data.


## Other Info

- CNN architecture:
    - input to the network is a **stack of four consecutive frames** (84x84 grayscale) from the game environment, to capture the temporal dynamics of the environment
    - `Conv2d(4, out_channels=32, kernel_size=(8, 8), stride=4)`
    - `Conv2d(32, out_channels=64, kernel_size=(4, 4), stride=2)`
    - `Conv2d(64, out_channels=64, kernel_size=(3, 3), stride=1)`
    - `flatten`
    - `Linear` -> one hot encoded vector for each action

- Activation:
    - ReLU
    - SoftMax for output