---
tags:
  - paper
status: done
year: 2015/10
authors: Matthew Loper, Naureen Mahmood, Javier Romero, Gerard Pons-Moll, Michael J. Black
citekey: SMPL:2015
---
# SMPL: a skinned multi-person linear model

## TLDR

- SMPL function $\mathcal{M}: \beta \times \theta \rightarrow \mathbb{R}^{N \times 3}$  maps shape and pose to a 3D mesh where
    - $N = 6890$ is the number of vertices
    - $\beta \in \mathbb R^{10}$: linear coefficients of a low-dimensional statistical shape model
    - $\theta \in \mathbb R^{3K}$: global rotation of the body and the 3D relative rotations of the kinematic skeleton of $K=23$ joints in axis-angle representation