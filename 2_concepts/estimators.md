---
tags:
  - note
  - math/stats
status: todo
---
# Estimators in Statistics: Bias, Variance, Mean Squared Error (MSE), and Asymptotic Properties

## Introduction to Estimators

In statistics, an estimator is a rule or a function that provides an estimate of an unknown population parameter based on sample data. Estimators are fundamental tools for statistical inference, allowing us to make predictions or decisions about population characteristics using observed data.

## Key Properties of Estimators

### 1. Bias

Bias measures the accuracy of an estimator in terms of its expected value relative to the true value of the parameter being estimated.

- Definition: The bias of an estimator $\hat{\theta}$ for a parameter $\theta$ is defined as:
  $$
  \text{Bias}(\hat{\theta}) = \mathbb{E}[\hat{\theta}] - \theta
  $$
- Unbiased Estimator: If $\text{Bias}(\hat{\theta}) = 0$, the estimator is said to be unbiased
- Interpretation: A biased estimator systematically overestimates or underestimates the true parameter

Example: The sample mean $\bar{X}$ is an unbiased estimator of the population mean $\mu$.

### 2. Variance

Variance quantifies the spread or variability of the estimator around its expected value.

- Definition: The variance of an estimator $\hat{\theta}$ is: $\text{Var}(\hat{\theta}) = \mathbb{E}(\hat{\theta} - \mathbb{E}\hat{\theta})^2$
- Interpretation: A lower variance indicates that the estimator produces estimates that are consistently close to its expected value.

### 3. Mean Squared Error (MSE)

Mean Squared Error combines both the bias and the variance of an estimator to provide a comprehensive measure of estimator quality.

- Definition: The MSE of an estimator $\hat{\theta}$ is: $\text{MSE}(\hat{\theta}) = \mathbb{E}(\hat{\theta} - \theta)^2$

- Relation to Bias and Variance:
  $$
  \text{MSE}(\hat{\theta}) = (\text{Bias}(\hat{\theta}))^2 + \text{Var}(\hat{\theta})
  $$
- Interpretation: MSE assesses both the accuracy (via bias) and precision (via variance) of an estimator.

### 4. Bias-Variance Trade-off

- Concept: Improving an estimator's bias often increases its variance, and vice versa.
- Goal: Select an estimator that minimizes MSE by balancing bias and variance appropriately.

Illustration:

- High Bias, Low Variance: Estimates are consistently wrong in the same direction.
- Low Bias, High Variance: Estimates vary widely but average out to the true parameter.

## Asymptotic Properties of Estimators

As sample size $n$ increases, estimators often exhibit certain desirable properties known as asymptotic properties.

### 1. Consistency

- Definition: An estimator $\hat{\theta}_n$ is **consistent** if it converges in probability to the true parameter $\theta$ as $n \to \infty$:
  $$
  \hat{\theta}\_n \xrightarrow{P} \theta
  $$
- Implication: The estimator becomes increasingly accurate with larger samples.

### 2. Asymptotic Normality

- Definition: An estimator is asymptotically normal if the distribution of a properly normalized version of the estimator converges to a normal distribution as $n \to \infty$:
  $$
  \sqrt{n}(\hat{\theta}\_n - \theta) \xrightarrow{d} N(0, \sigma^2)
  $$
- Usage: Facilitates hypothesis testing and confidence interval construction for large samples.

### 3. Asymptotic Efficiency

- Definition: Among a class of consistent estimators, an estimator is asymptotically efficient if it achieves the lowest possible asymptotic variance.
- Benchmark: The Cramér-Rao Lower Bound provides a theoretical minimum variance for unbiased estimators.

## Practical Considerations

- Estimator Selection: Choose estimators based on the context, balancing bias and variance to minimize MSE.
- Sample Size: Larger samples generally improve estimator properties, making asymptotic approximations more accurate.
- Model Assumptions: Ensure that the assumptions underlying the estimators are met in the data.

## Summary

- Bias measures the accuracy of an estimator.
- Variance measures the precision of an estimator.
- MSE combines bias and variance to evaluate estimator quality.
- Asymptotic properties provide insights into estimator behavior with large samples.

Understanding these concepts is crucial for effective statistical analysis and making reliable inferences from data.

