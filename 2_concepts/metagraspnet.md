---
aliases:
  - MetaGraspNet
  - gillesMetaGraspNetLargeScaleBenchmark2022
authors: Maximilian Gilles, Yuhao Chen, Tim Robin Winter, E. Zhixuan Zeng, Alexander Wong
citekey: gillesMetaGraspNetLargeScaleBenchmark2022
status: backlog
tags:
  - '#type/paper'
title: 'MetaGraspNet: A Large-Scale Benchmark Dataset for Scene-Aware Ambidextrous Bin Picking via Physics-based Metaverse Synthesis'
url: ''
year: 2022/08
---

# MetaGraspNet: A Large-Scale Benchmark Dataset for Scene-Aware Ambidextrous Bin Picking via Physics-based Metaverse Synthesis

> \[!abstract\]
> Autonomous bin picking poses significant challenges to vision-driven robotic systems given the complexity of the problem, ranging from various sensor modalities, to highly entangled object layouts, to diverse item properties and gripper types. Existing methods often address the problem from one perspective. Diverse items and complex bin scenes require diverse picking strategies together with advanced reasoning. As such, to build robust and effective machine-learning algorithms for solving this complex task requires significant amounts of comprehensive and high quality data. Collecting such data in real world would be too expensive and time prohibitive and therefore intractable from a scalability perspective. To tackle this big, diverse data problem, we take inspiration from the recent rise in the concept of metaverses, and introduce MetaGraspNet, a large-scale photo-realistic bin picking dataset constructed via physics-based metaverse synthesis. The proposed dataset contains 217k RGBD images across 82 different article types, with full annotations for object detection, amodal perception, keypoint detection, manipulation order and ambidextrous grasp labels for a parallel-jaw and vacuum gripper. We also provide a real dataset consisting of over 2.3k fully annotated high-quality RGBD images, divided into 5 levels of difficulties and an unseen object set to evaluate different object and layout properties. Finally, we conduct extensive experiments showing that our proposed vacuum seal model and synthetic dataset achieves state-of-the-art performance and generalizes to real world use-cases.

# Short Summary

### Key Points

-

### Problem

-

### Methodology

# Vision Problem

- address the vision problem of bin picking in two parts
  1. finding targeted objects
  1. predicting reliable grasp points for the objects
- Three main challenges for bin-picking:
  1. Combining information from multiple modalities, most robotic grasping systems are equipped with:
     - RGB sensors: captures the fine details of object’s texture
       - susceptible to shadows
       - objects with similar textures are difficult to differentiate
     - Depth sensors: captures geometry info via object’s surface location
       - prone to noise and produces faulty/invalid values for transparent and reflective
  1. Understanding/knowing where objects are and how they are posed and stacked
     - Objects in cluttered bin scenes are heavily occluded and entangled
     - an object can be visually broken into parts which can be detected as multiple
  1. Unseen objects or objects that change shape
     - when objects are scattered in the bin, visual features can be separated spatially
     - when multiple instances of unseen objects stacking together, visual features of the same class entangle at one location, and spatial information is not enough to separate instances
- Bin picking employs multiple gripper types
  - suction grippers: can pick box items and bags well, but struggles with complex or filigree objects
  - parallel jaw grippers:
  - others grippers: combination suction/PJ, hand-like grippers, etc.
-

# 6 Main Contributions

- 36 new objects suitable for a vacuum or parallel gripper
- Force-based suction cup model able to predict the vacuum seal for grasp candidates and provide a thorough method for generating parallel-jaw grasps based on physics simulation
- a pipeline to generate photo-realistic bin picking scenes together with a large-scale dataset
  - Besides rich grasp label annotation, it provides segmentation mask, object pose, center of mass heat-maps and propose the concept of semantic object key-points
- labels to characterize the objects’ layout in the bin: amodal segmentation masks, occlusion rates, object relationship matrix and layout label
- a real dataset consisting of 2.3k pixel-wise annotated RGBD images captured in a logistic setting with an industry-grade camera system
- extensive experiments in real world evaluating our proposed vacuum seal model and providing baseline experiments for vacuum grasp point detection and object detection and segmentation

## Method

- The proposed method to generate MetaGraspNet can be divided into three steps
  1. putting together a diverse item set,
  1. sampling ambidextrous grasp labels for each object individually
  1. generating bin scenes together with rich annotations in the metaverse

### A. Custom Object Dataset and Novel Object Test Set

- Existing object sets were extended with custom scans regarding the following criteria:
  - parallel and vacuum grasp capability, transparency, reflectiveness, dimensions, industry/warehouse domain, deformability, texture, weight and fragility

### B. Parallel Jaw Grasps Sampling Strategy

- Our proposed parallel-jaw grasps sampling method is inspired by the Acronym paper
- We expand it by a robust sampling strategy and an improved dynamic collision check.
- For each object in our dataset we generate up to $5000$ antipodal grasps, $G_j$, by:
  1. sample finger-object contact points $c_i$ evenly distributed over the mesh’s surface
  1. For each contact point, $c_i$:
     1. we sample $k=1, \ldots, N$, $N=5$ antipodal grasp attempts $c_{i,k}$ with random deviation in approach direction and translation
  1. The robust antipodal score $s_{\text{antipodal},i}$ for a contact point $c_i$ is: $s = n_{\text{successful samples}}/N$
  1. To obtain grasp poses in $SE(3)$, we sample for each successful contact point $s_{\text{antipodal},i}\gt 0$ up to $l=1\ldots L$ gripper poses by rotating it around the fingers’ closing direction
  1. A grasp $G_j=G_{i,k,l}$ is considered successful if the gripper does not collide with the object and we assign it $s_{pj,\text{anal.},j}=s_{\text{antip.},i}$
  1. In the next step, each successful grasp $G_j$ is executed multiple times in a physics simulation in IsaacGym
  1. Again, we extend the idea of robust sampling into simulation: Each grasp $G_j$ is simulated with different mass density factors and friction coefficients.
  1. Similar to [Acronym](acronym.md) we perform an upward and rotating gripper movement and assume a grasp is successful if the object is still in contact after execution
  1. The robust simulation score $s_{pj,sim.,j}$ is then defined as the fraction of successful grasps divided by the total number of attempts.

## Dataset Details

- The MetaGraspNet benchmark dataset contains:
  - 127k RGBD images with 5884 different scenes and 82 different objects
  - camera parameters are provided for generating point clouds
  - labels are provided in the respective camera coordinate system for each viewpoint, arranged in a hemishpere around the bin
  -
-

### Results

-

### Comments and Implications

-
