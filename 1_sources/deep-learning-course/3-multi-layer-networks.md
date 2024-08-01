#### 3.1 Multi-layer feed-forward networks make a series of simple but unintuitive calculations
![](Pasted%20image%2020231217155646.png)
- The overall architecture and functionality is intuitive
- What each neuron is technically doing is intuitive
- BUT, the information each neuron represents and how it relates network function is NOT INTUITIVE, we do not know what these mean..

#### 3.2 Multi-layer networks are composite functions
![](Pasted%20image%2020231217155911.png)

#### 3.3 Multi-layer networks break the curse of dimensionality
- Recall from [2.13](2-linear-regression-classification.md) that:
	- Multi-layer neural networks take advantage of this by adapting basis functions so that:
		- Regions/directions of variation correspond to regions/directions over which input typically varies
- Fewer basis functions are needed if they are adaptive
	- Different parts of the surface can overlap in lower-dimensional projections, so all the dimensions should be considered

#### 3.4 A two layer function can closely approximate any continuous function on a bounded domain
- In principle, a network with a single hidden layer can approximate any continuous function with arbitrary precision, however the number of hidden units required may be impractical
- Two-layer networks can approximate any function over a bounded domain to
arbitrary precision
- Large hidden layer sizes increase risk of overfitting
- Deeper networks can represent some kinds of functions more efficiently, particularly functions that are compositions of simpler functions

#### 3.5 Networks with different weight matrices can perform identical mapping
- This means that there isn’t a single global minimum of the loss
- For any minimum, there are many equivalent minima

#### 3.6 Classification and Regression employ different output and loss functions
- We want to perform maximum likelihood estimation of the network parameters, $\theta$
	- we adjust the parameters to maximize the probability of the target given the input and the parameters
$$
\displaylines{

p(\boldsymbol{y|\theta})=\prod_{n=1}^Np(y_n|\boldsymbol{\theta}) \\

L(\boldsymbol{\theta}) = -\ln(p(\boldsymbol{y|\theta}))=\sum_{n=1}^N-\ln(p(y_n|\boldsymbol{\theta}))

}
$$

- The negative log-likelihood is:
$$
\displaylines{

p(\boldsymbol{y|\theta})=\prod_{n=1}^N \hat y ^{y_n} (1-\hat y_n)^{1-y_n} \\

L(\boldsymbol{\theta}) = -\ln(p(\boldsymbol{y|\theta}))=-\sum_{n=1}^N y_n\ln(\hat y) + (1-y_n)\ln(1-\hat y_n)

}
$$
![](Pasted%20image%2020231217204226.png)

#### 3.7 Multi-layer networks are also called multi-layer perceptrons, but are not perceptrons
- Artificial neural networks with at least two layers are often called multi-layer perceptrons
- However, such networks
	- Do not typically use the perceptron activation function
	- Do not typically use the perceptron learning rule
	- Can perform regression as well as classifications
