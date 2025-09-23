---
tags:
  - "area"
  - "app/object-detection"
---
# What is Object Detection?

- In image classification, we simply predict whether or not a class exists within an image
- In image detection, we must predict where instances of classes are located within an image using bounding boxes
- Before the [R-CNN](rcnn.md) [paper](https://arxiv.org/pdf/1311.2524.pdf), the two most successful methods for generating bounding boxes were to use a [regression CNN](https://papers.nips.cc/paper_files/paper/2013/hash/f7cade80b7cc92b991cf4d2806d6bd78-Abstract.html), and others used a sliding window detector
  - The sliding window detector led to units deep in the network to have very large receptive fields and strides in the input image, which makes precise localization an open technical challenge