# Dreamer

- addresses the problem of instead of running a bunch of trials, learn a model of the world by collecting samples to create latent world models and then learns to train itself in imagination

- dreamerv3: goal: very data efficient can throw any environment at it

- dreamerv1 to v3 progression
    - planet: train world models on high dimensional inputs:
        - to make this feasible you need:
            - world model: representation that gives the agent rich perception, summarizes inputs compactly, latent representation
            - dynamics model: predict forward, ie model predictive control or monte carlo tree search
        - why has this been challenging in the past:
            - 1. need an accurate model, that actually represents the environment well
            - 2. compute-efficiency: compute scales the same as data in RL
        - in planet they figured out how to learn a world model, by encoding all sensory inputs into compact repr at each timestep, w/ stochastic bottle neck
        - learning to predict sequence of compact repr w/ gru conditioned on sequence of actions, trained via image reconstr. and predicting rewards
            - rewards is important enabling "dreaming" w/o image reconstr.
    - planet -> v1
        - how do we derive behaviour from model
            - online planning at each timestep as you interact w/ env
                - comp inefficient
                - bunch of rollouts w/ model to find a good action, cant reuse comp for each timestep, plan didnt look for into the future
                - thousands of model rollouts at each step in the environment
                - cannot compete with methods w/ methods using simulated envs
    - v1: offline rollouts starting w/ states in replay buffer
        - using rollouts to train AC policy thats fast to sample from
        - also has V fn and therefore can take rewards into account that are beyond rollout horizon
        - focused on continuous control from pixels, data-efficient, had high performance but not very general of an algorithm
        - could not handle discrete actions very well, thus could not perform well on atari
    - v2: attempted to improve atari results, used discrete representations and discrete actions
        - also improved objective functions
        
    - v3: next natural step, people wanted to use to use dremerv2 for a wider range of problems esp where data efficiency matters and high dimensional inputs
        - in hparam tuning, for various tasks, danijar gained intuitions about them such as: 
        - entropy reg higher with high rewards, need to explore more
        - visual complexity of environment is low i.e. atari, thus need to pay importance to individual pixels to get good performance, thus need to change the world model objective to get really good at reconstruction and not abstract much away, whereas in complex 3D envs you want abstract more away to generalize more quickly/better and forward predication improves as well
        - goal of dreamer v3: be able to run it out of the box w/o tuning hparams too much
        - bc the algo is so robust, observed very predictable scaling behaviour of the algorithm
        - if you do more gradient steps (replay more data), you will be more data efficient however, at some point you will begin overfitting, however, this takes longer with world models
            - in a sense the wm lets you trade compute (gradient steps) for data efficiency
        - more surprisingly, increasing the size of the model, improves data efficiency and then performance
            - this is found in SL (LLMs) but not in RL (until now)

- dreamer does well as a meta RL agent?:
    - the model ingrates information over time into markovian states, there is actually a reason we are not using transformers in the world model (even though they are everywhere now)
    - markovian states make it much easier to do control / rl on top of the representations, its easier to fit a seq with a transformers that doesnt have this recurrent bottleneck to squeeze everything to, but by forcing the model to learning markovian reprs, we are offloading whats challenging in RL to the unsupervised model learning objective, so we dont need rewards to learn whats relevant about the state
    - not that surprised that just bc its a sequence model (integrates info over time) that feeding rewards, and understand what they mean
- 