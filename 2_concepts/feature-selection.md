---
date: March 18, 2021
status: backlog
tags:
  - '#ai/comp-neuroscience/encoding'
---

# 2.3 Feature Selection

## Discretization

- When we represent a discretized stimulus as a vector, the first axis corresponds to the value of the stimulus at the first time point, the second axis to the value of the stimulus at the second time point, and so on.
- Thus, the dimensionality of the vector space (and all the vectors within it) is the number of time points used to discretize the stimulus
- Note that we often label the axes by their corresponding times, even though the elements of the stimulus vector have the same units as the y-axis of the original stimulus waveform

## Dimensionality Reduction

- The dimensionality of a stimulus is just the number of numbers you need to describe it
- If you know nothing at all about the patterns in your stimulus, then you’d need a long list of numbers to describe it, one for each point in time at which the stimulus was sampled.
- On the other hand, if you knew that your stimulus was always approximately a multiple of some function f(t), then the only number you would need would be the scaling factor, and you’d have a pretty good description of the stimulus.
- The goal of dimensionality reduction is to try to find a small set of numbers such that knowing the values of those numbers for a given stimulus describes it as best as possible
- Sometimes those numbers will correspond to scaling factors (like in the above example), but sometimes they will correspond to things more complex.
- For the purposes of illustration, we often draw high-dimensional points in a 2D or 3D space

## Determining linear features from white noise

- The spike-triggered ensemble, or spike-conditioned distribution, is just the set of all the stimuli that trigger a spike

![](2.3.1.png#center){ width=70% }

- Each set of stimuli can be interpreted geometrically as a set of points which form a gaussian distribution in high dimensional space, with each time point in the stimuli having an axis

- If we were to take any vector and project all the points onto that vector, the distribution would again be Gaussian

![](2.3.2.png#center){ width=70% }

- The goal is to find an efficient and faithful representation of the stimuli in this set

- To do this we can find the average stimulus (each blue stimuli is the stimuli which produced a spike)

- The set of points which trigger spikes, called the spike conditional distributions will form some structure, however unlike the above graph, the structure would be visible

- in order to see this structure in high dimensional space, we must choose the correct coordinate axis

  - find the Spike Triggered Average (green)
  - Project all the other spike triggered points onto the STA's vector
  - All the other spike triggered stimuli should form a gaussian distribution projected on that vector

## Determining Non-Linear Input/Output Function

- We have discussed how to estimate the linear filter with a Spike Triggered Average $P(\text{spike } | \text{ stimulus})$ , next. we want to find the input/output function

![](2.3.3.png#center){ width=100% }

$\text{The input/output function is: (where s}_1: \text{is the STA )}$

$$
P(\text{spike } | \text{ stimulus}) \rightarrow P(\text{spike } | \text{ s}_1) , \text{where s}_1: \text{is the STA}
$$

$\text{This can be found from the data using Bayes' Rule:}$

$$
P(\text{spike } | \text{ s}_1) = \frac{ P(\text{ s}_1 | \text{ spike})P(\text{spike}) } {P(\text{s}_1)}
$$

![](2.3.4.png#center){ width=100% }

![](2.3.5.png#center){ width=70% }

- Our model can be made even better by allowing the neuron to have multiple linear filters

![](2.3.6.png#center){ width=100% }

## Principal component analysis: spike sorting

- The spike-triggered average gives us a simple view of the stimuli that lead up to a spike, but because of its simplicity it cannot capture some of the interesting dynamics that can occur

![](2.3.5.png#center){ width=100% }

- In this case, if a cell responds to both positive/negative changes and negative/positive changes, the spike-triggering stimuli will average to zero, making the spike-triggered average look like a flat line
- That does not give us much useful description! Principal component analysis can help is pull out the right number of dimensions we need to describe the stimulus features the neuron is looking for.
- If PCA works well for describing the patterns in your dataset, then the following should be true:
  - Given n principal components $f_1(t),  f_2(t), ... ,  f_n(t)$ of your dataset, any arbitrary stimulus $s(t)$ in the dataset should be very well represented as a weighted sum of the principal components added to the average stimulus $s_0(t)$

## Finding interesting features in the retina

- PCA is a dimensionality reduction technique. Knowing the principal components tells us how to write each stimulus as just a small set of numbers
- If there are only two relevant principal components, then each stimulus can be written as two numbers.
- Each stimulus can therefore be plotted as a point in a 2D space. In the retina example, doing this clearly shows separation between the two types of stimuli that drove the cell
