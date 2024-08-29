---
aliases:
  - carionEndtoEndObjectDetection2020
authors: Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas Usunier, Alexander Kirillov, Sergey Zagoruyko
citekey: carionEndtoEndObjectDetection2020
status: backlog
tags:
  - '#type/paper'
title: End-to-End Object Detection with Transformers
url: ''
year: 2020/05
---

# End-to-End Object Detection with Transformers

> \[!abstract\]
> We present a new method that views object detection as a direct set prediction problem. Our approach streamlines the detection pipeline, effectively removing the need for many hand-designed components like a non-maximum suppression procedure or anchor generation that explicitly encode our prior knowledge about the task. The main ingredients of the new framework, called DEtection TRansformer or DETR, are a set-based global loss that forces unique predictions via bipartite matching, and a transformer encoder-decoder architecture. Given a fixed small set of learned object queries, DETR reasons about the relations of the objects and the global image context to directly output the final set of predictions in parallel. The new model is conceptually simple and does not require a specialized library, unlike many other modern detectors. DETR demonstrates accuracy and run-time performance on par with the well-established and highly-optimized Faster RCNN baseline on the challenging COCO object detection dataset. Moreover, DETR can be easily generalized to produce panoptic segmentation in a unified manner. We show that it significantly outperforms competitive baselines. Training code and pretrained models are available at https://github.com/facebookresearch/detr.

# Short Summary

### Key Points

- the goal of object detection is to predict a set of bounding boxes and category labels for each object of interest
- their performances are significantly influenced by post-processing steps to collapse near-duplicate predictions ([non-maximum suppression](non-max-suppresion.md))
- as well as many other hand-crafted components such as anchor generation (as introduced in  [RCNNs](rcnn.md)) and rule-based training target assignment
- to simplify these pipelines we propose a direct set prediction approach to bypass the surrogate tasks
  !\[\[Pasted image 20231004152026.png\]\]
- DETR utilizes a simple architecture, by combining CNNs and [Transformer](1_sources/cv-papers/transformers.md) encoder-decoders
- DETR exploits the versatile and powerful relation modeling capability of Transformers to replace the hand-crafted rules, under properly designed training signals
-

## Arch

- The overall DETR architecture contains three main components a CNN backbone to extract a compact feature representation, an encoder-decoder transformer, and a simple feed forward network (FFN) that makes the final detection prediction
- Starting from the initial image $x\_{img} \\in \\mathcal{R}^3 \\times H_0 \\times W_0$ , a conventional CNN backbone generates a lower-resolution activation
  0 W0
  map f ∈ RC×H×W . Typical values we use are C = 2048 and H, W = H
  32 , 32 .
  Transformer encoder. First, a 1x1 convolution reduces the channel dimension
  of the high-level activation map f from C to a smaller dimension d. creating a
  new feature map z0 ∈ Rd×H×W . The encoder expects a sequence as input, hence
  we collapse the spatial dimensions of z0 into one dimension, resulting in a d×HW
  feature map. Each encoder layer has a standard architecture and consists of a
  multi-head self-attention module and a feed forward network (FFN). Since the
  transformer architecture is permutation-invariant, we supplement it with fixed
  positional encodings \[31,3\] that are added to the input of each attention layer. We
  defer to the supplementary material the detailed definition of the architecture,
  which follows the one described in \[47\].
-

### Problem

-

### Methodology

-

### Results

-

### Comments and Implications

-
