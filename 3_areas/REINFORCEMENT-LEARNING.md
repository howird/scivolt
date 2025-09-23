---
tags:
  - area
  - ai/rl
  - ece750
---

# Reinforcement Learning?

- At a high level, __Reinforcement Learning__ (RL)  is:
    - A mathematical formalism for learning based decision making
    - An approach for learning decision making and control from experience

- RL defines the state to encapsulate an agent and environment
    - __Agent__: learns and selects actions
    - __Environment__: responds to actions by providing the next state and a reward

![Markov Decision Process Diagram](Pasted%20image%2020240821184927.png)

## How does Reinforcement Learning differ from other ML

- Generally, in ML, we have a labelled dataset $\mathcal D = {(x_i, y_i)}$
    - The data is independently and identically distributed (i.i.d)
    - The ground truth is known during training
    
- In Reinforcement Learning (RL),
    - The data is not i.i.d., prev outputs influence future inputs
    - The ground truth is not known, only success/failure

[MDPs](markov-decision-process.md)
[Value functions](value-functions.md)

