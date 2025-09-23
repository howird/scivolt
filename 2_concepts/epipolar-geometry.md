---
tags:
  - note
  - comp-methods/vision
  - math/lin-alg
  - cs684
aliases:
  - essential matrix
  - fundamental matrix
status: review
---
# Epipolar Geometry

## Overview

![](2_concepts/media/Pasted%20image%2020241022143320.png)

- Epipoles ($e_l$, $e_r$): the image coordinate of the other camera from a camera
    - For every stereo system there is a unique pair of epipoles
- Epipolar plane: each point in the scene has an epipolar plane, the plane containing $P$, $O_l$, $O_r$, $e_l$, $e_r$
- Epipolar lines:  each point in the scene has an epipolar plane, the plane containing $P$, $O_l$, $O_r$, $e_l$, $e_r$

## Essential Matrix

### Overview

![](2_concepts/media/Pasted%20image%2020241022143448.png)

- The __epipolar matrix__ is essential in stereo vision for determining corresponding points between images, which is crucial for tasks like 3D reconstruction

- The **epipolar matrix** encapsulates the geometric relationship between two different views of the same scene, enforcing the **epipolar constraint**:
$$
\mathbf{x}_l^\top E \mathbf{x}_r = 0
$$

- The __epipolar constraint__ states that a point in one image must lie along a specific line (the epipolar line) in the other image:
![](2_concepts/media/Pasted%20image%2020241023102852.png)

### Derivation

#### 1. Epipolar Constraint

- By definition, $\bf x_l$, $\bf x_r$, and $\bf t$ are __co-planar__, they all exist on the epipolar plane:
$$
\therefore \bf x_l^\top \cdot (\bf t \times \bf x_r) = 0
$$
- additionally, we re-express the [cross-product](2_concepts/cross-product.md) $\mathbf{t} \times \mathbf{x}_r$ as a matrix multiplication of the skew-symmetric matrix, $[\mathbf{t}]_\times$:
$$
\mathbf{t} \times \mathbf{x}_r = [\mathbf{t}]_\times \mathbf{x}_r
$$
- where:

$$
\bf t = \begin{bmatrix} t_x \\ t_y \\ t_z \end{bmatrix},
[\mathbf{t}]_\times = \begin{bmatrix}
0 & -t_z & t_y \\
t_z & 0 & -t_x \\
-t_y & t_x & 0 \\
\end{bmatrix}
$$

$$
\therefore \bf x_l^\top \cdot ([\mathbf{t}]_\times \bf x_r) = 0
$$

#### 2. Camera Transformation Equation

- By definition, $\bf x_l$ can be written in terms of $\bf x_r$ with:
$$
\bf x_l = \bf R x_r + \bf t
$$
- where $\mathbf{R}$ is the rotation matrix and $\mathbf{t}$ is the translation vector between the coordinate systems of the left and right cameras
- this equation transforms the point from the right camera's coordinate system to the left's


#### 3. Derivation of the Essential Matrix

- Substituting the Camera Transformation equation for $\mathbf{x}_l$ into the epipolar constraint:
$$
\begin{align}
(\mathbf{R} \mathbf{x}_r + \mathbf{t})^\top [\mathbf{t}]_\times \mathbf{x}_r &= 0 \\
\mathbf{x}_r^\top \mathbf{R}^\top [\mathbf{t}]_\times \mathbf{x}_r + \underbrace{\mathbf{t}^\top [\mathbf{t}]_\times}_{\bf a\times \bf b = \bf 0} \mathbf{x}_r &= 0 \\
\mathbf{x}_r^\top \underbrace{\mathbf{R}^\top [\mathbf{t}]_\times}_{E} \mathbf{x}_r &= 0
\end{align}
$$

- defining the Essential Matrix $E = [\mathbf{t}]_\times \mathbf{R}$:
$$
\therefore \mathbf{x}_l^\top E \mathbf{x}_r = 0
$$

- in full matrix notation $\mathbf{x}_l^\top E \mathbf{x}_r = 0$, where:
$$
\begin{align}
E &= [\mathbf{t}]_\times \mathbf{R} \\

&= \begin{bmatrix}
0 & -t_z & t_y \\
t_z & 0 & -t_x \\
-t_y & t_x & 0 \\
\end{bmatrix} \begin{bmatrix}
r_{11} & r_{12} & r_{13} \\
r_{21} & r_{22} & r_{23} \\
r_{31} & r_{32} & r_{33} \\
\end{bmatrix} \\

&= \begin{bmatrix}
e_{11} & e_{12} & e_{13} \\
e_{21} & e_{22} & e_{23} \\
e_{31} & e_{32} & e_{33} \\
\end{bmatrix}
\end{align}
$$
