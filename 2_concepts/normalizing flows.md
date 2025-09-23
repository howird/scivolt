# Normalizing Flows

https://blog.evjang.com/2018/01/nf1.html?m=1
https://blog.evjang.com/2018/01/nf2.html?m=1

Normalizing Flows are density estimators based on the substitution formula for multivariate probability distributions. They can be used in two ways: backward (i.e. used for computing the likelihood of a sample) and forward (i.e. used for sampling from the modeled distribution). Most of the works are on tractable normalizing flows, that are a special kind of normalizing flows that guarantee computational tractability of inference and/or sampling from the modeled distribution. There are a LOT of normalizing flows based models, each of them having some advantages/disadvantages. For more information read the papers about RealNVP, MADE, MAF and NADE.

Eli5: Normalizing flows turn simple distributions, into complex distributions by twisting and turning parameters around. By inverting them, you can sample fast, if not, you can measure the probability of samples fast. Some normalizing flows allow for fast sampling and probability.

The first 3 answers have already given a good answer of what normalizing flow is. Unto the applications, recall that in VAE, we approximate the posterior distribution p(theta|X) as a Gaussian, just because it is easier to work with Gaussian, BUT we know that Gaussian is too simple to model the true posterior, and so, instead of Gaussian, we use the "more flexible" normalizing flow in approximating the true posterior.

