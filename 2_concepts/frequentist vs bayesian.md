# .
## frequentist

Frequentist $\bf X \sim f({\bf x} | \theta_0)$ where $\theta \in \Theta$ is a random variable

- statisticians start with a prior belief that $\theta \sim \Pi(\theta)$
- then, based on the observed dataset/evidence $x$, the knowledge is updated as the posterior
$$
\Pi(\theta | {\bf x}) = bayes theorem
$$

- if the number of data points go to inf, the pdf mass density converges towards the tru value

## mle
for the dataset x = (x_0... x_n) consider the model X \sim f(x|\theta), \theta \Theta

- likelihodd functionon: L(\theta| x) = f(x|\thetat) -- a function of \theta
    - density is treated as a function of X,
    - when we talk about liklihood were talking about the model parameters
- special case: if $x \sim$ iid,  $f(x| \theta)$. then
    - $L(\theta | x) = \Pi_{i=1}^n f(x_i | \theta)$
- best guess for a;theta from x
- $\hat\theta = \arg\max_{\theta \in \Theta)} L(\theta | x)$