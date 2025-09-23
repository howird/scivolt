---
tags:
  - paper
status: backlog
year: 2018/01
authors: Jiankang Deng, Jia Guo, Jing Yang, Niannan Xue, Irene Kotsia, Stefanos Zafeiriou
citekey: ArcFace
---
# ArcFace: Additive Angular Margin Loss for Deep Face Recognition

## Background

- Recently, a popular line of research in face recognition is adopting margins in the well-established softmax loss function to maximize class separability
- In this paper, we first introduce an Additive Angular Margin Loss (ArcFace), which not only has a clear geometric interpretation but also significantly enhances the discriminative power
- Since ArcFace is susceptible to the massive label noise, we further propose sub-center ArcFace, in which each class contains $K$ sub-centers and training samples only need to be close to any of the $K$ positive sub-centers
- Sub-center ArcFace encourages one dominant sub-class that contains the majority of clean faces and non-dominant sub-classes that include hard or noisy faces
- Based on this self-propelled isolation, we boost the performance through automatically purifying raw web faces under massive real-world noise
- Besides discriminative feature embedding, we also explore the inverse problem, mapping feature vectors to face images
- Without training any additional generator or discriminator, the pre-trained ArcFace model can generate identity-preserved face images for both subjects inside and outside the training data only by using the network gradient and Batch Normalization (BN) priors
- Extensive experiments demonstrate that ArcFace can enhance the discriminative feature embedding as well as strengthen the generative face synthesis.

### Problem

- 

### Goals / Contributions

- 

### Past Work

- 

## Methodology

> [! abstract]

- 

## Results

> [!abstract]

- 

## Comments and Implications

- 
