---
aliases:
  - 'AMP'
  - 'pengAMPAdversarialMotion2021'
authors: 'Xue Bin Peng, Ze Ma, Pieter Abbeel, Sergey Levine, Angjoo Kanazawa'
citekey: 'pengAMPAdversarialMotion2021'
status: backlog
tags:
  - '#paper'
title: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control'
url: ''
year: '2021/08'
---

# AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control

> [!abstract]
> Synthesizing graceful and life-like behaviors for physically simulated characters has been a fundamental challenge in computer animation. Data-driven methods that leverage motion tracking are a prominent class of techniques for producing high fidelity motions for a wide range of behaviors. However, the effectiveness of these tracking-based methods often hinges on carefully designed objective functions, and when applied to large and diverse motion datasets, these methods require significant additional machinery to select the appropriate motion for the character to track in a given scenario. In this work, we propose to obviate the need to manually design imitation objectives and mechanisms for motion selection by utilizing a fully automated approach based on adversarial imitation learning. High-level task objectives that the character should perform can be specified by relatively simple reward functions, while the low-level style of the character's behaviors can be specified by a dataset of unstructured motion clips, without any explicit clip selection or sequencing. These motion clips are used to train an adversarial motion prior, which specifies style-rewards for training the character through reinforcement learning (RL). The adversarial RL procedure automatically selects which motion to perform, dynamically interpolating and generalizing from the dataset. Our system produces high-quality motions that are comparable to those achieved by state-of-the-art tracking-based techniques, while also being able to easily accommodate large datasets of unstructured motion clips. Composition of disparate skills emerges automatically from the motion prior, without requiring a high-level motion planner or other task-specific annotations of the motion clips. We demonstrate the effectiveness of our framework on a diverse cast of complex simulated characters and a challenging suite of motor control tasks.

## 3-pass method

### Pass 1

> [!info]
>
> - carefully read title, abstract, intro
> - read all headings and subheadings
> - check references for papers that you have read
> - make any relevant comments on the following:
>   - Category: What type of paper is this? A measurement paper? An analysis of an existing system? A description of a research prototype?
>   - Context: Which other papers is it related to? Which theoretical bases were used to analyze the problem?
>   - Correctness: Do the assumptions appear to be valid?
>   - Contributions: What are the paper’s main contributions?
>   - Clarity: Is the paper well written?

#### Abstract & Introduction Summary

-

#### Additional Comments

-

#### Questions to Answer in Following Passes

-

### Pass 2

> [!info]
> Pass 2 (1 hour):
>
> - understand figures, graphs, looking for errors
> - read paper with greater care but skip proofs
> - note other significant references you may want to read

### Pass 3

> [!info]
> Pass 3 (5 hours):
>
> - essentially re-implement the entire paper
> - identify assumptions in the paper and challenge them
> - consider how you would present each idea

- [INSERT GIT REPO HERE](www.github.com)
  - comment code and make PR

## Distillation

> [!info]
> After the 2/3 pass method try and copy and paste the above notes and present them in a more structured manner

### Problem

-

### Key Points

-

### Methodology

-

### Results

-

### Comments and Implications

-
