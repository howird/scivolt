---
tags:
  - note
  - math/lin-alg
  - comp-methods/vision
  - cs684
status: done
---
# Fundamental Matrix

## Definition

- The __Fundamental Matrix__, $F$, enforces the [epipolar constraint](2_concepts/epipolar-geometry.md) to relate the pixel coordinates on two images $\tilde{\mathbf{x}}_l$ and $\tilde{\mathbf{x}}_r$

$$
\tilde{\mathbf{x}}_l^\top F \tilde{\mathbf{x}}_r = 0
$$

- where:
$$
\tilde{\mathbf{x}}_l = \begin{bmatrix} u_l \\ v_l \\ 1 \end{bmatrix}, \quad \tilde{\mathbf{x}}_r = \begin{bmatrix} u_r \\ v_r \\ 1 \end{bmatrix}, \quad F = K_l^{-\top} E K_r^{-1}
$$

## Motivation

- Recall [camera intrinsic parameters](2_concepts/camera-calibration.md), $K$, where:
$$
K = \begin{bmatrix}
f_x & s & c_x \\
0 & f_y & c_y \\
0 & 0 & 1 \\
\end{bmatrix}
$$
- where:
    - $f_x, f_y$: Focal lengths in pixels
    - $s$: Skew parameter (usually zero)
    - $c_x, c_y$: Principal point coordinates

- the [Essential Matrix](2_concepts/epipolar-geometry.md), $E$, assumes that both the cameras have the same intrinsic parameters $K=I$, obviously this is not always the case
- the __Fundamental Matrix__, $F$, extends the Essential Matrix, $E$, by also relating the pixel coordinates directly:
$$
F = K_l^{-\top} E K_r^{-1}
$$
- where:
    - $K_l$ and $K_r$ are the intrinsic parameter matrices of the left and right cameras
    - $K_l^{-\top}$ denotes the inverse transpose of $K_l$
