---
aliases:
  - kirillovSegmentAnything2023
authors: Alexander Kirillov, Eric Mintun, Nikhila Ravi, Hanzi Mao, Chloe Rolland, Laura Gustafson, Tete Xiao, Spencer Whitehead, Alexander C. Berg, Wan-Yen Lo, Piotr Dollár, Ross Girshick
citekey: kirillovSegmentAnything2023
status: backlog
tags:
  - '#type/paper'
title: Segment Anything
url: ''
year: 2023/04
---

# Segment Anything

> \[!abstract\]
> We introduce the Segment Anything (SA) project: a new task, model, and dataset for image segmentation. Using our efficient model in a data collection loop, we built the largest segmentation dataset to date (by far), with over 1 billion masks on 11M licensed and privacy respecting images. The model is designed and trained to be promptable, so it can transfer zero-shot to new image distributions and tasks. We evaluate its capabilities on numerous tasks and find that its zero-shot performance is impressive -- often competitive with or even superior to prior fully supervised results. We are releasing the Segment Anything Model (SAM) and corresponding dataset (SA-1B) of 1B masks and 11M images at https://segment-anything.com to foster research into foundation models for computer vision.

# Short Summary

### Key Points

# segment anything model

- SAM has three components, as illustrated:
  - an image encoder,
  - a flexible prompt encoder,
  - a fast mask decoder.
- Image encoder.
- Motivated by scalability and powerful pretraining methods, we use an MAE \[47\] pre-trained Vision Transformer (ViT) minimally adapted to process high resolution inputs \[62\]
- The image encoder runs once per image and can be applied prior to prompting the model. Prompt encoder. We consider two sets of prompts: sparse (points, boxes, text) and dense (masks).
- We represent points and boxes by positional encodings \[95\] summed with learned embeddings for each prompt type and free-form text with an off-the-shelf text encoder from CLIP \[82\].
- Dense prompts (i.e., masks) are embedded using convolutions and summed element-wise with the image embedding.
- Mask decoder. The mask decoder efficiently maps the image embedding, prompt embeddings, and an output token to a mask. This design, inspired by \[14, 20\], employs a modification of a Transformer decoder block \[103\] followed by a dynamic mask prediction head. Our modified decoder block uses prompt self-attention and cross-attention in two directions (prompt-to-image embedding and vice-versa) to update all embeddings. After running two blocks, we upsample the image embedding and an MLP maps the output token to a dynamic linear classifier, which then computes the mask foreground probability at each image location. Resolving ambiguity. With one output, the model will average multiple valid masks if given an ambiguous prompt. To address this, we modify the model to predict multiple output masks for a single prompt (see Fig. 3). We found 3 mask outputs is sufficient to address most common cases (nested masks are often at most three deep: whole, part, and subpart). During training, we backprop only the minimumloss \[15, 45, 64\] over masks. To rank masks, the model predicts a confidence score (i.e., estimated IoU) for each mask. Efficiency. The overall model design is largely motivated by efficiency. Given a precomputed image embedding, the prompt encoder and mask decoder run in a web browser, on CPU, in ∼50ms. This runtime performance enables seamless, real-time interactive prompting of our model. Losses and training. We supervise mask prediction with the linear combination of focal loss \[65\] and dice loss \[73\] used in \[14\]. We train for the promptable segmentation task using a mixture of geometric prompts (for text prompts see §7.5). Following \[92, 37\], we simulate an interactive setup by randomly sampling prompts in 11 rounds per mask, allowing SAM to integrate seamlessly into our data engine.

## Details

### Image encoder

- In general, the image encoder can be any network that outputs a $C\times H\times W$ image embedding

- Motivated by scalability and access to strong pre-training, we use an MAE \[47\] pre-trained Vision Transformer (ViT) \[33\] with minimal adaptations to process high resolution inputs, specifically a ViT-H/16 with $14\times 14$ windowed attention and four equally-spaced global attention blocks, following \[62\]

- The image encoder’s output is a $16\times$ downscaled embedding of the input image. Since our runtime goal is to process each prompt in real-time, we can afford a high number of image encoder FLOPs because they are computed only once per image, not per prompt. Following standard practices (e.g., \[40\]), we use an input resolution of 1024×1024 obtained by rescaling the image and padding the shorter side. The image embedding is therefore 64×64. To reduce the channel dimension, following \[62\], we use a 1×1 convolution to get to 256 channels, followed by a 3×3 convolution also with 256 channels. Each convolution is followed by a layer normalization \[4\]. Prompt encoder. Sparse prompts are mapped to 256- dimensional vectorial embeddings as follows. A point is represented as the sum of a positional encoding \[95\] of the point’s location and one of two learned embeddings that indicate if the point is either in the foreground or background. A box is represented by an embedding pair: (1) the positional encoding of its top-left corner summed with a learned embedding representing “top-left corner” and (2) the same structure but using a learned embedding indicating “bottomright corner”. Finally, to represent free-form text we use the text encoder from CLIP \[82\] (any text encoder is possible in general). We focus on geometric prompts for the remainder of this section and discuss text prompts in depth in §D.5. Dense prompts (i.e., masks) have a spatial correspondence with the image. We input masks at a 4× lower resolution than the input image, then downscale an additional 4× using two 2×2, stride-2 convolutions with output channels 4 and 16, respectively. A final 1×1 convolution maps the channel dimension to 256. Each layer is separated by GELU activations \[50\] and layer normalization. The mask and image embedding are then added element-wise. If there is no mask prompt, a learned embedding representing “no mask” is added to each image embedding location. Lightweight mask decoder. This module efficiently maps the image embedding and a set of prompt embeddings to an output mask. To combine these inputs, we take inspiration from Transformer segmentation models \[14, 20\] and modify a standard Transformer decoder \[103\]. Before applying our decoder, we first insert into the set of prompt embeddings a learned output token embedding that will be used at the decoder’s output, analogous to the \[class\] token in \[33\]. For simplicity, we refer to these embeddings (not including the image embedding) collectively as “tokens”. Our decoder design is shown in Fig. 14. Each decoder layer performs 4 steps: (1) self-attention on the tokens, (2) cross-attention from tokens (as queries) to the image embedding, (3) a point-wise MLP updates each token, and (4) cross-attention from the image embedding (as queries) to tokens. This last step updates the image embedding with prompt information. During cross-attention, the image embedding is treated as a set of 642 256-dimensional vectors. Each self/cross-attention and MLP has a residual connection \[49\], layer normalization, and a dropout \[93\] of 0.1 at training. The next decoder layer takes the updated tokens and the updated image embedding from the previous layer. We use a two-layer decoder. To ensure the decoder has access to critical geometric information the positional encodings are added to the image embedding whenever they participate in an attention layer. Additionally, the entire original prompt tokens (including their positional encodings) are re-added to the updated tokens whenever they participate in an attention layer. This allows for a strong dependence on both the prompt token’s geometric location and type. After running the decoder, we upsample the updated image embedding by 4× with two transposed convolutional layers (now it’s downscaled 4× relative to the input image). Then, the tokens attend once more to the image embedding and we pass the updated output token embedding to a small 3-layer MLP that outputs a vector matching the channel dimension of the upscaled image embedding. Finally, we predict a mask with a spatially point-wise product between the upscaled image embedding and the MLP’s output. The transformer uses an embedding dimension of 256. The transformer MLP blocks have a large internal dimension of 2048, but the MLP is applied only to the prompt tokens for which there are relatively few (rarely greater than 20). However, in cross-attention layers where we have a 64×64 image embedding, we reduce the channel dimension of the queries, keys, and values by 2× to 128 for computational efficiency. All attention layers use 8 heads. The transposed convolutions used to upscale the output image embedding are 2×2, stride 2 with output channel dimensions of 64 and 32 and have GELU activations. They are separated by layer normalization

-

### Problem

-

### Methodology

-

### Results

-

### Comments and Implications

-
