---
status: backlog
tags:
  - '#ai/dl'
---

#### 5.1 Challenges include high dimensionality, non-convexity, poor conditioning, and gradient cliffs

-

#### 5.2 Deep networks probably do not suffer much from local minima

#### 5.3 Parameter initialization should break symmetry and encourage stability

- We must initialize parameters such that they experience different gradients

- Both uniform and normal distributions are widely used, they do not make much of a difference

- Glorot Initialization: suggests uniformly distributed weights:
  $$
  x \sim U(-\sqrt \frac{6}{m+n}, \sqrt \frac{6}{m+n})
  $$

- When $m=n$, the variance of $x$ is $\frac 1 m$

- This keeps the scale of the variances and $\delta$s (during backprop) at a consistent scale throughout the network

- Kaiming Intialization: suggest normally distributed weights:
  $$
  x \sim N(\sqrt \frac 2 m, -\sqrt \frac 2 m)
  $$

- Variance will go from 1 to 2 after layers

- This will correct for rectification with ReLU nonlinearities

  - the outputs would have variance close to 1

#### 5.4 Stochastic gradient descent makes efficient use of data

-

#### 5.5 Momentum helps find directions with small but consistent gradients

- Momentum
  - $g = \nabla \frac{\partial L}{\partial \theta}$
  - $v = \alpha v - \epsilon g$
  - $\theta \leftarrow \theta + v$
- Nesterov Momentum
  - $\tilde\theta \leftarrow \theta + \alpha v$
  - $g = \nabla \frac{\partial L}{\partial \tilde\theta}$
  - $v = \alpha v - \epsilon g$
  - $\theta \leftarrow \theta + v$

#### 5.6 Adaptive algorithms reduce updates in steep directions

- AdaGrad:
  - $g = \nabla \frac{\partial L}{\partial \theta}$
  - $r \leftarrow r + g \odot g$
  - $\theta \leftarrow \theta + \frac \epsilon {\delta + \sqrt r} \odot g$
- RMSProp:
  - $g = \nabla \frac{\partial L}{\partial \theta}$
  - $r \leftarrow \rho r + (1-\rho)g \odot g$
  - $\theta \leftarrow \theta + \frac \epsilon {\sqrt{\delta + r}} \odot g$
- Adam:
  - $g = \nabla \frac{\partial L}{\partial \theta}$
  - $s \leftarrow \rho_1 s + (1-\rho_1)g$
  - $r \leftarrow \rho_2 r + (1-\rho_2)g \odot g$
  - $\hat s \leftarrow \frac s{1-\rho_1}$
  - $\hat r \leftarrow \frac r{1-\rho_2}$
  - $\theta \leftarrow \theta - \epsilon \frac{\hat s}{\sqrt{\delta + \hat r}}$

#### 5.7 Batch normalization reduces coupling between parameters in different layers

- Following the gradient ignores interactions between parameters in different layers
- The gradient is calculated using forward-propagated activations, considering only what happens if the weights change while their incoming activations stay the same
- This makes the effects of parameter updates less predictable
- It is hard to choose a good learning rate, because the effect of each update depends on previous layers (which also change)
- Batch Normalization gives each neuron’s activation a mean of zero and a standard deviation of one, regardless of its weights

#### 5.8 Hyperparameters can be tuned by grid search, random search, or search algorithms

#### 5.9 Hyperparameters can be manually tuned according to their typical effects
