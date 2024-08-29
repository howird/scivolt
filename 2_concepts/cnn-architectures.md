---
status: backlog
tags:
  - '#ai/dl'
---

#### 8.1 The earliest convolutional networks were LeNets, developed for handwritten digit recognition

#### 8.2 AlexNet ignited interest in deep learning by combining convolutional networks with GPUs and big data

See [AlexNet](8.2-alexnet.md)

#### 8.3 VGG networks added simplicity and depth

- Compared to AlexNet
  - Smaller kernels (3x3 throughout)
  - More parameters (VGG-16 has 138M vs. 60M for AlexNet)
  - Similar otherwise (alternating convolution and max-pooling layers, increasing numbers of channels, a few fully-connected layers at the end)
- Main ideas: depth, small kernels

#### 8.4 Inception networks introduced parallel paths with different kernel sizes

- Fewer parameters because:
  - Fewer channels per path, fewer large kernels
  - Smaller fully-connected layers
- Fewer parameters reduces overfitting and computation
- Between Inception modules are max-pooling layers with stride 2, to reduce feature-map dimension
- Auxiliary classifiers try to classify images using mid-level features, to improve propagation of errors deep into the network (this helps performance slightly)

#### 8.5 All-convolutional networks removed max-pooling and fully connected layers

- Eliminated some standard parts of convolutional networks
  - Found that max pooling could be replaced with an additional strided convolutional layer without loss of accuracy
  - Also replaced fully-connected layers with 1x1 convolutions and global average pooling

#### 8.6 ResNets added residual connections to facilitate training of very deep networks

- The main idea is to incorporate “skip connections” in parallel with blocks of convolutional layers, which pass on the previous layer’s outputs unchanged
- Input
  - If the ideal mapping in a part of the network is $f(x)$, the network must then learn $f(x)-x$, which may be easier
  - gradients get passed deeper into the network
  - can learn to use fewer layers by learning the identity function

#### 8.7 DenseNets included all possible skip connections

- DenseNet carried this idea to an extreme:
  - Each layer gets input from all previous layers
  - Each of these paths is combined by concatenation (rather than summation)
- Similar performance to ResNets with fewer parameters and floating-point operations

#### 8.8 Squeeze & excitation networks applied a channel-wise gain that was input-dependent and learned

## ![](Pasted%20image%2020231218022422.png)

#### 8.9 MobileNets were optimized for edge computing

- Literally just watch [THIS!](https://www.youtube.com/watch?v=vVaRhZXovbw)
- Replaces a standard convolutional layer with depth-wise convolution
- Nearly 9x more efficient with 3x3 kernels

#### 8.10 EfficientNet used a scaling heuristic

- Intuition:
  - Given a baseline network, previous approaches had improved performance by scaling up depth (# layers) or width (# channels) or less commonly resolution
  - Maybe better to scale all three up together, e.g., higher resolution may require more depth to increase the receptive field size and more width to model a greater variety of fine-grained patterns
  - Start with an optimized small network
  - Scale depth, width, and resolution together with an empirical ratio
    ![](Pasted%20image%2020231218030131.png)
    ![](Pasted%20image%2020231218030147.png)

#### 8.11 U-Net combined low and high-level features to produce structured output

- Contractive and expansive parts:
- Expansive section: Upsampling via convolution
  - Shortcut connections combine lower and higher- level features
    ![](Pasted%20image%2020231218030310.png)

#### 8.12 Convolutional networks continue to improve
