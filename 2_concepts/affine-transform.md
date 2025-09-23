---
tags:
  - note
  - comp-methods/vision/processing
  - math/lin-alg
  - cs684
status: done
---
# Affine Transformations

[useful video by leios labs](https://www.youtube.com/watch?v=E3Phj6J287o)

- Affine transformations are linear transformations performed upon [homogeneous coordinates](2_concepts/homogeneous-coordinates.md)
    - similarly to homogeneous coordinates, an affine transform in $n$-dimensions has $n+1$ dimensionality to enable translation and thus is a  $(n+1) \times (n+1)$ matrix

## General Form

- The general form of an affine transformation matrix in $n$-dimensions is:

$$
T = \begin{bmatrix}
A & \mathbf{t} \\
\mathbf{0}^\top & 1
\end{bmatrix}
$$
- Where:
    - matrix $A \in \mathbb{R}^{n \times n}$ represents the linear transformation [(rotation, scaling, or shearing)](2_concepts/linear-transformations.md)
    - vector $\mathbf{t} \in \mathbb{R}^{n \times 1}$ represents the translation along each axis
    - row vector $\mathbf{0}^\top$ is a row vector of zeros with length $n$, ensuring that the extra coordinate remains unaffected

- Transformation formula:
$$
\mathbf{p'} = T \cdot \mathbf{p} = \begin{bmatrix}
A & \mathbf{t} \\
\mathbf{0}^\top & 1
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n \\
1
\end{bmatrix}
=
\begin{bmatrix}
A \cdot \mathbf{v} + \mathbf{t} \\
1
\end{bmatrix}
$$
- where 
    - $\mathbf{v}$: original point in Cartesian coordinates $[ x_1, x_2, \dots, x_n]^\top$
    - $\mathbf{p}$: original point in homogeneous coordinates
    - $\mathbf{p'}$: transformed point in homogeneous coordinates

## Properties

- Origin does not necessarily map to the origin
- Lines map to lines
- Parallel lines remain parallel
- closed under composition

- Can be combined with other affine transformations by multiplying their matrices.
- Cannot perform perspective distortions (for that, projective transformations are needed)
