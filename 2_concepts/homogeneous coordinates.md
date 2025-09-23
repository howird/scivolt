---
tags:
  - note
  - comp-methods/vision/processing
  - math/lin-alg
  - cs684
status: done
---
# Homogeneous Coordinates

- Homogeneous coordinates augment the Cartesian coordinates by adding an extra coordinate, allowing transformations like translation to be represented as matrix multiplications (via an [affine transform](2_concepts/affine%20transform.md))
- In $n$-dimensional space, a point $[x_1, x_2, \dots, x_n]^\top$ is represented in homogeneous coordinates as $[x_1, x_2, \dots, x_n, w]^\top$, where:
    - $w$ is a scaling factor, which can normalize the coordinate back to Cartesian space
    - $w$ is typically 1

- ex: in 2D:
$$
\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} =
\begin{bmatrix} x_1/w \\ x_2/w \\ w \end{bmatrix} =
\begin{bmatrix} x_1 \\ x_2 \\ 1 \end{bmatrix}
$$
## Normalization

- For a point $\mathbf{p} = [x_1, x_2, \dots, x_n, w]^\top$ in homogeneous coordinates, the normalized Cartesian coordinates $[x'_1, x'_2, \dots, x'_n]^\top$ are computed as:

$$
x'_i = \frac{x_i}{w}, \quad \text{for } i = 1, 2, \dots, n
$$
- This reduces the point back to the Cartesian form, provided that $w \neq 0$
- If $w = 0$, the point is considered to be at infinity (in the context of projective geometry)

### Use of $w$-Coordinate in Projective Geometry
- The $w$-coordinate is crucial in projective geometry, where it represents points at infinity when $w = 0$
- This enables the representation of parallel lines meeting at a point at infinity and allows for the modeling of perspective transformations (which are important in 3D graphics and camera projections)

#### Perspective Division

- In graphics and 3D rendering, the $w$-coordinate can change dynamically as part of a transformation
- After transformations (such as projection), the perspective division is applied to bring points back into the viewable 3D Cartesian coordinate system
- This step ensures that points closer to the viewer (larger $w$) are properly scaled and those farther away (smaller $w$) are represented correctly in the rendering process





