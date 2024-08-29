---
tags:
- '#area/ai/dl'
---

#### 6.1 Overfitting can be reduced by simplifying the model, using more training data, or regularization

- Regularization is any modification we make to a learning algorithm that is intended to reduce its generalization error but not its training error
- Regularizing a high-capacity model gives better results than using a low-capacity unregularized

#### 6.2 Training data can often be augmented to increase its apparent size

-

#### 6.3 Overfitting can be reduced by training on multiple datasets

- Transfer learning:
  - training your model on a pretrained model that has been trained on a larger, similar dataset
- Self-supervised pre-training
  - initializing your model with parameters from self-supervised learning
  - Self-supervised learning consists of predicting labels that can be calculated automatically from the inputs, so that they do not require manual labelling
- Multi-task learning
  - Training a model to perform multiple tasks provides additional data to constrain shared parts of the model

#### 6.4 Overfitting tends to develop during training, and early stopping can reduce it

- You can implement early stopping by ending gradient descent when the validation loss increases for $p$ iterations in a row

#### 6.5 Parameter norm penalties shrink weights selectively

- L2 regularization can resemble early stopping
  - Early stopping limits weight size because gradient, learning rate, and # steps are bounded
  - These methods can be equivalent if:
    - The task-based loss is quadratic
    - Weights are initialized at origin
- L1 regularization makes weights sparse
  - Sets some weights to zero
  - This can be useful at the input for feature selection, and possibly for more efficient computation, depending on hardware
  - Adds $\\alpha \\text{ sgn}(\\boldsymbol w)$ term to loss

#### 6.6 Dropout is a practical approximation of bagging for large networks

- Training:
  - In each forward/ backward training pass, remove each unit from the network with probability $(1-p)$
  - Rescale outbound weights of other units by $1/p$
- Inference:
  - Include all units and undo weight rescaling
- This approximates bagging in a way that is practical for large models
  - In contrast with bagging:
    - There are as many models as training passes (sampled from $2^{n\_{units}}$ possibilities)
    - Parameters are shared between models
    - Each model sees at most one training example (or batch)
- Inference method approximates averaging over many random network samples

#### 6.7 Batch normalization is also a regularizer

- Although batch norm was intended to simplify optimization, it has also been found to improve generalization
- Batch norm can reduce or eliminate the need for dropout
  - Recall that batch norm prevents updates that increase the activation variance
  - This can reduce growth of weights