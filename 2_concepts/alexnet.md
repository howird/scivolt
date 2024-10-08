---
date: June 15, 2022
status: backlog
tags:
  - '#ai/dl'
---

# AlexNet

I'll be going over [AlexNet](https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf),
one of the most influential papers on Convolutional Neural Networks

- Designed by Alex Krizhevsky with Ilya Sutskever and Geoffrey Hinton in 2012
- Achieved state of the art results on the LSVRC-2010 ImageNet

## Architecture Design Choices

- From afar, AlexNet can just be seen as a larger version of [LeNet](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf)
- However, there are various advancements made in its architecture that led to significant improvements in performance

### Nonlinearity

- The [__ReLU__](https://machinelearningmastery.com/rectified-linear-activation-function-for-deep-learning-neural-networks/) function was chosen over
  the $\tanh$ function as the nonlinear activation
- Unlike the $\text{sigmoid}$ or $\tanh$ functions, $\text{ReLU}$ does not __saturate__:
  - In this context, saturation is when functions output values close to their __asymptotic ends__
  - Saturation squashes the derivative leading to smaller steps taken during gradient descent $\implies$ slower training
  - $\text{ReLU}$ enables faster training which is especially important when training large models on large datasets

![](fn_compare.png#center){width=70%}

- Notice from the above plot, as $x \rightarrow \infty$:

  - $\text{ReLU}(x) \rightarrow \infty$, while $\tanh(x)$ and $\text{sigmoid}(x)$ $\rightarrow 1$ (saturates)
  - Additionally, $\frac d{dx}\text{ReLU}(x)=1$, while $\frac d{dx}\tanh(x)\rightarrow 0$
  - Therefore, when performing gradient descent, at large values of $x$, $\frac d{dx}\tanh(x)$ will produce smaller gradients leading to slower training

- Additionally, $\text{ReLU}$ does not require input normalization since it does not saturate at large inputs

- As long as inputs produce a positive input to the function, it can learn

### Local Response Normalization

- As previously mentioned, while using the $\text{ReLU}$ function does not require normalization, the authors did implement some normalization in the following form
- Essentially, each activation that is output by the convolution layer is normalized by the activations of the units surrounding itself
- This is done with the following equation where the normalized activation is $b^i_{x,y}$, the original activation is $a^i_{x,y}$, and $k$, $n$, $\alpha$, and $\beta$ are hyperparameters

$$
b^i_{x,y} = a^i_{x,y} / (k + \alpha \sum_{\max(0, i-n/2)}^{\max(0, i-n/2)})^\beta
$$

- This is similar to [Jarret et Al. 2011](https://ieeexplore.ieee.org/document/5459469), however, in that normalization method, the mean of the surrounding activations is subtracted to get the output activation
  - this can be interpreted as a contrast normalization, while AlexNet's method is more of a brightness normalization
- The optimal hyperparameters were found to be $k=2$, $n=5$, $\alpha=10^{-4}$, and $\beta=0.75$ through testing on validation sets
- This led to a reduction in top-1 and top-5 error rates by 1.4% and 1.2%, respectively
			
### Overlapping Pooling

- Max Pool layers traditionally use a stride that matches the size of the kernel, however, the authors of AlexNet chose to have a smaller stride leading to __overlapping pooling__
- The authors' experimentation found that overlapping pooling made it less likely for the model to overfit
- Changing from a kernel size of $(2, 2)$ and stride of $2$ to a kernel size of $(3, 3)$ and stride of $2$ reduces the top-1 and top-5 error rates by $0.4\%$ and $0.3\%$, respectively

### Architecture

![AlexNet Architecture](https://www.researchgate.net/profile/Nicola-Strisciuglio/publication/339756908/figure/fig5/AS:866265283457032@1583545146587/AlexNet-architecture-used-as-the-baseline-model-for-the-analysis-of-results-on-the.png#center){ width=100% }
