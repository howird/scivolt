---
date: April 22, 2022
status: backlog
tags:
  - '#ai/ml'
  - '#application/clustering'
---

# Soft K-Means Clustering

## Introduction / Background

Soft K-Means Clustering is an extension of [K-Means Clustering](k-means.md)

- However, instead of updating the $k$ means solely based on the mean of the points closest to them, we calculate the probability distribution that each point belongs to the same class as each mean using the $\text{softmax}$ function:

$$
\text{softmax}(x_i) = \frac{e^{x_i}}{\sum_{j=1}^n e^{x_j}}
$$

- Then, we update the value of each mean as the expected value ($E\[x\]$) or weighted average of the points w.r.t. their probability distribution

## Implementation

### Algorithm Inputs

```py
def soft_k_means(X, k=3, max_iterations=3)
```

Here is the function definition, whose inputs are:

- a point set/dataset $X$, which is an $(N, D)$ matrix where $N$ is the number of points, and $D$ is the number of dimensions:

$$
\begin{bmatrix}
x_{1,1} & \dots  & x_{1,d} \\
x_{2,1} & \dots  & x_{2,d} \\
\vdots  & \ddots & \vdots \\
x_{N,1} & \dots  & x_{N,d}
\end{bmatrix}
$$

- a positive integer $k$, which is the number of classes/means to classify from
- the max number of iterations to optimize the k means

### Setup

This algorithm follows the same setup as that of [K-Means Clustering](k-means.md)

### Main Loop

```py
for i in range(max_iterations):
    # 1. calculate the distance between each point and the k means
    # 2. calculate the probability distribution of each point belonging to each mean
    # (optionally calculate the loss)
    # 3. if no updates are made then stop early
    # 4. update each k mean to be the mean of all points nearest to it
```

- Now we get to the main loop, where we perform the $k$ means algorithm
- I have commented the tasks that we have to do in the loop

### Loop Step 1

```py
dists = euclidean(X, mus)
```

- We have already implemented most of the first step with our `euclidean` function

- We now have `dists`, a $(N, k)$ matrix of distances from each of the k means:

$$
\begin{bmatrix}
\text{dist}_{1,1} & \dots  & \text{dist}_{1,k} \\
\text{dist}_{2,1} & \dots  & \text{dist}_{2,k} \\
\vdots            & \ddots & \vdots \\
\text{dist}_{N,1} & \dots  & \text{dist}_{N,k}
\end{bmatrix}
$$

### Loop Step 2

```py
exps = np.exp(dists) # Nxk
r = exps/np.sum(exps, axis=1, keepdims=True) # Nxk
```

- Next, to calculate the the $\text{softmax}$ of each point, we first apply the $\exp$ function a.k.a. $e^x$ to each point (using `np.exp`)

- This gives us a $(N, d)$ matrix, `exps`:

$$
\begin{bmatrix}
e^{x_{1,1}} & \dots  & e^{x_{1,d}} \\
e^{x_{2,1}} & \dots  & e^{x_{2,d}} \\
\vdots  & \ddots & \vdots \\
e^{x_{N,1}} & \dots  & e^{x_{N,d}}
\end{bmatrix}
$$

- Then, we calculate the $\text{softmax}$ by dividing each element by the sum of its row giving us the $(N, D)$ matrix, `r`:

$$
\begin{bmatrix}
e^{x_{1,1}}/\sum_{m=1}^d e^{x_{1,m}} & \dots  & e^{x_{1,d}}/\sum_{m=1}^d e^{x_{1,m}} \\
e^{x_{2,1}}/\sum_{m=1}^d e^{x_{2,m}} & \dots  & e^{x_{2,d}}/\sum_{m=1}^d e^{x_{2,m}} \\
\vdots  & \ddots & \vdots \\
e^{x_{N,1}}/\sum_{m=1}^d e^{x_{N,m}} & \dots  & e^{x_{N,d}}/\sum_{m=1}^d e^{x_{N,m}}
\end{bmatrix}
$$

### Loop Step 4

```py
labels = np.argmin(dists, axis=1)
if len(ret) > 0 and (ret[-1] == labels).all():
    print(f"Early stop at index {i}")
    break
ret.append(labels)
```

- Next, we create the labels by calculating which mean is each point closest to (this is the same as Loop Step 3 of KNN) to get:

$$
\begin{bmatrix}
\text{label}_{1} \\
\text{label}_{2} \\
\vdots \\
\text{label}_{N}
\end{bmatrix}
$$

$$
\text{where: } \text{ label}_{i} \in \[0, k), \mathbb{Z}
$$

- Then, we check if the labels we just created are the exact same as the previous iteration, if so, we end the algorithm
- If not, we continue by adding the new labels to our list

### Loop Step 5

```py
for j in range(k):
    mus[j] = r[:,j].dot(X)/np.sum(r[:,j]) 
```

- In the last step, we go through each of the means,
- We get the corresponding column of `r`, which corresponds to the probability distributions of each point belonging to the current mean:

$$
\begin{bmatrix}
e^{x_{1,j}}/\sum_{m=1}^d e^{x_{1,m}} \\
e^{x_{2,j}}/\sum_{m=1}^d e^{x_{2,m}} \\
\vdots \\
e^{x_{N,j}}/\sum_{m=1}^d e^{x_{N,m}}
\end{bmatrix}
$$

- Then, we compute the dot product between $X$ and that column of `r` and divide by the total sum of that column to get the expected value of each mean

### Overall code

```py
def soft_k_means(X, k=3, max_iterations=3, beta=1.0):
    N, dim = X.shape
    ret = []
    mus = X[np.random.choice(N, size=(k,), replace=False)]

    for i in range(max_iterations):
        # Step 1
        dists = euclidean(X, mus)
        # Step 2
        exps = np.exp(-beta*dists)
        r = exps/np.sum(exps, axis=1, keepdims=True)
        # Step 3
        labels = np.argmin(dists, axis=1)
        # the line below is the optional loss calculation
        loss = sum([np.sum(dists[np.where(labels==j), j]) for j in range(k)])
        if len(ret) > 0 and (ret[-1][0] == labels).all():
            print(f"EARLY STOP AT {i}, max_iterations={max_iterations}")
            break
        ret.append((labels, loss))

        # Step 4
        for j in range(k):
            mus[j] = r[:,j].dot(X)/np.sum(r[:,j]) 
    
    return ret
```
