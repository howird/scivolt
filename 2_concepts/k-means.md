---
date: April 20, 2022
status: backlog
tags:
  - '#ai/ml'
  - '#application/clustering'
---

# K-Means Clustering

## Introduction / Background

K-Means Clustering is a clustering method that can classify a dataset into $k$ classes, where $k$ is given by the user.

- Here is a great video explaining how the algorithm works, this post will contain a python implementation

<iframe width="100%" height="310px" src="https://www.youtube.com/embed/4b5d3muPQmA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Implementation

### Algorithm Inputs

```py
def kmeans(X, k=3, max_iterations=3)
```

Here is the function definition, whose inputs are:

- a point set/dataset $X$, which is an $(N, D)$ matrix where $N$ is the number of points, and $D$ is the number of dimensions

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

### Setup: Initializing Means

```py
N, dim = X.shape
means = X[np.random.choice(N, size=(k,), replace=False)]
ret = []
```

- The first thing we do is to get the shape of $X$ so we know the number of points ($N$) and the dimensionality of the points ($D$)
- Next, we choose $k$ random points in our point set, these will be our initial $k$ means
- Additionally, we want to keep track of the progress of the algorithm so we create a list that we can fill with information at each step of the algorithm

### Setup: Euclidean Distance Function

```py
def euclidean(X, means):
    dists = [np.linalg.norm(X - a, axis=1) for a in means]
    return np.vstack(dists).T
```

- Before the main loop, we must define a function to calculate the distances between all points and each mean
- In the above function, `euclidean()`, we calculate the euclidean distance from each point using `np.linalg.norm` for each of the $k$ means
- Thus we have a list of $k$ row vectors with $N$ length:

$$
\begin{bmatrix}
\text{dist}_{1,1} & \text{dist}_{1,2} & \dots & \text{dist}_{1,N}
\end{bmatrix}
$$

$$
\dots
$$

$$
\begin{bmatrix}
\text{dist}_{k,1} & \text{dist}_{k,2} & \dots & \text{dist}_{k,N}
\end{bmatrix}
$$

- Next, we stack the $k$ row vectors to get a $(k, N)$ matrix:

$$
\begin{bmatrix}
\text{dist}_{1,1} & \text{dist}_{1,2} & \dots  & \text{dist}_{1,N} \\
\vdots            & \vdots            & \ddots & \vdots \\
\text{dist}_{k,1} & \text{dist}_{k,2} & \dots  & \text{dist}_{k,N}
\end{bmatrix}
$$

- Then transpose that matrix to get a $(N, k)$ matrix of distances for each mean

$$
\begin{bmatrix}
\text{dist}_{1,1} & \dots  & \text{dist}_{1,k} \\
\text{dist}_{2,1} & \dots  & \text{dist}_{2,k} \\
\vdots            & \ddots & \vdots \\
\text{dist}_{N,1} & \dots  & \text{dist}_{N,k}
\end{bmatrix}
$$

### Main Loop

```py
for i in range(max_iterations):
    # 1. calculate the distance between each point and the k means
    # 2. find the nearest mean for each point
    # 3. if no updates are made then stop early
    # 4. update each k mean to be the mean of all points nearest to it
```

- Now we get to the main loop, where we perform the $k$ means algorithm
- I have commented the tasks that we have to do in the loop

### Loop Step 1

```py
dists = euclidean(X, means)
```

- We have already implemented most of the first step with our `euclidean` function
- We now have `dists`, a $(k, N)$ matrix of distances from each of the k means:

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
labels = np.argmin(dists, axis=1)
```

- Next, we calculate the the nearest mean to each point using `np.argmin` across axis 1 or the columns
- This gives us a vector, `labels` which contains column index of the smallest euclidean distance for each point, this column index corresponds to the nearest mean

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

### Loop Step 3

```py
if len(ret) > 0 and (ret[-1] == labels).all():
    print(f"Early stop at index {i}")
    break
ret.append(labels)
```

- Next we check if the labels we just created are the exact same as the previous iteration, if so, we end the algorithm
- If not, we continue by adding the new labels to our list

### Loop Step 4

```py
for j in range(k):
    means[j] = X[np.where(labels==j)].mean(axis=0)
```

- In the last step, we go through each of the means,
- We get the indices of each point that was labelled as the current mean with `np.where`
- Then, we calculate the means of all the points with `np.mean`

### Overall code

```py
def kmeans(X, k=3, max_iterations=3):
    N, dim = X.shape
    means = X[np.random.choice(N, size=(k,), replace=False)]
    ret = []

    for i in range(max_iterations):
        dists = euclidean(X, means)
        labels = np.argmin(dists, axis=1)

        if len(ret) > 0 and (ret[-1] == labels).all():
            print(f"Early stop at index {i}")
            break
        ret.append(labels)
        
        for j in range(k):
            means[j] = X[np.where(labels==j)].mean(axis=0)
    
    return ret
```
