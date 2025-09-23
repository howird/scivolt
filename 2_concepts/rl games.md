---
tags:
  - guide
  - ai/rl
  - sw/tool/ai
status: doing
---
# RL Games Python Library

- Uses the Builder Factory design pattern
- Builder
    - `load(params)`: 
- Factory
    - `create(params)`: 

- Each Builder has a Factory as a field

- when an Agent is instantiated, it runs `self.load_networks()` which reads the `params`, then builds a Model

- What is the difference between 