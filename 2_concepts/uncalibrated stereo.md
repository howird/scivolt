---
tags:
  - note
  - math/lin-alg
  - comp-methods/vision
  - cs684
status: done
---
# Uncalibrated Stereo

- [Epipolar Geometry](2_concepts/epipolar%20geometry.md): Describes the intrinsic projective geometry between two views.
- Essential Matrix $E$: Encapsulates rotation and translation between two calibrated cameras.
- [Fundamental Matrix](2_concepts/fundamental%20matrix.md) $F$: Extends $E$ to uncalibrated cameras, incorporating intrinsic parameters.
- **Epipolar Constraint**: Ensures that corresponding points in two images satisfy $\mathbf{x}_l^\top E \mathbf{x}_r = 0$ or $\tilde{\mathbf{x}}_l^\top F \tilde{\mathbf{x}}_r = 0$

