---
tags:
  - paper
  - "#ai/rl"
status: backlog
year: 2025/01
authors: Scott Fujimoto, Pierluca DOro, Amy Zhang, Yuandong Tian, Michael Rabbat
citekey: fujimotoGeneralPurposeModelFreeReinforcement2025
---
# Towards General-Purpose Model-Free Reinforcement Learning

- **Problem Addressed:**
    - Reinforcement learning (RL) algorithms are often specialized to particular benchmarks, requiring careful hyperparameter tuning and specific algorithmic choices.
    - While powerful model-based RL methods have shown general results, they suffer from high complexity and slow run times.
    - The paper aims to develop a unifying model-free deep RL algorithm that can perform well across a diverse range of domains and problem settings without re-tuning.

- **Proposed Solution: MR.Q (Model-based Representations for Q-learning)**
    - A model-free RL algorithm that leverages model-based representations.
    - It aims to learn features that create an approximately linear relationship between state-action pairs and the value function.
    - This is achieved by using model-based objectives to learn embeddings ($Z_s$​ for state, $Z_{sa}$​ for state-action) which then serve as inputs to the policy and value functions.
    - The core idea is that the benefit of model-based objectives lies in the learned representation rather than the model itself
    
- **Key Characteristics and Motivations of MR.Q:**
    - **Unified Input Space:** By mapping states and actions to a unified embedding, environment-specific input characteristics are eliminated, allowing for standardized hyperparameters
    - **Linearity Motivation:** The theoretical basis is that model-free and model-based approaches converge to the same solution in a linear feature space. Theorem 1 and 2 support this by showing the equivalence of fixed points and bounding value error by model accuracy.
        
    - **Practical Relaxations:**
        - To avoid dependence on the current policy and undesirable local minima, the dynamics target uses a state-dependent embedding ($Z_{s′}$​) from a target network, rather than a state-action embedding ($Z_{s′a′}$​) from the current policy/encoder.
            
        - A non-linear value function ($Q^​{(zsa)​}$) is used with the learned features to account for approximation errors, as the linear relationship is only approximate. Theorem 3 provides justification that such a non-linear function Q^​ can exist if features are sufficiently rich (MDP homomorphism).
            
    - **Encoder Loss:** Composed of three terms for reward, dynamics, and terminal signal, unrolled over a short horizon ($H_{Enc}$​)
        - Reward prediction uses a categorical representation with cross-entropy loss for robustness to sparse rewards and varying magnitudes.
        - Dynamics loss minimizes MSE between predicted next state embedding and the target encoder's next state embedding
        - Terminal loss uses MSE for the predicted terminal signal
            
    - **Value Function:** Based on TD3, using two value functions, minimum of target networks for target value, and multi-step returns (HQ​). Huber loss is used. Target value is normalized by the average absolute reward in the replay buffer.
        
    - **Policy:** Updated using deterministic policy gradient, with Gumbel-Softmax for discrete actions and Tanh for continuous actions. A small regularization on pre-activations is added.
        
    - **Synchronized Updates:** Target networks, reward scaling, and the encoder are updated periodically at the same time (Ttarget​) to reduce non-stationarity.
        
- **Evaluation and Results:**
    
    - Evaluated on four RL benchmarks (Gym - Locomotion, DMC - Proprioceptive, DMC - Visual, Atari - 10M) covering 118 environments, using a single set of hyperparameters.
        
    - MR.Q showed competitive performance against domain-specific and general baselines.
        
    - Achieved strong performance with fewer network parameters and faster training/evaluation speeds compared to general-purpose model-based methods like DreamerV3.
        
    - Outperformed PPO, DQN, and Rainbow in Atari.
        
    - Was the strongest overall across continuous control benchmarks, achieving highest performance in both DMC benchmarks.
        
- **Significant Perspectives/Insights (Potentially Beyond Abstract):**
    
    - The paper emphasizes that the _representation_ learned via model-based objectives might be the most crucial component, even more so than the planning or simulation aspects often associated with model-based RL.
        
    - A "no free lunch" phenomenon is observed, where top-performing baselines in one benchmark do not necessarily replicate success in others, highlighting the need for evaluation across diverse tasks.
        
    - Design choices like categorical reward loss and dynamics unrolling show different impacts across benchmarks (e.g., Gym vs. Atari), underscoring how hyperparameters can overfit and the importance of multi-benchmark evaluation.
        
- **Glaring Assumptions:**
    
    - The environments are assumed to be Markov Decision Processes (MDPs) or be reasonably approximated by them.
        
    - The paper assumes that a unified embedding and a single set of hyperparameters can be effective across diverse environments, which is what it sets out to prove.
        
    - The theoretical motivation relies on the possibility of achieving an approximately linear relationship between learned features and the true value function.
        
- **Potential Prerequisite Knowledge (Conservative Recommendations):**
    
    - A solid understanding of fundamental RL concepts: MDPs, value functions (Qπ(s,a)), policy (π), Bellman equations, temporal difference (TD) learning.
        
    - Familiarity with common deep RL algorithms, particularly:
        - Q-learning and DQN
            
        - TD3 (as MR.Q's value learning is based on it).
            
    - Basic concepts of representation learning in RL.
        
    - The concept of MDP homomorphisms could be useful for a deeper understanding of the theoretical underpinnings of Theorem 3.
        
    - Parr et al. (2008), "An analysis of linear models, linear value-function approximation, and feature selection for reinforcement learning," as this work is heavily drawn upon for the theoretical motivation regarding linear feature learning.