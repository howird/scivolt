---
tags:
  - note
  - math/lin-alg
status: done
---
# Cross Product

## Overview

- A vector operation that given 2 vectors, returns a vector perpendicular to both
- Properties:
    - $\mathbb R^3 \times \mathbb R^3 \rightarrow  \mathbb R^3$
    - **anti-commutative**: $\mathbf{a} \times \mathbf{b} = -(\mathbf{b} \times \mathbf{a})$; the operation yields the negative of the original result when the order of the operands is reversed

## Definition

- For two vectors $\mathbf{a} = [a_1, a_2, a_3]$ and $\mathbf{b} = [b_1, b_2, b_3]$, the cross product $\mathbf{a} \times \mathbf{b}$ is computed as:

$$
\mathbf{a} \times \mathbf{b} =
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
a_1 & a_2 & a_3 \\
b_1 & b_2 & b_3 \\
\end{vmatrix}
= \left[ a_2b_3 - a_3b_2, a_3b_1 - a_1b_3, a_1b_2 - a_2b_1 \right]
$$

## Cross Product in Higher Dimensions (n-Dimensions)

- In higher dimensions, the cross product is not as straightforward as in 3D
- for $n$-dimensional space, an $n-2$-dimensional cross product can be defined
- this operation is less common and much more complex
- The most widely known cross product is the 3D version, which has practical uses in various fields

## Skew-Symmetric Matrix Representation

- Given: $\mathbf{a} \times \mathbf{b} = \left[ a_2b_3 - a_3b_2, a_3b_1 - a_1b_3, a_1b_2 - a_2b_1 \right]$, it is clear that the cross product vector is a linear combination of $\bf a$ and $\bf b$
- This implies that $\mathbf{a} \times \mathbf{b}$ can be represented by a linear transformation or matrix multiplication; where, the matrix is defined as:

$$
\displaylines{
\mathbf{a} \times \mathbf{b} = [\mathbf{a}]_\times \mathbf{b} \\
\text{Where: }[\mathbf{a}]_\times = \begin{bmatrix}
0 & -a_3 & a_2 \\
a_3 & 0 & -a_1 \\
-a_2 & a_1 & 0
\end{bmatrix}
}
$$
- Thus $\mathbf{a} \times \mathbf{b}$ in 3D can be expressed using a skew-symmetric matrix multiplication

### Usage in Epipolar Geometry

- In [epipolar geometry](2_concepts/epipolar-geometry.md), which is fundamental in stereo vision and 3D reconstruction, the cross product is used to compute the epipolar lines
- Given two cameras viewing the same scene, the relative positions of corresponding image points can be described by the **fundamental matrix** $\mathbf{F}$
- The cross product comes into play when calculating epipolar constraints, ensuring that the corresponding points lie on their respective epipolar lines