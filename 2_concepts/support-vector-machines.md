---
date: June 9, 2022
status: backlog
tags:
  - '#ai/ml'
  - '#application/classification'
---

# Support Vector Machines

## Basic SVM Formulation

### Formulating a Decision Rule

- Suppose we have a dataset with positive and negative classes:

![](learning-wiki/machine-learning/img/4.1.1.png#center){width=60%}

- We can draw an arbitrary decision boundary:

![](4.1.2.png#center){width=60%}

- In order to classify new points using this decision boundary, we define a vector, $\overrightarrow w$, that is perpendicular to the decision boundary:

![](4.1.3.png#center){width=60%}

- When classifying a given data point, $u$, we can interpret it as a vector, $\overrightarrow u$, and take the dot product between $\overrightarrow w$ and $\overrightarrow u$,  ($\overrightarrow u \cdot \overrightarrow w$)
- If this dot product is greater than a constant, $c$, then the data point, $u$ can be classified as positive:

$$
\overrightarrow w \cdot \overrightarrow u \ge c
$$

- For future convenience, we can adjust this equation by replacing $c$ with a constant, $b$, where $b = -c$; giving us:

$$
\overrightarrow w \cdot \overrightarrow u + b \ge 0 \tag{1}
$$

- We have not defined enough constraints in order to calculate the constant, $b$, or the magnitude of $w$; this means we will have to formulate some constraints

### Calculate an Equation for the Margins

- Suppose we are given a data point that we know is either negative or positive, we can create constraints where:

$$
\overrightarrow w \cdot \overrightarrow x_+ + b \ge 1
$$

$$
\overrightarrow w \cdot \overrightarrow x_- + b \le -1
$$

- For convenience, we can define a variable, $y_i$, such that $y_i = +1$ for positive samples and $y_i = -1$ for negative samples in order to combine the above equations:

$$
y_i (\overrightarrow w \cdot \overrightarrow x_i + b) \ge 1 \implies y_i (\overrightarrow w \cdot \overrightarrow x_i + b) -1 \ge 0
$$

- Notice, when $y_i = -1$ and we move it to the other side, the $\ge$ flips and $1\rightarrow-1$

- Now that we have this inequality, we notice that when:

$$
y_i (\overrightarrow w \cdot \overrightarrow x_i + b) -1 = 0 \tag{2}
$$

- We get an equation for our margins

![](4.1.2.png#center){width=60%}

### Calculating the Width of our Decision Boundary/Margins

- Looking back to our goal of creating a decision boundary, it is clear that we want a boundary that is as wide as possible
- To do so, we must be able to calculate its width
- In order to determine the distance between our two margins, we first think of two arbitrary vectors $\overrightarrow{x_+}$ and $\overrightarrow{x_-}$ that lie on the positive and negative margins, respectively:

![](4.1.4.png#center){width=60%}

- We can calculate the vector going from $\overrightarrow{x_-}$ to $\overrightarrow{x_+}$ as $\overrightarrow{x_+} - \overrightarrow{x_-}$
- Given the unit vector $\hat w$ that is perpendicular to the decision boundary, the width between the margins is:

$$
\text{width} = \hat w \cdot (\overrightarrow{x_+} - \overrightarrow{x_-})
$$

$$
\text{where: } \hat w = \frac{\overrightarrow w}{||w||}
$$

![](4.1.5.png#center){width=60%}

- In order to solve for width, we can take equation $(2)$ and solve for $x_+$ and $x_-$ to get:

$$
x_+ = \frac{1 - b}{\overrightarrow w}, x_- = \frac{1 + b}{\overrightarrow w}
$$

- When subbing this back into the width equation we get:

$$
\text{width} = \hat w \cdot (\frac{2}{\overrightarrow w}) = \frac{\overrightarrow w}{||w||} \cdot \frac{2}{\overrightarrow w} = \frac{2}{||w||}
$$

- Thus, we want to maximize this width term: $\frac{2}{||w||}$

  - This is equivalent to maximizing $\frac{1}{||w||}$
  - Or minimizing $||w||$
  - Or minimizing $\frac12||w||^2$

- Thus we want to find:

$$
\operatorname\*{argmin}_w \frac12||w||^2 \tag{3}
$$

### Optimization

- To do so, we use Lagrange Multipliers:

$$
L = \frac12||w||^2 - \sum_i\alpha_i\[y_i (\overrightarrow w \cdot \overrightarrow x_i + b) -1\]
$$

- We try to find the extremum with respect to $w$:

$$
\frac{\partial L}{\partial w} = 0
$$

$$
\frac{\partial L}{\partial w} = w- \sum_i\alpha_iy_ix_i
$$

$$
w = \sum_i\alpha_iy_ix_i \tag{4}
$$

- As well as $b$:

$$
\frac{\partial L}{\partial b} = 0
$$

$$
\frac{\partial L}{\partial b} = \sum_i\alpha_iy_i
$$

$$
0 = \sum_i\alpha_iy_i
$$

- From this, we notice that $w$ is simply a linear sum of the samples!

- On a sidenote, we can plug our two equations back into the original equation $L$:

$$
L = \frac12||w||^2 - \sum_i\alpha_i\[y_i (\overrightarrow w \cdot \overrightarrow x_i + b) -1\]
$$

$$
L = \frac12(\sum_i\alpha_iy_ix_i)(\sum_j\alpha_jy_jx_j) - \sum_i\alpha_iy_i\overrightarrow x_i (\sum_j\alpha_jy_jx_j)- b\sum_i\alpha_iy_i + \sum_i\alpha_i
$$

$$
\text{since: } \sum_i\alpha_iy_i = 0
$$

$$
L = \frac12(\sum_i\alpha_iy_ix_i)(\sum_j\alpha_jy_jx_j) - \sum_i\alpha_iy_i\overrightarrow x_i (\sum_j\alpha_jy_jx_j) + \sum_i\alpha_i
$$

$$
L = \sum_i\alpha_i - \frac12(\sum_i\alpha_iy_ix_i)(\sum_j\alpha_jy_jx_j)
$$

$$
L = \sum_i\alpha_i - \frac12\sum_i\sum_j\alpha_iy_i\alpha_jy_j(x_i \cdot x_j) \tag{5}
$$

- In doing so, we notice that the optimization process only depends on the summation of dot products between pairs of samples!
- This means that the optimization of our loss, $L$, is easy to compute

## Bringing all of this Together

- To recap of all the work we have done, we first have a "Decision Rule"
- This is the computation we perform to check if a given data point, $\overrightarrow u$, should be classified as positive

$$
\overrightarrow w \cdot \overrightarrow u + b \ge 0 \tag{1}
$$

- Because $\overrightarrow w$ and $b$ are parameters of the decision boundary which defines our "Decision Rule", we must optimize them in some manner
- We do so by defining two symmetrical margins parallel to our decision boundary, that are still able to separate our two classes, the equations for which are:

$$
y_i (\overrightarrow w \cdot \overrightarrow u + b) -1 = 0 \tag{2}
$$

![](4.1.3.png#center){width=60%}

- We want to maximize the distance between these margins and our decision boundary
  - Using equations $(1)$ and $(2)$, we find that we can maximize the width of the margins with:

$$
\operatorname\*{argmin}_w \frac12||w||^2 \tag{3}
$$

- We optimize this using Lagrange Multipliers and get:

$$
w = \sum_i\alpha_iy_ix_i \tag{4}
$$

- Plugging $\text{(4)}$ back into our decision rule, $\text{(3)}$, we get:

$$
\sum_i\alpha_iy_i(x_i \cdot \overrightarrow u) + b \ge 0 \tag{6}
$$

- We notice that there is a total dependence of the decision rule on the dot product between the sample vectors, $x_i$, and our unknown, $u$

## Key Takeaways

- We can produce an optimal decision line to perform classification
- This classification is performed by computing the decision rule, see $(\text{6})$
- The decision rule is simply a linear combination of dot products between the samples and the unknown, see $(\text{4})$
- While we do not discuss this here, the optimization of SVMs has been proven to be in a purely __convex__ space
  - Meaning, SVMs will never get stuck in local maxima
  - This is an incredible advantage that other methods such as neural networks do not have
- However, simple decision boundaries do not work if the classes are not linearly separable
  - This can be solved by transforming the points into a space in which they __are__ linearly separable
  - A method to solve this problem will be discussed in the next section

## The Kernel Function

- In order to solve the problem of linear inseparability, we can notice that all the operations that are required in our optimization and classification process involve a dot product between two points in our sample space
- Thus, we can define a function, $\phi(\overrightarrow x)$, to transform these points into a space that makes them linearly separable before taking the dot product
- So, optimization would look like:

$$
L = \sum_i\alpha_i - \frac12\sum_i\sum_j\alpha_iy_i\alpha_jy_j(\phi(x_i) \cdot \phi(x_j)) \tag5
$$

- and classification would look like:

$$
\sum_i\alpha_iy_i(\phi(x_i) \cdot \phi(\overrightarrow u)) + b \ge 0 \tag6
$$

- Adding on to this, we could even define a function, $K$, which returns the dot product between two points in another space:

$$
K(\overrightarrow x_i, \overrightarrow x_j)=\phi(x_i) \cdot \phi(x_j)
$$

- This way, we do not even have to know the transformation to the other space, this is our __Kernel Function__:
- So, optimization would look like:

$$
L = \sum_i\alpha_i - \frac12\sum_i\sum_j\alpha_iy_i\alpha_jy_jK(\overrightarrow x_i, \overrightarrow x_j) \tag5
$$

- and classification would look like:

$$
\sum_i\alpha_iy_iK(\overrightarrow x_i, \overrightarrow x_j) + b \ge 0 \tag6
$$

### Polynomial kernel:

$$
K(\overrightarrow x_i, \overrightarrow x_j) = (x_i \cdot x_j + r)^n
$$

### Exponential/Radial Basis Kernel

$$
K(\overrightarrow x_i, \overrightarrow x_j) = \exp(-\frac{x_i - x_j}{\sigma})
$$

## Resources

- Here are two great resources that I used to learn this topic
- The first helps provides a foundational understanding of math, and the second provides a high level overview
- I would suggest watching in this order as the MIT lecture's content will fill in the technical gaps that are omitted by the StatQuest for simplicity's sake

<iframe width="100%" height="310px" src="https://www.youtube.com/embed/_PwhiWxHK8o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="100%" height="310px" src="https://www.youtube.com/embed/videoseries?list=PLblh5JKOoLUL3IJ4-yor0HzkqDQ3JmJkc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
