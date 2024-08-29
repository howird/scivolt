---
tags:
- '#ai/dl'
---

#### 9.1 Transformers operate on sequences of vectors

- Tokenization
  - Word Tokenization
  - Char Tokenization
  - Sub-word tokenization
- Each index in the vocabulary is mapped to a high-dimensional embedding vector (e.g., 768D) as the first step in the transformer network
  - The vectors are initialized randomly and optimized during training

#### 9.2 Transformers use soft attention to weigh elements of a sequence

- The similarity of query $i$ and key $j$ vectors $= Q_i \\cdot K_i / \\sqrt{d}$
  ![](Pasted%20image%2020231218023559.png)
- This is a “soft” attention mechanism where the

#### 9.3 Queries, keys, and values undergo linear mappings

#### 9.4 Attention is multi-headed

#### 9.5 Encoder-decoder transformers can perform sequence-to-sequence mapping

- Self-attention:
  - when the queries, keys, and values all come from the same sequence
- Cross-attn:
  - In other parts, queries come from the output sequence while keys and values come from the input sequence
- During inference, the network gets a full input sequence, and then predicts each element of the output, one at a time
  - Autoregressive: At each step, its previous outputs make up the output sequence
  - During training, the decoder should only see the part of the output sequence up to but not including the element it is predicting
  - The rest of the sequence is masked by setting the corresponding similarities to negative infinity
- Other elements:
  - After the attention layers, a two-layer feedforward network is applied independently to the vector at each position
  - There are residual connections around the attention layers and the feedforward layers
  - Layer norm is used rather than batch norm; the difference is that the mean and standard deviation are calculated over the input vectors rather than over a batch

#### 9.6 Position encodings allow spatial attention

#### 9.7 Transformers process elements of a sequence in parallel

- CNNs:
  - CAN run in parallel
    - neurons in the same layer of a CNN do not depend on each other
  - CANNOT access long range context
    - older information has a declining influence
    - disappears altogether after a certain number of sequence elements
- RNNs:
  - CANNOT run in parallel:
    - neurons in a recurrent layer depend on their own outputs in previous time steps
  - CAN access long range content:
    - use multiplication and gates, to determine when to use, retain, or discard older information
- Transformers CAN DO BOTH!
  - all responses in a layer can be computed in parallel during training
  - neurons in each layer receive input from all elements of the sequence in the previous layer
- Teacher forcing and non-parallel inference
  - When a transformer’s decoder is used for sequence generation, it receives its own previous outputs as input, so the predictions must be sequential
  - When training the decoder, each element can be predicted in parallel
    - Each element doesn’t receive the network’s previous predictions as input, but rather the correct previous elements as input, so that mistakes early in the sequence to not propagate through the whole sequence
    - For each query, later keys/values in the sequence are masked

#### 9.8 Transformers can omit the encoder or decoder

#### 9.9 Transformers perform self-supervised learning with large datasets

- Causal language modelling
  - This task consists of predicting the next word in a sequence
  - This can be performed as a self-supervised task based on large collections of text
    - E.g., the first GPT network was trained on BookCorpus (Zhu et al., 2015, ICCV), a collection of 11K free books with about one billion words
- Masked language modelling
  - The encoder-only BERT model (Devlin et al., 2019) introduced masked language modelling to transformers
  - Given a full sequence, 15% of tokens are masked at random using a new \[MASK\] token
  - The network predicts these tokens at each masked location, using both forward and backward context

#### 9.10 Transformers create contextualized embeddings

- A limitation of classical word embeddings is that they don’t handle words that have multiple meanings
- To work around this limitation, some models have concatenated context
  embeddings with word embeddings
- Each layer of a transformer can be seen as producing a contextual embedding of each token that can incorporate context from the rest of the sequence
- In transformer models, embeddings for a given token in different contexts become less similar in deeper layers
  ![](Pasted%20image%2020231218030746.png)