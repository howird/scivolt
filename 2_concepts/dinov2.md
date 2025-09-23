---
tags:
  - paper
status: todo
year: 2024/02
authors: Maxime Oquab, Timothée Darcet, Théo Moutakanni, Huy Vo, Marc Szafraniec, Vasil Khalidov, Pierre Fernandez, Daniel Haziza, Francisco Massa, Alaaeldin El-Nouby, Mahmoud Assran, Nicolas Ballas, Wojciech Galuba, Russell Howes, Po-Yao Huang, Shang-Wen Li, Ishan Misra, Michael Rabbat, Vasu Sharma, Gabriel Synnaeve, Hu Xu, Hervé Jegou, Julien Mairal, Patrick Labatut, Armand Joulin, Piotr Bojanowski
citekey: oquabDINOv2LearningRobust2024
---
# DINOv2: Learning Robust Visual Features without Supervision

### Key Advancements Over DINO (Caron et al., 2021)

- Scalability: DINOv2 scales both data and model size, leveraging 1B-parameter ViTs.
- Curated Data: Instead of using uncurated datasets, DINOv2 introduces a high-quality, curated dataset (LVD-142M).
- Training Efficiency: Improved training techniques make DINOv2 2× faster and require 3× less memory than earlier discriminative self-supervised methods.
- Distillation for Smaller Models: Instead of training all models from scratch, DINOv2 distills from a large model (ViT-g) to smaller models, preserving high performance.
- Improved Feature Generalization: DINOv2 outperforms OpenCLIP and other state-of-the-art models on classification, retrieval, and dense prediction tasks.

---

### Perspectives Missing from the Abstract

- Beyond ImageNet-1K: The paper focuses heavily on generalization across multiple vision benchmarks beyond ImageNet.
- Comparison with Contrastive Learning: Unlike previous SSL methods relying on contrastive loss (MoCo, SimCLR), DINOv2 fully embraces self-distillation.
- Scaling Trade-offs: The paper does not explicitly discuss the compute cost trade-offs when training 1B-parameter models vs. smaller architectures.
- Potential Biases: The impact of large-scale self-supervised models on fairness (e.g., geographical and demographic biases) is analyzed but not deeply discussed in the abstract.

---

### Assumptions in the Paper

- Data Curation is Key: The paper assumes that self-supervised models require carefully curated datasets (rather than large uncurated web scrapes like LAION) to learn generalizable features.
- Scaling Enhances Generalization: Increasing both model size and dataset diversity improves zero-shot performance across tasks.
- Distillation Preserves Feature Quality: The assumption that distilling from ViT-g to ViT-L/B does not lead to major degradation in feature quality.
- Frozen Features are Useful: The model assumes that pretrained features without fine-tuning should work well for multiple tasks (classification, segmentation, retrieval).
- SSL Features Can Match Weakly-Supervised Models: The study assumes that self-supervised pretraining alone can match weakly supervised models (e.g., OpenCLIP) without the need for textual labels.

---

### 🔹 Recommended Prerequisite Papers

To fully understand DINOv2, familiarity with the following works is essential:

- Caron et al. (2021) - "Emerging Properties in Self-Supervised Vision Transformers" (DINO)
- Zhou et al. (2022) - "iBOT: Image BERT Pre-training with Online Tokenizer" (Influenced DINOv2’s patch-level objective)
- Caron et al. (2020) - "Unsupervised Learning of Visual Features by Contrasting Cluster Assignments" (SwAV)
- He et al. (2022) - "Masked Autoencoders Are Scalable Vision Learners" (Contrast with Masked Autoencoders - MAE)
- Radford et al. (2021) - "Learning Transferable Visual Models from Natural Language Supervision" (OpenCLIP, for contrast with text-supervised pretraining methods)


### Problem Formulation for DINOv2: Improvements Over DINO

(Focusing on advancements from the original DINO framework)

---

## 1. Problem Definition & Motivation

### 1.1 Goal

- Develop a self-supervised learning (SSL) framework that learns general-purpose, robust visual features.
- Scale self-supervised Vision Transformers (ViTs) to 1B+ parameters for improved feature quality.
- Address the limitations of previous SSL methods (e.g., DINO, iBOT, SwAV) by improving efficiency, training stability, and scalability.

### 1.2 Key Challenges in Scaling SSL for Vision Transformers

- Uncurated Data Leads to Poor Features → Need a curated dataset (LVD-142M) for high-quality features.
- Training Stability Issues at Scale → Requires improved regularization and optimization techniques.
- Computational Cost of Large ViTs → Must improve training efficiency while preserving feature generalization.
- Feature Collapse in Self-Distillation → Need robust centering & sharpening techniques.

---

## 2. Scaling Self-Supervised Learning for Large ViTs

### 2.1 Large-Scale Data Curation (LVD-142M)

- Unlike previous self-supervised models trained on uncurated datasets, DINOv2 uses a curation pipeline.
- Key formulation:
  - Define image embedding function $f(x)$ that maps images to a feature space.
  - Deduplicate images:\
    $$
    \text{similarity}(x_i, x_j) = \frac{f(x_i) \cdot f(x_j)}{|f(x_i)| |f(x_j)|}
    $$
  - Remove near-duplicate images if similarity $> \tau$ (threshold).

---

## 3. Improved Self-Distillation with DINOv2

### 3.1 Optimization Objective

- In DINO, the student model $g_{\theta_s}$ was trained to match the teacher $g_{\theta_t}$ using:\
  $$
  \mathcal{L}_{\text{DINO}} = \sum_{x \in \mathcal{X}} H(P_t(x), P_s(x))
  $$
  where $P_t(x)$ and $P_s(x)$ are softmax outputs with temperature scaling.
- DINOv2 introduces multiple improvements:
  - Sinkhorn-Knopp Centering instead of moving average centering from DINO.
  - Untied projection heads for image-level and patch-level objectives.
  - KoLeo regularization to spread features more uniformly:
    $$
    \mathcal{L}_{\text{KoLeo}} = - \frac{1}{n} \sum_{i=1}^{n} \log \left( \min_{j \neq i} | f(x_i) - f(x_j) | \right)
    $$

---

## 4. Model-Level Improvements for Training Efficiency

### 4.1 Efficient Stochastic Depth

- Unlike DINO, DINOv2 skips computation for dropped residuals, reducing memory usage by up to 40%.
- Mathematical Formulation:
$$
y = x + \text{Drop}(F(x))
$$
  where $\text{Drop}(\cdot)$ randomly drops residual updates instead of masking them.

### 4.2 Sequence Packing for Efficient Attention

- In standard ViTs, small and large patches must be processed separately due to varying sequence lengths.
- DINOv2 concatenates short sequences and uses block-diagonal attention masks:\
  $$
  A_{\text{mask}}(i, j) =
  \begin{cases}
  1, & \text{if } x_i, x_j \text{ belong to the same sequence} \\
  0, & \text{otherwise}
  \end{cases}
  $$
- This avoids redundant computation, speeding up training by 2×.

---

## 5. Knowledge Distillation for Smaller Models

### 5.1 Distilling ViT-g (1.1B params) to ViT-L/B

- In DINO: Each model was trained from scratch.
- In DINOv2:
  - Smaller models are trained from a frozen ViT-g teacher:\
    $$
    \mathcal{L}_{\text{distill}} = H(P_g, P_s)
    $$
  - Leads to better generalization for ViT-L/B models.

---

## 6. High-Resolution Adaptation for Fine-Grained Features

### 6.1 Short High-Resolution Training Phase

- Instead of training at high resolution (512×512) from scratch, DINOv2 finishes training with a short phase at high resolution.
- Reduces compute cost while maintaining fine-grained feature quality.

---

## 7. Conclusion

- Key Improvements Over DINO:
  - Curated Dataset (LVD-142M) → Avoids uncurated data bias.
  - Sinkhorn-Knopp Centering & KoLeo Regularization → Prevents feature collapse.
  - Efficient Stochastic Depth & Sequence Packing → Reduces memory and compute cost.
  - Knowledge Distillation from ViT-g → Enables smaller models to match larger ones.
  - High-Resolution Adaptation Phase → Preserves fine-grained details with minimal compute overhead.


### **Implementation Pipeline for DINOv2**  
*(Focused on improvements over DINO, including scaling, efficiency, and distillation)*  

---

## **Pipeline Overview**  
This section provides a **detailed, structured breakdown** of the implementation pipeline for **DINOv2**, focusing on each processing stage. Inputs, outputs, and tensor shapes are explicitly defined.  

---

## **1. Data Preprocessing & Curation (LVD-142M)**
### **1.1 Input Data**
- Uncurated image dataset **$X_{\text{raw}} \in \mathbb{R}^{B \times H \times W \times C}$**, where:
  - $B$ = batch size
  - $H, W$ = image height and width
  - $C = 3$ (RGB channels)
- **Curated datasets** (ImageNet-22K, Google Landmarks, etc.).

### **1.2 Automatic Data Filtering & Deduplication**
1. Extract image embeddings using **pretrained self-supervised ViT**:  
   $$
   f(x) = g_{\theta}(x), \quad f(x) \in \mathbb{R}^{D}
   $$
   where $D$ is the embedding dimension.
2. Compute cosine similarity between image embeddings:
   $$
   S(x_i, x_j) = \frac{f(x_i) \cdot f(x_j)}{\|f(x_i)\| \|f(x_j)\|}
   $$
3. **Remove duplicates** based on a threshold $\tau$:
   $$
   x_i, x_j \text{ removed if } S(x_i, x_j) > \tau
   $$
4. Perform **balanced dataset re-weighting** to ensure uniform class distribution.

### **1.3 Output**
- **Filtered, curated dataset** $X_{\text{curated}} \in \mathbb{R}^{B' \times H \times W \times C}$ (size $B' \leq B$).

---

## **2. Multi-Crop Augmentation**
### **2.1 Input**
- Image batch $X_{\text{curated}}$.

### **2.2 Processing**
1. Generate **two global crops**:
   $$
   x_g^1, x_g^2 \in \mathbb{R}^{B' \times 224 \times 224 \times 3}
   $$
2. Generate **six to ten local crops**:
   $$
   x_l^i \in \mathbb{R}^{B' \times 96 \times 96 \times 3}, \quad i = 1, ..., n
   $$
3. The final augmented batch:
   $$
   X_{\text{aug}} = \{x_g^1, x_g^2, x_l^1, ..., x_l^n\}
   $$
   where $X_{\text{aug}} \in \mathbb{R}^{(B' \times (2 + n)) \times h' \times w' \times C}$.

### **2.3 Output**
- Multi-view augmented images $X_{\text{aug}}$.

---

## **3. Vision Transformer (ViT) Feature Extraction**
### **3.1 Tokenization (Patch Embedding)**
#### **Input**
- Augmented images $X_{\text{aug}}$.
- Patch size $p \times p$ (e.g., $14 \times 14$).

#### **Processing**
1. Split each image into $N = \frac{H}{p} \times \frac{W}{p}$ patches:
   $$
   X_{\text{patches}} \in \mathbb{R}^{B' \times N \times (p^2 \cdot C)}
   $$
2. Apply a **linear projection** to map patches into **D-dimensional embeddings**:
   $$
   Z_{\text{embed}} = W_e X_{\text{patches}} + b_e, \quad Z_{\text{embed}} \in \mathbb{R}^{B' \times N \times D}
   $$
3. Add a **[CLS] token** and position embeddings:
   $$
   Z_{\text{input}} = [\text{CLS}] \oplus Z_{\text{embed}} + P_{\text{pos}}
   $$

#### **Output**
- Tokenized patches $Z_{\text{input}} \in \mathbb{R}^{B' \times (N+1) \times D}$.

---

## **4. Self-Distillation with DINOv2**
### **4.1 Student & Teacher Networks**
- **Student Network** $g_{\theta_s}$.
- **Teacher Network** $g_{\theta_t}$ (momentum-based update of student).

#### **4.2 Softmax Output with Temperature Scaling**
For each input image $x$, the networks output:
$$
P_s(x) = \text{softmax} \left( \frac{g_{\theta_s}(x)}{\tau_s} \right), \quad P_t(x) = \text{softmax} \left( \frac{g_{\theta_t}(x)}{\tau_t} \right)
$$
where:
- $\tau_s$, $\tau_t$ = temperature parameters.

#### **4.3 Loss Function (DINOv2)**
4. **Image-level Objective (DINO Loss)**:
   $$
   \mathcal{L}_{\text{DINO}} = - \sum P_t(x) \log P_s(x)
   $$
5. **Patch-level Objective (iBOT Loss)**:
   $$
   \mathcal{L}_{\text{iBOT}} = - \sum_{i} P_t(x_i) \log P_s(x_i)
   $$
6. **Regularization (KoLeo Loss)**:
   $$
   \mathcal{L}_{\text{KoLeo}} = - \frac{1}{n} \sum_{i=1}^{n} \log \left( \min_{j \neq i} \| f(x_i) - f(x_j) \| \right)
   $$
7. **Final Loss Function**:
   $$
   \mathcal{L} = \mathcal{L}_{\text{DINO}} + \mathcal{L}_{\text{iBOT}} + \lambda \mathcal{L}_{\text{KoLeo}}
   $$

#### **4.4 Teacher Network Update (EMA)**
$$
\theta_t \leftarrow \lambda \theta_t + (1 - \lambda) \theta_s
$$
where $\lambda$ is momentum (0.994 → 1).

### **4.5 Output**
- Updated student parameters $\theta_s$.
- EMA-updated teacher parameters $\theta_t$.

---

## **5. Feature Evaluation & Knowledge Distillation**
### **5.1 Distilling ViT-g to ViT-L/B**
- Use ViT-g as a **frozen teacher**.
- Train smaller models to minimize:
  $$
  \mathcal{L}_{\text{distill}} = H(P_g, P_s)
  $$

### **5.2 k-NN Classification**
- Store frozen **[CLS] token features** $Z_{\text{CLS}}$.
- Use weighted **k-nearest neighbor (k-NN)** classifier:
  $$
  y = \sum_{i \in kNN(x)} w_i y_i
  $$
  where $w_i = e^{Z_{\text{CLS}} \cdot Z_i}$.

### **5.3 Linear Probing**
$$
\hat{y} = W_{\text{linear}} Z_{\text{CLS}} + b
$$

---

## **Final Summary of the Pipeline**
| **Stage** | **Input Shape** | **Output Shape** | **Description** |
|-----------|---------------|---------------|----------------|
| **Data Curation** | $B \times H \times W \times C$ | $B' \times H \times W \times C$ | Filter and rebalance data |
| **Multi-Crop Augmentation** | $B' \times H \times W \times C$ | $(B' \times (2 + n)) \times h' \times w' \times C$ | Generate multi-view crops |
| **ViT Tokenization** | $B' \times H \times W \times C$ | $B' \times (N+1) \times D$ | Convert images to patch tokens |
| **Self-Distillation** | $B' \times D$ | $B' \times K$ | Train student using teacher network |
| **Feature Evaluation** | $B' \times D$ | $B' \times 1$ | Classify using k-NN or linear probe |

---

### **Would you like PyTorch implementation details or visualization of feature maps? 🚀**