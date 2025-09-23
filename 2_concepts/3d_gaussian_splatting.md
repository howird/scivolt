---
tags:
  - 'paper'
status: backlog
year: '2023/08'
authors: 'Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis'
citekey: kerbl3DGaussianSplatting2023
---
# 3D Gaussian Splatting for Real-Time Radiance Field Rendering

## Background

- Radiance Field methods have recently revolutionized novel-view synthesis of scenes captured with multiple photos or videos
- However, achieving high visual quality still requires neural networks that are costly to train and render, while recent faster methods inevitably trade off speed for quality
- For unbounded and complete scenes (rather than isolated objects) and 1080p resolution rendering, no current method can achieve real-time display rates
- We introduce three key elements that allow us to achieve state-of-the-art visual quality while maintaining competitive training times and importantly allow high-quality real-time (>= 30 fps) novel-view synthesis at 1080p resolution
- First, starting from sparse points produced during camera calibration, we represent the scene with 3D Gaussians that preserve desirable properties of continuous volumetric radiance fields for scene optimization while avoiding unnecessary computation in empty space; Second, we perform interleaved optimization/density control of the 3D Gaussians, notably optimizing anisotropic covariance to achieve an accurate representation of the scene; Third, we develop a fast visibility-aware rendering algorithm that supports anisotropic splatting and both accelerates training and allows realtime rendering
- We demonstrate state-of-the-art visual quality and real-time rendering on several established datasets.

### Problem

- 

### Goal

- Method for Radiance Field Rendering:
    - using a set of 3D Gaussian Splats initialized from the sparse point cloud generated as a by-product of SfM (which is already used as a preprocessing step in NeRFs)
    - demonstrates 3D Gaussians preserve the desirable properties of Radiance Fields while avoiding the unnecessary computation in empty space
- Techniques to generate 3D Gaussians:
    - interleaved optimization/density control
    - minimize anisotropic covariance
- Rendering algorithm:
    - visibility aware
    - supports anisotropic splatting
    - faster training & rendering (DSTA)


### Past Work

- NeRFs. built on MLPs; which are not efficient for rendering; continuous representations
    - efficient methods use interpolation from values from voxels/hashes/grdis
    - stochastic sampling used in continuous representations lead to noise and are costly+inefficient

## Methodology

> [! abstract]

- 

## Results

> [!abstract]

- 

## Comments and Implications

- 
