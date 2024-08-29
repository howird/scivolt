---
tags:
- '#type/area'
- '#area/ai/rl`
---

# What is Reinforcement Learning?

- A mathematical formalism for learning based decision making
- An approach for learning decision making and control from experience

## How does Reinforcement Learning differ from other ML

- Generally, in ML, we have a labelled dataset $\\mathcal D = {(x_i, y_i)}$
  - The data is independently and identically distributed (i.i.d)
  - The ground truth is known during training
- In Reinforcement Learning (RL),
  - The data is not i.i.d., prev outputs influence future inputs
  - The ground truth is not known, only success/failure

## Reinforcement Learning Terminology

- Agent makes a decision,\
  !\[\[1.1.png\]\]

## Why is Deep RL Important?

- END TO END TRAINING!
  !\[\[1.2.png\]\]
- For example, classical Computer Vision involved taking an image and manually extracting low level and then mid level features before feeding those features into a classifier
- Deep Learning enabled the end to end optimization of the feature extraction and classification components altogether
- Similarly, in classical RL, one must design not only a feature extraction from the agent observation, one must also design a complex policy to produce actions
- This is incredibly difficult to do especially since domain experts in an RL problem i.e. a chess player could probably identify some heuristics to get features indicating reward, however translating those into features representing the policy would be nearly impossible as they would have to be experts in RL as well
- Deep RL allows us to train a neural net to replace the manual feature extraction with automatically learned features and trained end to end

## End to End Learning

- What does E2E learning mean for sequential decision making?

- In terms of RL, traditionally, before end to end learning would handle the recognition component and the control components separately

- non-e2e
  !\[\[1.3.png\]\]

- e2e
  !\[\[1.4.png\]\]

- non-e2e
  !\[\[1.5.png\]\]

- e2e:
  !\[\[1.6.png\]\]

- Using e2e training, each component of of the pipeline is informed and optimized by the following components

- With traditional, non-e2e training, each component is sequentially optimized individually

  - This means the components are not informed of the demands of the following components, it does not know what kind of features are important/unimportant or what kind of actions are costly

- RL problem represents the entierty the AI problem, superviesed learning relies on inputs and labels while RL aim for optimal behaviour without input/output, simply rely on reward feedback

- RL provide the algorithmic foundations and DL provides the representations that allow the RL foundations to be scaled up

## What other problems do we need to solve to enable real-world sequential decision making

- RL deals with maximizing rewards by making actions, getting a reward and figuring out hte best action based on the rewards

- this is not the only problem that matters for sequential decision making

  - learning reward functions form example (inverse RL)
  - transferring knowledge between domain (transfer learning, meta-learning or learning how to learn)
  - learning to predict and using prediction to act (model based RL, learning the representation of how the world works and using that to plan)

## How do we build intelligent machines

- logically we can start by modelling modules of the brain to perform the required tasks
- our learning mechanisms are likely powerful enough to do everything we associate with intelligence
  - it may still be convenient to hard code some modules
- The previous way of thinking was to implement an algorithm for each of the modules of the brain individually to perform a task, i.e. the visual cortex, then motor cortex
- However, is there a single flexible that we can use to encapsulate the functionality of the entire brain?
- The evidence for a single flexible learning algorithm:
  - One study showed that electrodes on the tongue have been used to allow people to see while closing their eyes with practice
  - Another study showed that when the connections to young ferrets' optic nerves were disconnected from the visual cortex and reconnected to the auditory cortex, the ferrets were able to recover their visual.Thus their auditory cortex was also able to be repurposed to see
- The results of these studies imply that since the sensory cortices of the brain can be repurposed to perform each other's jobs, they may implement the same algorithm
  - This theory could be extended to hypothesize that the functionality entire brain may be performed by the same algorithm
- What must that algorithm do?
  - interpret rich sensory inputs
  - choose complex actions
- These requirements can be fulfilled by deep reinforcement learning!
  - Deep Neural Networks have been proven to process complex sensory input
    - and also compute very complex functions
  - Reinforcement Learning provides the formalism to choose complex actions
- One study in support of deep learning \[Saxe et Al\](unsupervised learning mdels of primary cortical receptive fields and receptive field plasticity) showed:
  - tries to analyze the feature known to exist in the brain and compare to feature known to exist in primate senory cotices
  - exposed visual stimulus to a DNN known to elicit specific responss in the primate brain and found that the learned features were statistically very similar to the features in the primate brain
    - the same statistical similarities were found in auditory and touch stimuli
  - Two possible conclusions that we can infer from these results are:
    - DNNs work the same way as the brain
    - It's probably not about the DNN itself, perhaps any over-parametrized model will discover features with these statistics becase they are simply the right features for this data, the feature a are properties of the data itself and a powerful enough model will discover those same features becaus they are the right ones
- Studies in support of RL: Some studies in psychology and neuroscience
  - percepts that anticipate reward become associated with similar firing patterns as the reward itself
  - basal ganglia appears to be related to the reward system
  - model-free RL-like adaptation is often a good fit for experimental data of animal adaptation
- Thus, if there is a single flexible aalgo that can acquire the broafdb ehaviours associated with human intelligence that algo may look like an RL algo equipped with large high cacpacity representations like DNNs
- What can DRL do well now
  - current DRL can acquire a high degree of proficiency in domains governed by simple known rules
  - learn simple skills with ra sensory inputs given enough experience
  - learn from imitatin enoug himan provided expert behaviour
- What has prvoen challenging
  - humans can learn very quicklu
    - deep RL are notv ery efficient require a lot of experience
  - Humans can reuse past knowledge to learn new tasks
  - not clear wht the reqard funciton should be
    - in classis RL the read fn is know however this is not the case in the real world
  - not clear what the role of prediciton should be
    - should we learn by trial and error or learn from creating and internal model of the entire of the world and planning from that model
- What can RL provide to us?
  - a way to think about the acquisition of intell in a unified algortihmic ways wio havith to design the indiviual algos
- Instead of trying to produc