---
date: April 26, 2021
status: backlog
tags:
  - '#ai/comp-neuroscience/encoding'
---

# 2.4 Variability

## The Gaussian

$$
p(x) = Ae^{ -\frac12{( x - \mu/\sigma)^2}}
$$

![](2.4.1.png#center){ width=30% }

![](2.4.2.png#center){ width=70% }

- $s_f$ meaning the stimulus projected on a filter, $f$
- Instead of using PCA to find filter $f$, we could simply look for a choice of f that would produce a $P(\text{s}_f | \text{ spike})$ that is most different
- We can us the Kullback-Leibler divergence to do this:

$$
D_{KL}(P(s), Q(s))=\int ds P(s)\log_2(P(s)/ Q(s))\D_{KL}(P(\text{s}_f | \text{ spike}), P(\text{s}_f))
$$

## Maximally-Informative Dimensions

![](2.4.3.png#center){ width=70% }

- Give us a way of seeking filters that maximize the discriminability of the spike conditioned distribution and the prior
- It does not require a specific structure for the distributions, such as white noise from a Gaussian distribution and thus models can be derived from natural stimuli

## Summary

- We now know how to build a model with:
  - A single filter, by taking the spike triggered average
  - We could generalize that to multiple filters using PCA
  - We introduced an information theoretic method that uses the whole distribution of stimuli to compute and optimal filter and this method does not require for Gaussian stimuli.

## Binomial Spiking

- The next issue to deal with is to generate the arrival time of spikes $p(t),$ from  $r(t)$
- Over a time period $t$ which is divided into $n$ time bins:
  - Each time bin is $\Delta t$ long where $\Delta t= \frac T n$
  - Over $t$ the probability that $k$ spikes occur is $P_n\[k\] = \binom nk p^k(1-p)^k$
  - The mean or average number of spikes is $<k> = np$
  - The variance is $Var(k) = np(1-p)$

## Poisson Spiking

- When there are many time bins and the probability of a spike in any bend becomes very small, we want to use a different form for the distribution
- We use the Poisson Distribution which is the Binomial with $n \rightarrow \infin \text{ and } p \rightarrow 0$
  - Thus the Poisson Distribution can be used to provide a reasonable approx. to the binomial if $n$ is large and $p$ is small

  - Distribution: $P_T\[k\] = (rT)^k \exp(-rT)/k!$ where $r = \frac {P}{\Delta t}$

  - Mean: $<k>= rT$

  - Variance: $Var(k)= rT$

  - Fano Factor: $F = \frac {\sigma^2}{\mu} = 1$, a distribution is Poisson if $F = 1$

  - The intervals between successive spikes have an exponential distribution:

    $P(T)= r \exp(-rT)$

    - The negative exponential means that a consecutive spike is likely to occur soon after the first spike
    - However there a physical limitations as neurons take time to regenerate their negative potential (the refractory period) so no spikes occur within 10 milliseconds of the first spike

## The Generalized Linearized Model

- All of our additions to the model can be put together in a model called a GLM (Pillow et Al '08)

![](2.4.4.png#center){ width=70% }

- To summarize:
  - First, the stimulus is passed through a linear filter (derived from PCA) and then processed by a non-linearity function
    - An exponential function is often used at the non-linearity function as to allow for the entire system to be solved for, mathematically, much more easily
  - The output of the non-linearity is then passed into the Poisson Spike Generator
  - If a spike is generated, a post spike filter is injected into the non-linearity functions input as to account for the refractory period
    - The filter first draws the neuron away from spiking, with a big initial dip,
    - Then becomes positive to promote spiking at some time after the previous spike,this models a neuron that has a slight tendency to fire periodically
  - This model has also added positive filters that are injected when a coupled (nearby) neuron  fires

# Evaluating our Model

- We can use this Poisson nature of firing to test whether we have captured everything that we can about the inputs in our model
- Let's say we have a model like the GLM, where the output depends on many influences, such as the stimulus, the history of firing in the neuron, as well as other neurons
- Then we can our output spike intervals and scale them by the firing rate that's predicted by the model
- So we take these intervals times between successive spikes, we scale them by the firing rate that our model predicted given all the interactions that, that we've incorporated.

If this predicted rate does truly account for all the influences on the firing, even ones due to previous spiking, then these new scaled intervals should be distributed like a pure Poisson process, with an effective rate of one, that is as a single clean exponential. So this is called the Time-rescaling theorem and it's used as a way to test how well one has done in capturing all the influences on spiking with ones models.

- A Poisson process with a time varying rate $r(t)$ is completely characterized by the rate $r(t)$ : if you know $r(t)$  then you know all of the statistics of the process
  - A given spike-train might have a very high probability under a Poisson process with one $r(t)$ and a very low probability under a Poisson process with another $r(t)$
  - A simple linear-nonlinear model says that $r(t)$ depends only on the stimulus
  - The GLM generalizes this by saying that $r(t)$ depends on the activity of the neuron as well
- Mathematically, the goal of these models is to use your data to figure out the $r(t)$ (and thus the associated Poisson process) such that the observed spike-train has the highest probability
  - A linear non-linear model only looks at the stimulus to figure out this $r(t)$, whereas a GLM looks at both the stimulus and the spike train
