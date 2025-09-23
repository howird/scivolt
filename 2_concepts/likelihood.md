---
status: backlog
tags:
  - "note"
  - "math/prob"
---

# Likelihood

- __Probability__: chance of a particular outcome, given a model of a distribution (parameterized by $\theta$)
    - Given a parameter $\theta$, you compute $P(\text{Data} \mid \theta)$
    - __Usage__: used when the model (including parameters) is known and fixed, and you want to assess the chance of observing certain data

- __Likelihood__: chance that a sampled outcome provides support for a particular values of a parameter in a model
    - After observing the data, the likelihood function is $\mathcal{L}(\theta) = P(\text{Data} \mid \theta)$, viewed as a function of $\theta$
    - __Usage__: Used when the observed data is considered fixed and you treat the model parameters as unknown
    - __Question__: what does observing this particular set of data say about the likely values of the parameters?

>[!note] 
> - the same formula $P(\text{data} \mid \theta)$ can be used in two ways:
>    - when $\theta$ is fixed and you vary the data, it’s probability
>    - when the data is fixed and you vary $\theta$, it’s likelihood.
