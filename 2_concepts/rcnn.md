---
status: backlog
tags:
  - '#ai/dl'
  - '#application/vision'
---

# What is Image Detection?

- In image classification, we simply predict whether or not a class exists within an image
- In image detection, we must predict where instances of classes are located within an image using bounding boxes
- Before the [R-CNN](https://arxiv.org/pdf/1311.2524.pdf) paper, the two most successful methods for generating bounding boxes were to use a [regression CNN](https://papers.nips.cc/paper_files/paper/2013/hash/f7cade80b7cc92b991cf4d2806d6bd78-Abstract.html), and others used a sliding window detector
  - The sliding window detector led to units deep in the network to have very large receptive fields and strides in the input image, which makes precise localization an open technical challenge
- The R-CNN solves the CNN localization problem by operating within the "recognition using regions" paradigm
- At test time, the method:
  - generates around 2000 category independent region proposals for the input image
  - extracts a fixed length feature vector from each proposal using a CNN
  - classifies each region with category-specific linear SVMs
- Use a simple technique affine image warping to compute a fixed-size CNN input from each region proposal regardless of the region' shape

!\[\[Pasted image 20231002184636.png\]\]

# Fast RCNN and Faster RCNN

- The object detection system is composed of 2 modules
  - a CNN which proposes regions, Region Proposal Network (RPN)
  - Rast RCNN detector that uses the proposed regions

## Region Proposal Network

### Intro

- A RPN takes an image (of any size) as input and outputs a set of rectangular object proposals, each with an objectness score
  - "objectness": membership to an object class vs background
- To generate region proposals, we slide a small network over the convolutional feature map output by the last shared convolutional layer
- This small network takes as input an $n \times n$ spatial window of the input convolutional feature map
  - We use $n = 3$ in this paper, noting that the effective receptive field on the input image is large (228 pixels for VGG)
- Each sliding window is mapped to a lower-dimensional feature ($512-d$ for VGG, with $\text{ReLU}$ following)
- This feature is fed into two sibling fully-connected layers:
  - a box-regression layer (_reg_)
  - a box-classification layer (_cls_)
- Note: because the mini-network operates in a sliding-window fashion, the fully-connected layers are shared across all spatial locations
- This architecture is naturally implemented with an $n\times n$ convolutional layer followed by two sibling $1 \times 1$ convolutional layers (for _reg_ and _cls_, respectively)

### Anchors

- At each sliding-window location, we simultaneously predict multiple region proposals,
  - where the number of maximum possible proposals for each location is denoted as $k$.
- So the _reg_ layer has $4k$ outputs encoding the coordinates of $k$ boxes, and the _cls_ layer outputs $2k$ scores that estimate probability of object or not object for each proposal
  - the _cls_ layer is implemented as a two class softmax layer, alternatively a single logistic regression unit can be used to produce $k$ scores
- The $k$ proposals are parameterized relative to $k$ reference boxes, which we call anchors
- An anchor is centered at the sliding window in question, and is associated with a scale and aspect ratio
- By default we use 3 scales and 3 aspect ratios, yielding $k = 9$ anchors at each sliding position. For a convolutional feature map of a size $W \times H$ (typically $\sim 2400$), there are $WHk$ anchors in total

Multi-Scale Anchors as Regression References

- Our design of anchors presents a novel scheme for addressing multiple scales (and aspect ratios)
- As shown in Figure 1, there have been two popular ways for multi-scale predictions.
  !\[\[Pasted image 20231003173212.png\]\]
- The first way (b) is based on image/feature pyramids, e.g., in DPM \[8\] and CNNbased methods
  - The images are resized at multiple scales, and feature maps (HOG \[8\] or deep convolutional features) are computed for each scale (Figure 1(a)). This way is often useful but is time-consuming.
- The second way is to use sliding windows of multiple scales (and/or aspect ratios) on the feature maps. For example, in DPM \[8\], models of different aspect ratios are trained separately using different filter sizes (such as 5×7 and 7×5). If this way is used to address multiple scales, it can be thought of as a “pyramid of filters” (Figure 1(b)).
- The second way is usually adopted jointly with the first way \[8\]. As a comparison, our anchor-based method is built on a pyramid of anchors, which is more cost-efficient.
- Our method classifies and regresses bounding boxes with reference to anchor boxes of multiple scales and aspect ratios.
- It only relies on images and feature maps of a single scale, and uses filters (sliding windows on the feature map) of a single size.
- We show by experiments the effects of this scheme for addressing multiple scales and sizes (Table 8).
- Because of this multi-scale design based on anchors, we can simply use the convolutional features computed on a single-scale image, as is also done by the Fast R-CNN detector.
- The design of multiscale anchors is a key component for sharing features without extra cost for addressing scales.

### Loss Function

- For training RPNs, we assign a binary class label (of being an object or not) to each anchor
- We assign a positive label to two kinds of anchors:
  - (i) the anchor/anchors with the highest Intersection-overUnion (IoU) overlap with a ground-truth box, or
  - (ii) an anchor that has an IoU overlap higher than 0.7 with any ground-truth box.
  - Note: that a single ground-truth box may assign positive labels to multiple anchors. Usually the second condition is sufficient to determine the positive samples; but we still adopt the first condition for the reason that in some rare cases the second condition may find no positive sample. We assign a negative label to a non-positive anchor if its IoU ratio is lower than 0.3 for all ground-truth boxes. Anchors that are neither positive nor negative do not contribute to the training objective. With these definitions, we minimize an objective function following the multi-task loss in Fast R-CNN \[2\]. Our loss function for an image is defined as:
    $$
    L({p_i},{t_i}) = \frac{1}{N_{cls}}\sum_iL_{cls}(p_i, p_i^*) + \lambda\frac{1}{N_{reg}}\sum p_i^* L_{reg}(t_i, t_i^\*)
    $$

## Fast RCNN
