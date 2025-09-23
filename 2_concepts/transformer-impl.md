# implementing transformers

now that people are paying attention again, here is your periodic reminder. Always run in bf16. always apply ROPE and attention softmax at float32 (as shown here)

https://github.com/xjdr-alt/entropix/blob/main/entropix/model.py#L46
