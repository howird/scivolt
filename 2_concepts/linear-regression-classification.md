---
status: backlog
tags:
  - '#type/theory'
  - '#statistics/regression'
  - '#ai/dl'
---

#### 2.1 Regression and classification are prediction of continuous and categorical values, respectively

- Regression: given a vector $x$ what is the associated vector $y$
- Classification: given a vector $x$ to which group does it belong

#### 2.2 Linear regression and classification use linear functions of the inputs

- In Linear Regression:

  - the prediction, $\\hat y$, is a linear (or affine) function of the inputs, $x$
    $$
    \\hat y = \\boldsymbol{w}^T\\boldsymbol{x}+b
    $$

- In Linear Classification:

  - the prediction, $\\hat y$, uses a linear decision boundary
    $$
    \\hat y = \\begin{cases}
    0 &\\text{if } \\boldsymbol{w}^T\\boldsymbol{x}+b \< 0 \\
    1 &\\text{if } \\boldsymbol{w}^T\\boldsymbol{x}+b \\ge 0
    \\end{cases}
    $$

- If $x$ is $D$-dimensional, then the decision is based on

- Two-dimensional $x$ boundary is a (D-1)-dimensional hyperplane

- Non-linear basis functions allow approximations and decision boundaries that are not linear

  - replace $\\boldsymbol x$ with $\\boldsymbol{f(x)}$

- linear methods work well with input dimensions

#### 2.3 Regression and classification are supervised learning problems

- Learning a function that approximates examples of input-output pairs
- The function has a generic form with parameters $\\theta$
- The differences between predictions $\\hat y$ and target values $y$ are summarized with a loss function

#### 2.4 Linear regression typically minimizes squared-error loss

- Sum squared error (SSE) is:
  $$
  L = \\sum\_{i=1}^N (\\hat y_i - y_i)^2
  $$
- Minimizing this is the same as minimizing the mean-squared error
- SSE in matrix form is (where we merge the bias term into $\\boldsymbol w$):
  $$
  \\displaylines{

L = ||X\\boldsymbol{w}-\\boldsymbol{y}||^2 \\
L = (X\\boldsymbol{w}-\\boldsymbol{y})^T(X\\boldsymbol{w}-\\boldsymbol{y}) \\
L = \\boldsymbol{w}^TX^TX\\boldsymbol{w} - X^T\\boldsymbol{w}^T\\boldsymbol{y} - \\boldsymbol{y}^TX\\boldsymbol{w} + \\boldsymbol{y}^T\\boldsymbol{y} \\
\\frac{\\partial L}{\\partial \\boldsymbol w} = 2X^TX\\boldsymbol{w} - 2X^T\\boldsymbol{y} \\
\\frac{\\partial L}{\\partial \\boldsymbol w} = 0 \\
0 = X^TX\\boldsymbol{w} - X^T\\boldsymbol{y} \\
\\boldsymbol{w}^\* = (X^TX)^{-1}X^T\\boldsymbol{y} \\
}
$$

#### 2.5 One can have too many or too few basis functions

![](Pasted%20image%2020231217134822.png)

- Above we are trying to fit a polynomial regression model to a sin function
- These low-order polynomials are not flexible enough to approximate it
  - This is underfitting
- Overfitting occurs when the model is too flexible, by fitting itself to the gaussian noise, the model will be unable to generalize
  ![](Pasted%20image%2020231217135040.png)

#### 2.6 One can have too many or too few inputs

- The model will not perform well if too little inputs are given
  - because the input will not have enough information, thus differing inputs with similar targets will confuse the model
- The model will not generalize well if some inputs have a weak relationship with the output
  - because the sample correlation of two uncorrelated random variables (e.g., target and irrelevant input) is not generally zero

#### 2.7 Ridge regression reduces weights to reduce overfitting

- Weights typically have more magnitude when there are more basis functions
- For polynomial regression, as the order increases, so does the magnitude of the weights
- This can be rectified by penalizing large weights within the loss function:
  $$
  \\displaylines{
  \\tilde L = \\sum\_{i=0}^N \\overbrace{(\\hat y_i - y_i)^2}^\\text{prediction errors are bad} + \\overbrace{\\lambda \\boldsymbol w^T \\boldsymbol w}^\\text{large weights are bad} \\
  \\implies \\boldsymbol{w}^\* = (\\lambda I + X^TX)^{-1}X^T\\boldsymbol{y} \\
  }
  $$

#### 2.8 A linear discriminant uses a linear boundary to separate examples into different categories

- $\\boldsymbol{w}$ determines the orientation of the decision surface, and $b$ determines its distance from the origin
- Ways to find a linear discriminant
  - Logistic regression
  - Perceptron learning rule

#### 2.9 Perceptrons adjust the boundary to correct classification errors

- For the perceptron binary classification task, we use target values of:
  $$
  y\\in {-1, 1}
  $$
- The Perceptron function is:
  $$
  \\displaylines{
  \\hat y = f (\\boldsymbol{w}^T\\boldsymbol{x}) \\
  \\text{where: }
  f(a) = \\begin{cases}
  -1 &\\text{if } a \< 0 \\
  1 &\\text{if } a \\ge 0
  \\end{cases}
  }
  $$
- The activation function is a step function from $-1 \\rightarrow 1$ at $x=0$
- To optimize the weights of the perceptron, we use a modified gradient descent that uses a single example at a time
- Loop through examples and update $\\boldsymbol{w}$ to reduce error on the $n$th misclassified example:
  $$
  \\boldsymbol{w}^{(\\tau+1)} = \\boldsymbol{w}^\\tau - \\eta \\nabla L (\\boldsymbol{w}) = \\boldsymbol{w}^\\tau + \\eta\\boldsymbol{x}\_n y_n
  $$
- where $\\tau$ is the iteration number, and $\\eta$ is the learning rate
  - learning rate is not too important here
- this method is not good at separating linear separable examples

#### 2.10 Logistic regression categorizes inputs probabilistically

- Logistic regression function:
  $$
  p(x) = \\frac 1{1+\\exp(-(\\boldsymbol{w}^T\\boldsymbol{x}+b))}
  $$
- This isn’t a classifier on its own, but it just needs a threshold such as $p(x) = 0.5$
- The $\\boldsymbol{w}^T\\boldsymbol{x}+b$ term is called the log-odds and the unit of this term is a "logit"
- The loss function which is used to iteratively optimize this function is:
  $$
  \\text{where: }
  L_k = \\begin{cases}
  -\\ln(p(\\boldsymbol{x}\_k)) &\\text{if } y_k = 1 \\
  -\\ln(1-p(\\boldsymbol{x}\_k)) &\\text{if } y_k = 0
  \\end{cases}
  $$

#### 2.11 Linear classifiers can implement Boolean logic, except for XOR

- A linear model can only distinguish linearly separable groups of potential inputs
  ![](Pasted%20image%2020231217153115.png)
- cannot do `XOR`

#### 2.12 If there are multiple categories, it’s best to make a predictor for each and choose the one with the highest pre-threshold output

- Use a separate binary member/non-member classifier for each category and hope only one is positive
  - fails when multiple are positive
- Use a separate classifier to distinguish between each pair of possibilities and hope one is positive more than the others
  - have to train $n^2$ classifiers where $n$ is the number of classes
- Learn a binary member/non-member classifier for each category and adopt the category of the classifier with the highest output
  - This approach does not produce ambiguous regions (except with exactly equal outputs)

#### 2.13 The number of basis functions needed to tile a space depends exponentially on the dimension of the space

- Using linear methods for nonlinear functions of a high-dimensional space would require tiling the space with basis functions
- This is not practical because the number of fixed basis functions needed grows exponentially with the dimension
- However, we do not care about the entire space. ex:
  - we can produce images by sampling random noise and they would mean nothing
  - actual images take up very specific domains of the feature space
- Multi-layer neural networks take advantage of this by adapting basis functions so that:
  - Regions/directions of variation correspond to regions/directions over which input typically varies
