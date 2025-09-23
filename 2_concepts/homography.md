---
tags:
  - note
  - comp-methods/vision
  - cs684
status: done
---

# Homography Matrix

- A homography matrix is simply a fully parameterized $3\times 3$ matrix:

$$
H = \begin{bmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{bmatrix}
$$

- Generally, it is performed on a normalized [homogeneous coordinate](2_concepts/homogeneous%20coordinates.md), $X = [x, y, 1]^\top$
- Thus it can be thought of as distorting an image by moving the plane/canvas it is on in space
- This would enable you to stitch images together, e.g. panorama
