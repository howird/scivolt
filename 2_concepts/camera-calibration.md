---
tags:
  - note
  - math/lin-alg
  - comp-methods/vision
  - cs684
aliases:
  - perspective projection
  - camera projection
status: doing
---
# Camera Calibration

## Overview

![linear camera model](2_concepts/media/Pasted%20image%2020241015230922.png)

### Goal

$$
\underbrace{\begin{bmatrix}
x_i \\
y_i
\end{bmatrix}}_{\text{Pixel Coordinates, }X_i} = 
\underbrace{\begin{bmatrix}
f_x & s & u_c \\
0 & f_y & v_c \\
0 & 0 & 1
\end{bmatrix}}_{\text{Intrinsic Camera Params, } K}
\cdot
\underbrace{
\underbrace{\begin{bmatrix}
R & T \\
\bf0^\top & 1
\end{bmatrix}}_{\text{Extrinsic Camera Params, } R|T}
\cdot
\underbrace{\begin{bmatrix}
x_\cal{w} \\
y_\cal{w} \\
z_\cal{w} \\
1
\end{bmatrix}}_{\text{World Frame Coordinates, } X_\cal{W}}
}_{\text{Camera Frame Coordinates, } X_\cal{C}}
$$

- Given a world coordinate frame $\mathcal W$ (3D), and a camera coordinate frame $\cal C$ (3D), how the coordinates of an arbitrary point, $X$, in the world frame map onto the image plane (2D)?

- Steps:
    - find camera matrix, $P$, from known matches (resection problem)
    - find intrinsic, $K$, and extrinsic, $R|T$, parameters (matrix factorization, $P=K \cdot R|T$)
    
## World to Camera Transformation
;;
- To go from the world frame to the camera frame, only, $R|T$, a 3D [affine transform](2_concepts/affine-transform.md) is needed (consisting of a rotation and a translation)

$$
R|T = \begin{bmatrix}
R & T \\
\bf0^\top & 1
\end{bmatrix}
$$

- where:
    - $R\in\mathbb{R}^{3x3}$: and is a rotation matrix
    - $T\in\mathbb{R}^{3x1}$: representing the translation
    - $\implies R|T\in\mathbb{R}^{4x4}$

## Camera to Image Transformation (Perspective Projection)

- In perspective projection, we map arbitrary coordinate(s) relative to the camera frame, $X_\cal C$, to their location on the image plane $X_i$

- This matrix, $K$, is known as an intrinsic matrix as it encapsulates the internal parameters of the camera

$$
K = \begin{bmatrix}
f_x & s & u_c \\
0 & f_y & v_c \\
0 & 0 & 1
\end{bmatrix}
$$
- note: $K$ is an upper triangle matrix

### Derivation

![](2_concepts/media/Pasted%20image%2020241016191124.png)

- to get from $(x, y, z) \rightarrow (u, v)$, we use the following mapping, where:
    - $f$ is the focal length of the camera
    - $m_x$ and $m_y$: is the pixel density (pix/mm) in the $x$ and $y$ directions respectively
    - $(u_c, v_c)$: is the center of the image plane $(o_x, o_y)$

$$
(x, y, z) \rightarrow (\underbrace{fm_x\frac xz + u_c}_u, \underbrace{fm_y\frac yz + v_c}_v, \underbrace 1 _{\text{homogenous coord}})
$$
- note: this point is in normalized homogeneous form

- $f$ and $m_x$ or $m_y$ are often combined into $f_x$ and $f_y$, respectively
    - when $f_x \ne f_y$ the pixel is anisotropic, the aspect ratio, $f_x/f_y \ne 1$
- we can further extend this to skewed pixels, skewed by factor $s$
    - rewriting in homogeneous form:

$$
\begin{bmatrix}
wu \\ wv \\ w
\end{bmatrix} =
\begin{bmatrix}
f_x & s & u_c \\
0 & f_y & v_c \\
0 & 0 & 1
\end{bmatrix} \cdot
\begin{bmatrix}
x \\ y \\ z
\end{bmatrix}
$$
- note: just because this mapping gives us coordinates with units: pixels, does not mean the image coordinates of each point must be an integer
    - instead we keep floats and use linear interpolation
