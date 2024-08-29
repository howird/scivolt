---
tags:
- '#area/ai/dl'
---

#### 7.1 Convolution is related to correlation

- Convolution
  $$
  (f * g)\[k\] = \\sum\_{m=1}^M f\[k - m\]g\[m\]
  $$

- Cross-correlation
  $$
  (f \\star g)\[k\] = \\sum\_{m=1}^M f\[k + m\]g\[m\]
  $$

#### 7.2 Convolution emphasizes features that are like the kernel

#### 7.3 Convolution is linear

#### 7.4 Convolution is less general than matrix multiplication

#### 7.5 Convolutional layers work with signals, images, and volumes

#### 7.6 Convolutional layers have multiple channels

#### 7.7 Something must be done about the edges

#### 7.8 Convolutional layers are efficient in terms of computation and parameters

- This approach implicitly assumes that:
  - The most useful and/or consistent low-level features of an image are small
  - Input statistics are similar in different parts of the input

#### 7.9 Stride and dilation subsample in different ways

#### 7.10 Pooling layers introduce translation invariance