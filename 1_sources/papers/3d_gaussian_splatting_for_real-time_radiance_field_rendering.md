---
tags:
  - "#RawInformation"
  - "#Paper"
  - "#Unread"
completed: false
title: "3D Gaussian Splatting for Real-Time Radiance Field Rendering"
authors: "Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis"
year: '2023/08'
url: ""
citekey: "kerbl3DGaussianSplatting2023"
aliases:
  - ""
  - "kerbl3DGaussianSplatting2023"
---

# 3D Gaussian Splatting for Real-Time Radiance Field Rendering

> [!abstract]
> Radiance Field methods have recently revolutionized novel-view synthesis of scenes captured with multiple photos or videos. However, achieving high visual quality still requires neural networks that are costly to train and render, while recent faster methods inevitably trade off speed for quality. For unbounded and complete scenes (rather than isolated objects) and 1080p resolution rendering, no current method can achieve real-time display rates. We introduce three key elements that allow us to achieve state-of-the-art visual quality while maintaining competitive training times and importantly allow high-quality real-time (>= 30 fps) novel-view synthesis at 1080p resolution. First, starting from sparse points produced during camera calibration, we represent the scene with 3D Gaussians that preserve desirable properties of continuous volumetric radiance fields for scene optimization while avoiding unnecessary computation in empty space; Second, we perform interleaved optimization/density control of the 3D Gaussians, notably optimizing anisotropic covariance to achieve an accurate representation of the scene; Third, we develop a fast visibility-aware rendering algorithm that supports anisotropic splatting and both accelerates training and allows realtime rendering. We demonstrate state-of-the-art visual quality and real-time rendering on several established datasets.

## 3-pass method

### Pass 1

> [!info]
> - carefully read title, abstract, intro
> - read all headings and subheadings
> - check references for papers that you have read
> - make any relevant comments on the following:
> 	- Category: What type of paper is this? A measurement paper? An analysis of an existing system? A description of a research prototype?
> 	- Context: Which other papers is it related to? Which theoretical bases were used to analyze the problem?
> 	- Correctness: Do the assumptions appear to be valid?
> 	- Contributions: What are the paper’s main contributions?
> 	- Clarity: Is the paper well written?

#### Abstract & Introduction Summary

##### Abstract

- This paper introduces 3 major contributions
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

###### Introduction

- Previous: NeRFs. built on MLPs; which are not efficient for rendering; continuous representations
	- efficient methods use interpolation from values from voxels/hashes/grdis
	- stochastic sampling used in continuous representations lead to noise and are costly+inefficient
- Ours: 3D Gaussians. use tile based splatting solution; real-time & SOTA quality
	- use sparese point clouds (which are an )

#### Additional Comments

- 

#### Questions to Answer in Following Passes

- 

### Pass 2

> [!info]
> Pass 2 (1 hour):
> - understand figures, graphs, looking for errors
> - read paper with greater care but skip proofs
> - note other significant references you may want to read

### Pass 3

> [!info]
> Pass 3 (5 hours):
> - essentially re-implement the entire paper
> - identify assumptions in the paper and challenge them
> - consider how you would present each idea

- [INSERT GIT REPO HERE](www.github.com)
	- comment code and make PR

## Distillation

> [!info]
> After the 2/3 pass method try and copy and paste the above notes and present them in a more structured manner

### Problem

- 

### Key Points

- 

### Methodology

- 

### Results

 - 

### Comments and Implications

- 
