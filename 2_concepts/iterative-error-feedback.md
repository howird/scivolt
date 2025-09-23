---
tags:
  - ai/dl/training
---
# Iterative Error Feedback

- can be used when training

directly regressing $\Theta$ in one go is a challenging task, particularly because $\Theta$ includes rotation parameters.

- regress $\Theta$ in an iterative error feedback (IEF) loop, where progressive changes are made recurrently to the current estimate
    - the 3D regression module takes the image features $\phi$ and the current predictions, $\Theta_t$, as an input and outputs the residual $\Delta\Theta_t$
    - The parameter is updated by adding this residual to the current estimate $\Theta_{t+1} = \Theta_t + \Delta\Theta_t$
    - The initial estimate $\Theta_0$ is set as the mean, $\bar\Theta$, this is pre-calculated from the labels from our dataset
    - $[\phi, \Theta]$ are the input features to the regressor

- **IN**: 
    - Feature vector $\phi \in \mathbb{R}^{2048}$
    - Current estimate $\Theta_t$, where:
        - $\Theta_0 = \bar{\Theta}$ (mean pose & shape parameters from train set)
    
- for $t$ in $T=3$:
    - $\Delta \Theta_t := f_{\text{regressor}}(\phi, \Theta_t)$
    - two fully-connected layers with 1024 neurons each with a dropout layer in between, followed by a final layer of 85
    - $\Theta_{t+1}: = \Theta_t + \Delta\Theta_t$
- $\Theta = \Theta_T$

- **OUT**: Estimated parameters $\Theta = \{ \theta, \beta, R, t, s \}$

- note: for a single forward pass, the entire loop ($t, ..., T$) of [iterative-error-feedback](2_concepts/iterative-error-feedback.md) occurs
