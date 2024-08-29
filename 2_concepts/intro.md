---
status: backlog
tags:
  - '#ai/dl'
---

# Key Concepts

#### 1.1 The best performing machine learning systems are usually based on deep networks or decision trees

- Deep networks are best for high dimensional, complex data
- Decision trees are best for tabular input
  - Normally trees are combined, i.e. random forests and gradient tree boosting
- No single method works best for every problem

#### 1.2 Deep Networks are Artificial Neural Networks that are large and often, complex

- There is no defined boundary between Deep and Shallow Neural nets; you'll know it when you see it
- Making neural networks deep is useful when the input is not closely related to the output
  - ex. in a melanoma classification network, the value of a pixel has no value, thus multiple layers (of abstraction) are required to abstract from many pixels to gather meaning
- The many layers of a deep network can learn high-level abstractions, ones that are less and less related to pixel colours but more and more relevant to the task
- This can occur within as few as half a dozen layers, but making a network deeper often makes it more accurate

#### 1.3 Important Elements of a Deep Learning System include: inputs, outputs, architecture, loss, parameters, optimization algorithms, hyper-parameters

- Inputs: The information that is fed into the network.
- Outputs: The inference that the network produces given the input
- Architecture: Structural properties of the network
- Loss (or cost): A function that quantifies how bad the network is at producing correct outputs (minimized during training)
- (Learned) parameters: the weights and biases that belong to each neuron
- Optimization algorithm: The algorithm for changing the parameters in order to reduce the loss
- Hyperparameters: network properties are fixed during training, but the best values are unknown in advance
  - ex. learning rate, architectural parameters

#### 1.4 Supervised Learning changes the network parameters so that it emulates examples

- Given pairs of inputs and outputs, supervised learning optimizes the network to calculate the same outputs given the inputs

#### 1.5 An artificial neural network has a simple mathematical relationship with its input

![](Pasted%20image%2020231216180530.png)

- $i$ are inputs to the model
- $w$ are connection weights
- $b$ is the bias of a neuron
- $g$ is a function (usually non-linear)

#### 1.6 Training a network involves setting the weights so that the network does something useful

- We want it to perform a task

#### 1.7 A network's errors need to be summarized with a single character

- We cannot derive the weights and biases analytically
- We must adjust them empirically according to their effect on the network’s performance
- The loss is a measure of this performance; its the difference between the network output and the desired output
- For regression tasks, a typical loss is mean-squared error (MSE)
  $$
  \text{MSE} = \frac 1n \sum^n_{i=1} (o_i -  t_i)^2
  $$
- $i$ is a the index of a labeled input and output pair
- $o_i$ is the network's output given the $i$th labeled input
- $t_i$ is the $i$th target value

#### 1.8 A network's weights and biases are improved via gradient descent

- Further explored [here](4-backprop.md)

#### 1.9 Deep networks must generalize from examples

- GENERALIZATION IS ESSENTIAL:
  - A network’s only value is in its ability to generalize beyond the data points it was trained on
  - The network is not useful for predicting the data points that were used to train it, because these data points are already known
- GENERALIZATION IS NOT GUARANTEED:
  - If there are systematic differences between those inside and outside the training dataset; the model will not generalize

#### 1.10 A deep network should only be applied to the distribution on which it was trained

- Self-explanatory

#### 1.11 A deep network must be trained and validated with with different datasets (OVERFITTING)

- Even when samples are drawn at random from the target distribution, it will still have its own peculiarities that don’t apply to the distribution as a whole
- A model with sufficient capacity will overfit to these peculiarities, in addition to the population trends
- For a given task, there is less overfitting with
  - Larger datasets (but these are expensive)
  - Less complex networks (but these may not be powerful enough to make good predictions)
  - Regularization
- We can measure overfitting using a training and test dataset

#### 1.12 Two datasets may not be enough

- Instead of using just a train and test set, we also use a validation set
- While we optimize the model parameters to the train set and get the accuracy from the test set
