---
tags:
  - paper
status: doing
year: 2022/07
authors: Sebastian Starke, Ian Mason, Taku Komura
citekey: 10.1145/3528223.3530178
---
# DeepPhase: periodic autoencoders for learning motion phase manifolds

## Background

- Learning the spatial-temporal structure of body movements is a fundamental problem for character motion synthesis
- In this work, we propose a novel neural network architecture called the Periodic Autoencoder that can learn periodic features from large unstructured motion datasets in an unsupervised manner
- The character movements are decomposed into multiple latent channels that capture the non-linear periodicity of different body segments while progressing forward in time
- Our method extracts a multi-dimensional phase space from full-body motion data, which effectively clusters animations and produces a manifold in which computed feature distances provide a better similarity measure than in the original motion space to achieve better temporal and spatial alignment
- We demonstrate that the learned periodic embedding can significantly help to improve neural motion synthesis in a number of tasks, including diverse locomotion skills, style-based movements, dance motion synthesis from music, synthesis of dribbling motions in football, and motion query for matching poses within large animation databases.

### Problem

- Learning the spatial-temporal structure of body movements is a fundamental problem for character motion synthesis
    - allows for the interpolation of motion data and the production of realistic transitions within and between different types of motions
- **Motion space**: a field where each sample in the space is collected from motion capture data
    - Modeling the motion space can be important to various tasks in motion prediction, synthesis and control

- Problematic properties of the motion space:
    - sparse (ex. mocap data)
    - highly non-linear structure
    
- Problems in practice:
    - sparsity makes modelling the interpolations or transitions between different motion types difficult
    - when updating the character state by interpolation, samples forwards and backwards states causing stagnation in the character
    - transitioning to far-away states causes updates to diverge to spaces w no samples [could be related to BEAR](2_concepts/bootstrapping%20error%20reduction.md)


### Goals / Contributions

- Data-driven models for character control tasks may produce **over-smoothed** or **erratic** movements because the **similarity in the motion space does not generally represent their similarity in time**
- This work focuses on the local periodicity of character motion both in time and in space

- **Goal:** to construct a latent space using an encoder and then applying a frequency domain conversion as an inductive bias

- **Contributions:**
    1. Periodic Autoencoder: transforms unstructured character movements (unsupervised) into a **periodic manifold** that effectively represents the alignment of full-body motion in space and time
    2. Demonstration with biped/quadriped locomotion (stylistic movements, dribbling, dance, effective motion query in motion matching?)
    3. Evaluation of learned phase space in comparison with SOTA animation

### Past Work

- Methods to learn continuous spaces have been proposed, though they often suffer from smoothed-out motions and poor responsiveness.
- Motion Synthesis in Frequency Domain
    - these methods mostly apply edits to each degree of freedom, and do not compute features that represent the correlation of different parts of the body
    - 

## Methodology

> [! abstract]
> 
> - Periodic Autoencoder (PAE): full-body motion data -> multi-dimensional phase space
>     - produces a manifold where feature distance is a better similarity measure
>     - helps achieve better spatio-temporal alignment
> - During training, each latent phase channel becomes tuned for different local movements and essentially acts as a band-pass filter for different ranges of learned frequency and amplitude values
> 

![Periodic Autoencoder](2_concepts/media/Pasted%20image%2020241029153154.png)

- Given $\mathbf{X} \in \mathbb R^{D\times N}$ where:
    - $D$: DOF in body
    - $N$: Number of frames
- train encoder, $g$, to learn $\mathbf L = g(\mathbf X)$, where:
    - $\mathbf L \in \mathbb R^{M\times N}$: latent representation with $M$ latent channels
- 


## Results

> [!abstract]

-  demonstrate that the learned periodic embedding can significantly enhance data-driven character animation for a number of tasks, including diverse locomotion skills, stylized movements, dance motion synthesis from music, synthesis of dribbling motion in football
- We show benefits of using our learned phase manifold when generating such motions with neural character con- trollers, as well as when applied to motion query tasks for matching poses within large animation databases in order to scale with the growing amounts of motion data available

## Comments and Implications

- 
