---
tags:
- '#ai/dl'
---

#### 4.0 Gradient Descent Background

- In deep learning, we minimize loss on training data as a proxy for loss calculated on test data
- The gradient of a scalar function of multiple parameters is a vector field that indicates the direction and rate of fastest increase of the function at each point, $\\theta_i$ in the parameter space
- We move the parameters in the opposite direction of the loss function's gradient
- We do not move too far because the gradient is different at each point

#### 4.1 The gradient can be calculated using perturbations, but this is inefficient

![](Pasted%20image%2020231217205357.png)

- This is a simple but inefficient way to estimate gradients
- For each training example, we calculate the derivative of the loss with respect to a certain parameter with two additional evaluations of parts of the network downstream of that parameter
- Approximately like doing the same number of forward passes as there are parameters in the network
- Its inefficiency really only makes it useful for verifying that backpropagation code is correct

#### 4.2 The gradient can be calculated using the chain rule, but this can be inefficient

- So, using the chain rule naively is about as inefficient as using the finite difference approximation

#### 4.3 Backpropagation is an efficient way to use the chain rule in a neural network

#### 4.4 Backpropagation requires storage of activations throughout the network

#### 4.5 Backpropagation is done automatically by deep learning software

#### 4.6 PyTorch creates computational graphs dynamically

-