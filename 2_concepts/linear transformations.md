---
tags:
  - note
  - math/lin-alg
  - comp-methods/vision/processing
  - cs684
status: done
---
# Linear Transformations

- A mapping $f: \mathbb{R}^n \rightarrow \mathbb{R}^n$ is linear if:
    - geometrically:
        - origin maps to origin (no translation)
        - lines map to lines
        - parallel lines stay parallel
    - algebraically:
        - preserves vector space operations
            - $af(x) + bf(y) = f(ax+by)$ where $x, y$ are vectors and $a, b$ are scalars
        - [closed under composition](2_concepts/closed%20under%20composition.md)

### Desirable Properties
- cheap to apply
- easy to solve
- product of many transformations can be a single matrix

### Decompositions

- [SVD](2_concepts/single%20value%20decomposition.md): good for signal processing
- LU: good for 
- Polar Decompositions: good for spatial transformations

## Common 2x2 Linear Transformations

#### 1. Identity Matrix

- The identity matrix does not change a vector during transformation:
$$
I = \begin{bmatrix} 
1 & 0 \\ 
0 & 1 
\end{bmatrix}
$$
- When applied to any vector, it leaves the vector unchanged.

#### 2. Rotation Matrix
- A rotation matrix rotates a vector by an angle $\theta$ counterclockwise about the origin:

$$
R(\theta) = \begin{bmatrix} 
\cos(\theta) & -\sin(\theta) \\ 
\sin(\theta) & \cos(\theta) 
\end{bmatrix}
$$

#### 3. Scaling Matrix
A scaling matrix scales a vector by a factor of $s_x$ along the x-axis and $s_y$ along the y-axis:
$$
S = \begin{bmatrix} 
s_x & 0 \\ 
0 & s_y 
\end{bmatrix}
$$
If $s_x = s_y$, the scaling is uniform in all directions; otherwise, it stretches or compresses differently along each axis.

#### 4. Shear Matrix

A shear matrix shifts one axis, changing the shape of objects without altering their area:

- **Shear along the x-axis**:
$$
\text{Shear}_x = \begin{bmatrix}
1 & k_x \\
0 & 1
\end{bmatrix}
$$
- **Shear along the y-axis**:
$$
\text{Shear}_y = \begin{bmatrix}
1 & 0 \\
k_y & 1
\end{bmatrix}
$$

#### 5. Reflection Matrix

Reflection matrices flip a vector over a specific axis:

- **Reflection across the x-axis**:
$$
R_x = \begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}
$$

- **Reflection across the y-axis**:
$$
R_y = \begin{bmatrix}
-1 & 0 \\
0 & 1
\end{bmatrix}
$$
- **Reflection across the line $y = x$**:
$$
R_{xy} = \begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix}
$$

#### 6. Determinant and Invertibility

The determinant of a 2x2 matrix $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ is given by $a d - b c$. The determinant tells us whether the transformation matrix is invertible:

- If the determinant is non-zero, the matrix is invertible, meaning the transformation is reversible.
- If the determinant is zero, the matrix is singular, meaning the transformation squashes the vector space into a lower dimension (e.g., collapsing the space onto a line).

Each of these matrices can be combined to create more complex transformations by multiplying the matrices together.