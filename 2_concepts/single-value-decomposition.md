---
tags:
  - "#math/lin-alg"
aliases:
  - SVD
---
# Singular Value Decomposition

- a fundamental matrix factorization technique 
- geometrically intuitive way to decompose any rectangular matrix into a set of orthogonal transformations and a diagonal matrix

### The Mathematics of SVD

For any given matrix $A$ of dimensions $m \times n$, its Singular Value Decomposition is given by:

$$
A = U \Sigma V^\top
$$

- where:
    - $U\in \mathbb R ^{m\times m}$ orthogonal matrix, whose columns are the _left-singular vectors_
    - $\Sigma \in \mathbb R^{m\times n}$ rectangular diagonal matrix, containing the _singular values_ ($\sigma_i$​) of A in descending order
        - These values are the non-negative square roots of the eigenvalues of $A^\top A$ (and $AA^\top$)
    - $V^\top$ is the transpose of an $n\times n$ orthogonal matrix $V$, whose columns are the _right-singular vectors_
        - These vectors form an orthonormal basis for the row space of A

- Geometrically, SVD states that any linear transformation represented by the matrix $A$ can be broken down into three fundamental operations:
    - a rotation (and/or reflection) in the domain space ($V^\top$)
    - a scaling along the axes ($\Sigma$)
    - another rotation (and/or reflection) in the codomain space ($U$)

- The singular values in $\Sigma$ represent the magnitude of this scaling in each orthogonal direction

---

### Applications in Probability and Statistics

The power of SVD in probability and statistics lies in its ability to reveal the underlying structure of a dataset. When a dataset is represented as a matrix, where rows might be observations and columns are random variables, SVD becomes a powerful analytical tool.

#### **Principal Component Analysis (PCA)**

One of the most significant applications of SVD in statistics is its direct relationship with Principal Component Analysis (PCA).8 For a centered data matrix $X$ (where the mean of each column is zero), the covariance matrix is proportional to $X^\top X$. The principal components of the data are the eigenvectors of this covariance matrix.

By performing SVD on the data matrix $X=U\Sigma V^\top$, we find that the columns of $V$ (the right-singular vectors) are precisely the principal components of the data
The squared singular values in $\Sigma$ are proportional to the eigenvalues of the covariance matrix, representing the variance captured by each principal component
This allows for a dimensionality reduction of the data by projecting it onto the principal components corresponding to the largest singular values, thereby retaining the most significant variance in the data with fewer dimensions.

#### **Low-Rank Approximation**

SVD provides the best low-rank approximation of a matrix. The Eckart-Young-Mirsky theorem states that the optimal rank-k approximation of a matrix A (in the sense of minimizing the Frobenius norm of the difference) is obtained by truncating the SVD:

$$
A_k​=U_k​\Sigma_k​V_k^\top
$$​

- Here, $U_k$​ and $V_k​$ are the first $k$ columns of $U$ and $V$ respectively, and $\Sigma_k$​ is the top-left $k\times k$ block of $\Sigma$
- In a probabilistic context, this is invaluable for noise reduction and data compression. By retaining only the components associated with the largest singular values, we can filter out the noise, which is often associated with the smaller singular values, thus revealing the more significant underlying probabilistic relationships within the data

#### **Understanding Covariance Structure**

SVD provides a direct decomposition of the relationships between random variables in a dataset. The right-singular vectors (V) identify directions of maximum covariance in the variable space, while the left-singular vectors (U) represent the projection of the data points onto these directions. The singular values quantify the magnitude of this covariance in each principal direction. This decomposition is crucial for understanding the dependencies and correlations inherent in a multivariate probability distribution.

#### **Pseudo-Inverse and Linear Regression**

- In linear regression, we often seek to solve the normal equations, which can be ill-conditioned or involve a non-invertible matrix
- The pseudo-inverse of a matrix, which provides a stable solution to least-squares problems, can be efficiently and stably calculated using SVD

$$
A^+=V\Sigma^+U^\top
$$

- where $\Sigma^+$ is obtained by taking the reciprocal of the non-zero singular values in \Sigma  and then transposing the resulting matrix
- This is particularly useful in probabilistic models where we need to estimate parameters from a set of linear equations derived from the data

- In the realm of linear algebra, Singular Value Decomposition (SVD) is a fundamental factorization of any real or complex matrix
- It extends the concept of eigendecomposition to any $m\times n$ matrix, whereas eigendecomposition is only defined for square matrices
- For a given matrix A, its SVD is given by:
$$
A=U\Sigma V^\top
$$

- where: 
    - $U \in \mathbb R^{m\times m}$ orthogonal matrix
        - The columns of $U$ are the left-singular vectors of $A$
    - $\Sigma \in \mathbb R^{m\times n}$ diagonal matrix with non-negative real numbers on the diagonal, known as the singular values of $A$
        - These values are typically arranged in descending order.
- **V^\top** is the transpose of an n\times n orthogonal matrix **V**. The columns of **V** are the right-singular vectors of **A**.

Geometrically, SVD decomposes the linear transformation represented by matrix **A** into a sequence of three simpler transformations: a rotation or reflection (V^\top), a scaling along the coordinate axes (\Sigma ), and another rotation or reflection (**U**).17

### Applications in Probability

Singular Value Decomposition is a powerful tool in probability and statistics, primarily through its application in dimensionality reduction and its connection to the structure of data distributions.

---

### Principal Component Analysis (PCA)

The most significant application of SVD in probability is its use in **Principal Component Analysis (PCA)**. PCA is a statistical procedure that uses an orthogonal transformation to convert a set18 of observations of possibly correlated variables into a set of values of linearly uncorrelated variables called principal components.19

Given a data matrix **X** where each row represents an observation and each column represents a variable, the goal of PCA is to find the directions of maximum variance in the data.20 The SVD of the covariance matrix of **X** (or the centered data matrix itself) directly provides the principal components.

Let X~ be the centered data matrix, where the mean of each column has been subtracted from the column. The SVD of X~ is X~=U\Sigma V^\top. The columns of **V** (the right-singular vectors) are the principal components of the data.21 The singular values in \Sigma  are related to the variance explained by each principal component. By selecting the top _k_ principal components corresponding to the _k_ largest singular values, one can perform dimensionality reduction while retaining the most significant information in the data.22

---

### Least Squares and Regression

In statistical modeling, particularly in linear regression, we often seek to solve the normal equation $A^\top Ax=A^\top b$
If the matrix $A^\top A$ is ill-conditioned or singular, finding a stable solution can be challenging.

SVD provides a robust method for solving such linear systems. By decomposing **A** using SVD, we can compute the **Moore-Penrose pseudoinverse** of **A**, denoted as $A^\top$

$A^+ = V\Sigma +U^\top$

Here, \Sigma + is obtained by taking the reciprocal of the non-zero singular values in \Sigma  and then transposing the resulting matrix. The solution to the least-squares problem is then given by x=A+b. This approach is more numerically stable than directly solving the normal equations.

---

### Connection to Multivariate Normal Distribution

SVD is also connected to the geometry of the multivariate normal distribution. The level sets of the probability density function of a multivariate normal distribution with covariance matrix $C$ are ellipsoids.
The SVD of the covariance matrix, $C=U\Sigma U^\top$ (since $C$ is symmetric, $U=V$), reveals the orientation and the lengths of the principal axes of these ellipsoids.
The columns of $U$ give the directions of the principal axes, and the square roots of the singular values (which are the eigenvalues in this case) give the lengths of these axes. This provides a geometric understanding of the distribution of the data.