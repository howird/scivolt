---
tags:
  - paper
  - ai/selfsup-learning
status: todo
year: 2021/05
authors: Mathilde Caron, Hugo Touvron, Ishan Misra, Hervé Jégou, Julien Mairal, Piotr Bojanowski, Armand Joulin
citekey: caronEmergingPropertiesSelfSupervised2021
---
# Emerging Properties in Self-Supervised Vision Transformers

#### Introduction & Purpose
## Objective: 

- GOAL: Investigate whether self-supervised learning introduces new properties in Vision Transformers (ViTs) that are distinct from convolutional networks (convnets)
- Proposes a self-supervised method called DINO (self-Distillation with NO labels) and evaluates its synergy with ViTs
- Aims to understand how self-supervised ViTs compare to supervised ViTs and convnets in feature quality and downstream tasks

#### Key Findings & Contributions

- Unsupervised Object Segmentation: Self-supervised ViTs learn explicit semantic segmentation features, which do not emerge as clearly in supervised ViTs or convnets
- Strong k-NN Classifier Performance: Self-supervised ViT features achieve 78.3% top-1 accuracy on ImageNet using a simple k-NN classifier without fine-tuning.
- DINO’s Effectiveness: The DINO framework, based on self-distillation, achieves 80.1% top-1 accuracy in linear evaluation on ImageNet using ViT-Base.
- Critical Components for Success:
    - Momentum Encoder: Crucial for self-supervised learning stability
    - Multi-Crop Training: Enhances performance significantly
    - Small Patch Sizes: Improve feature quality in ViTs

#### Recommended Prerequisite Papers

To fully understand the context and background of this paper, familiarity with the following works is recommended:

- Dosovitskiy et al. (2020) - "An Image is Worth 16x16 Words" (Introduction of ViTs)
- He et al. (2020) - "Momentum Contrast for Unsupervised Visual Representation Learning" (MoCo)
- Chen et al. (2020) - "A Simple Framework for Contrastive Learning of Visual Representations" (SimCLR)
- Grill et al. (2020) - "Bootstrap Your Own Latent (BYOL)" (Self-distillation framework similar to DINO)
- Caron et al. (2020) - "Unsupervised Learning of Visual Features by Contrasting Cluster Assignments" (SwAV)

## 1. Problem Definition

### 1.1 Goal

- Train Vision Transformers (ViTs) using self-supervised learning (SSL) without any labeled data
- Explore emergent properties in self-supervised ViTs, particularly in feature learning and semantic segmentation
- Introduce DINO, a self-distillation approach that matches a student network to a dynamically evolving teacher network

### 1.2 Why Self-Supervised Learning for ViTs?

- Unlike supervised learning, SSL does not reduce an image to a single category but learns rich visual representations
- ViTs are typically data-hungry; SSL can enable them to generalize better with less labeled data
- Self-supervised training allows for the discovery of semantic object boundaries without explicit annotations

## 2. Self-Distillation without Labels (DINO)

The DINO framework builds on knowledge distillation but does not require labeled data.

### 2.1 Model Components

- Student Network $g_{\theta_s}$ (parameters: $\theta_s$)
- Teacher Network $g_{\theta_t}$ (parameters: $\theta_t$)
- **Input Image $x$** and its different **augmented views** $(x_1, x_2, ..., x_v)$

Both networks have the same architecture but different parameters.

### 2.2 Objective Function

The student network is trained to match the output distribution of the teacher network using cross-entropy loss:
$$
\mathcal{L} = \sum_{x \in {x_1, x_2, ..., x_v}} \sum_{x' \in V, x' \neq x} H(P_t(x), P_s(x'))
$$
where:

- $P_t(x)$ is the output of the teacher network.
- $P_s(x')$ is the output of the **student** network for a different view $x'$.
- $H(a, b)$ represents the cross-entropy loss between probability distributions.

### 2.3 Softmax Output and Temperature Scaling

Each network produces a probability distribution over K dimensions using temperature-scaled softmax:
$$
P_s(x)^{(i)} = \frac{\exp(g_{\theta_s}(x)^{(i)} / \tau_s)}{\sum_{k=1}^{K} \exp(g_{\theta_s}(x)^{(k)} / \tau_s)}
$$
where:

- $\tau_s$ and $\tau_t$ are temperature parameters controlling the sharpness of the probability distribution.
- The same formulation holds for the teacher: $P_t(x)$ with temperature $\tau_t$.

### 2.4 Teacher Updates Using Exponential Moving Average (EMA)

Unlike traditional knowledge distillation, where the teacher is fixed, here the teacher network evolves by computing an exponential moving average (EMA) of the student:
$$
\theta_t \leftarrow \lambda \theta_t + (1 - \lambda) \theta_s
$$
where:

- $\lambda$ is a momentum parameter (increasing from 0.996 to 1 during training).
- Ensures the teacher is a slowly updated version of the student.

---

## 3. Self-Supervised Training Procedure

### 3.1 Multi-Crop Augmentation

- Each image is transformed into multiple global and local views:
- 2 global views $(224 \times 224)$ covering >50% of the image.
- 6-10 local views $(96 \times 96)$ covering <50% of the image.
- The teacher receives only global views, while the student processes both global and local views.

### 3.2 Avoiding Collapse

A key challenge in self-supervised learning is collapse, where the network outputs the same representation for all images.

#### 3.2.1 Centering and Sharpening

To prevent collapse, DINO applies:

- Centering to prevent one feature dominating:
$$
c \leftarrow m c + (1 - m) \frac{1}{B} \sum_{i=1}^{B} g_{\theta_t}(x_i)
$$
where $m$ is an exponential moving average parameter.
- Sharpening by adjusting the temperature $\tau_t$, ensuring the teacher’s outputs are not overly smooth.

---

## 4. Vision Transformer (ViT) as the Backbone

### 4.1 Patch-Based Processing

- ViT splits an image into non-overlapping patches $p \times p$.
- Each patch is embedded via a linear projection layer and combined with position embeddings.
- Self-attention layers compute global dependencies across patches.

### 4.2 Self-Attention Properties

- The $CLS$ token in the last self-attention layer encodes global image information.
- Self-supervised ViTs naturally learn object boundaries, leading to unsupervised segmentation

---

## 5. Experimental Setup

### 5.1 Dataset

- Pretraining: ImageNet-1K (without labels).
- Evaluation: ImageNet linear classification, k-NN classification, segmentation tasks.

### 5.2 Evaluation Metrics

- Linear probing: Train a linear classifier on frozen features.
- k-NN classification: Evaluate how well nearest neighbors match class labels.
- Semantic segmentation: Check how well self-attention maps align with object boundaries.

### 5.3 Comparison with Other SSL Methods

- MoCo v2: Contrastive learning with a memory bank.
- BYOL: Self-distillation without contrastive loss.
- SwAV: Cluster-based contrastive learning.
- DINO’s Advantage: No need for contrastive loss or a memory bank.

---

## 6. Key Findings

- ViTs in SSL outperform convnets in segmentation.
- DINO-trained ViTs match supervised ViTs on classification tasks.
- k-NN accuracy (78.3%) is close to linear probe accuracy (80.1%), indicating strong feature quality.
- ViTs learn high-quality representations without requiring labels.

---

## Conclusion

The DINO framework unlocks the potential of self-supervised ViTs by:

1. Leveraging self-distillation without contrastive learning.
2. Using multi-crop augmentation for better generalization.
3. Allowing ViTs to discover object boundaries naturally.
4. Achieving state-of-the-art performance in self-supervised learning.

This problem formulation outlines how DINO combines knowledge distillation with self-supervised training to produce high-quality features in Vision Transformers, paving the way for future research in unsupervised visual representation learning.

Would you like further elaboration on any section, such as the implementation details or mathematical derivations?


You:
can you please create a detailed pipeline explaining the implementation of the project mentioned in this paper?
each stage in the pipeline should have descriptions of the inputs and outputs, including their shapes if they are tensors, use latex for math

ChatGPT:
### Implementation Pipeline for Self-Supervised Vision Transformers (DINO)

This pipeline provides a structured step-by-step explanation of how to implement the DINO framework for self-supervised learning in Vision Transformers (ViTs). Each stage includes input/output tensor shapes and a detailed explanation.

---

## 1. Data Preprocessing & Augmentation

### 1.1 Input Image & Multi-Crop Augmentation

#### Input:

- Raw image $x \in \mathbb{R}^{H \times W \times C}$, typically $224 \times 224 \times 3$ for ImageNet.
- Batch of images $X \in \mathbb{R}^{B \times H \times W \times C}$.

#### Processing:

1. Generate two global views:
$$
x_g^1, x_g^2 \in \mathbb{R}^{H \times W \times C}
$$
where $H = W = 224$.
1. Generate several local views:
$$
x_l^i \in \mathbb{R}^{h \times w \times C}, \quad \text{where } h, w < H, W.
$$
1. The total set of views:
$$
V = {x_g^1, x_g^2, x_l^1, x_l^2, ..., x_l^n}
$$
where $n$ typically ranges from 6 to 10.

#### Output:

- Multi-crop augmented batch:
$$
X_{\text{aug}} \in \mathbb{R}^{(B \times (2 + n)) \times h' \times w' \times C}
$$
where $h', w'$ vary based on crop type.

---

## 2. Vision Transformer (ViT) Feature Extraction

### 2.1 Tokenization (Patch Embedding)

#### Input:

- Image $x \in \mathbb{R}^{H \times W \times C}$.
- Patch size $p \times p$ (e.g., $16 \times 16$).

#### Processing:

2. Split image into $N = \frac{H}{p} \times \frac{W}{p}$ patches:
$$
X_{\text{patches}} \in \mathbb{R}^{B \times N \times (p^2 \cdot C)}
$$
3. Apply a linear projection:
$$
Z_{\text{embed}} = W_e X_{\text{patches}} + b_e
$$
where $W_e$ is the projection matrix, giving:
$$
Z_{\text{embed}} \in \mathbb{R}^{B \times N \times D}
$$
with $D$ as the embedding dimension (e.g., 384 for ViT-Small).
4. Add a $CLS$ token:
$$
Z_{\text{input}} = \text{CLS}\oplus Z_{\text{embed}} + P_{\text{pos}}
$$
where $P_{\text{pos}}$ are position embeddings.

#### Output:

- Patch embeddings:
$$
Z_{\text{input}} \in \mathbb{R}^{B \times (N+1) \times D}
$$

---

## 3. Vision Transformer Forward Pass

### 3.1 Self-Attention Mechanism

#### Input:

- Patch embeddings $Z_{\text{input}}$

#### Processing:

5. Compute query (Q), key (K), and value (V):
$$
Q = W_Q Z_{\text{input}}, \quad K = W_K Z_{\text{input}}, \quad V = W_V Z_{\text{input}}
$$
where $W_Q, W_K, W_V$ are learnable projection matrices

6. Compute self-attention scores:
$$
A = \text{softmax} \left( \frac{QK^T}{\sqrt{D}} \right) V
$$

7. Pass through multi-head self-attention and feed-forward layers.

8. Extract $CLS$ token representation
$$
Z_{\text{CLS}} \in \mathbb{R}^{B \times D}
$$

#### Output:

- Final feature representation:
$$
Z_{\text{CLS}} \in \mathbb{R}^{B \times D}
$$

---

## 4. DINO Training (Self-Distillation)

### 4.1 Student & Teacher Networks

- Student network $g_{\theta_s}$: Standard ViT trained with gradient descent.
- Teacher network $g_{\theta_t}$: An exponential moving average (EMA) of the student.

#### 4.2 Softmax-Based Output with Temperature Scaling

For each input image $x$, the networks output:
$$
P_s(x) = \text{softmax} \left( \frac{g_{\theta_s}(x)}{\tau_s} \right), \quad P_t(x) = \text{softmax} \left( \frac{g_{\theta_t}(x)}{\tau_t} \right)
$$
where:

- $\tau_s$ and $\tau_t$ are temperature parameters.

#### 4.3 Cross-Entropy Loss

The student is trained to match the teacher’s predictions using:
$$
\mathcal{L} = \sum_{x \in V} \sum_{x' \in V, x' \neq x} H(P_t(x), P_s(x'))
$$
where $H(a, b)$ is the cross-entropy loss.

#### 4.4 Teacher Network Update (EMA)

$$
\theta_t \leftarrow \lambda \theta_t + (1 - \lambda) \theta_s
$$
where $\lambda$ follows a cosine schedule from 0.996 to 1.

---

## 5. Feature Evaluation & Transfer Learning

### 5.1 k-NN Classification

- Store frozen $CLS$ token features $Z_{\text{CLS}}$.
- Use weighted k-nearest neighbor (k-NN) classifier:
$$
y = \sum_{i \in kNN(x)} w_i y_i
$$
where $w_i = e^{Z_{\text{CLS}} \cdot Z_i}$.

### 5.2 Linear Probing

- Train a linear classifier on top of frozen features:
$$
\hat{y} = W_{\text{linear}} Z_{\text{CLS}} + b
$$
where $W_{\text{linear}}$ is learned with SGD.

---

## Final Summary of the Pipeline

| Stage                 | Input Shape | Output Shape                                      | Description |
| --------------------- | ----------- | ------------------------------------------------- | ----------- |
| 1. Data Augmentation  | $B \times 224 \times 224 \times 3$ | $B \times (2 + n) \times h' \times w' \times 3$        | Multi-crop global and local views                 |             |
| 2. ViT Tokenization   | $B \times 224 \times 224 \times 3$ | $B \times (N+1) \times D$        | Split image into patches and add embeddings       |             |
| 3. ViT Forward Pass   | $B \times (N+1) \times D$ | $B \times D$        | Self-attention and feature extraction             |             |
| 4. DINO Training      | $B \times D$ | $B \times K$        | Train student network to match teacher network    |             |
| 5. Feature Evaluation | $B \times D$ | $B \times 1$        | Classify images using k-NN or a linear classifier |             |

---

### Conclusion

This pipeline describes how DINO self-supervised learning is implemented in Vision Transformers. By leveraging self-distillation, multi-crop training, and momentum-based teacher updates, DINO enables ViTs to learn powerful unsupervised features. This method achieves state-of-the-art performance on tasks such as image classification, retrieval, and segmentation without requiring labels.

