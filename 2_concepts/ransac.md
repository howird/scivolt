---
tags:
  - note
  - comp-methods/clustering
status: doing
---
# RANSAC

## Algorithm

- RANSAC(number of iterations: $N$; threshold $T$):
- for $N$ iterations:
    - randomly sample two points from the set, get a model, $l$
    - for each point, $p$, in dataset check if distance between $l$ and $p$ is less than the threshold, $T$, i.e. $||p−l|| \le T$
    - store number of inliers and model, $(n_{in}, l)$
- select model with most inliers, $l_{in}$
- Use least squares to fit a model (line) to all inliers for $l^{in}$ i.e. $||p_{in}−l_{in}|| \le T$

## Applications

- [homography](2_concepts/homography.md)
- 