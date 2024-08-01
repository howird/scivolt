# What is batch normalization

```python
def batch_norm_test():
	# In prediction mode, use mean and variance
	# obtained by moving average
	X_hat = (X - moving_mean) / torch.sqrt(moving_var + eps)
	Y = gamma * X_hat + beta  # Scale and shift
    return Y, moving_mean.data, moving_var.data

def batch_norm_1d():
	# When using a fully connected layer, calculate the 
	# mean and variance on the feature dimension
	mean = X.mean(dim=0)
    var = ((X - mean) ** 2).mean(dim=0)

    # In training mode, the current mean and variance are used
	X_hat = (X - mean) / torch.sqrt(var + eps)

	# Update the mean and variance using moving average
	moving_mean = (1.-momentum) * moving_mean + momentum * mean
	moving_var = (1.-momentum) * moving_var + momentum * var
	
    # Scale and shift
    Y = gamma * X_hat + beta
    return Y, moving_mean.data, moving_var.data

def batch_norm_2d():
	# When using a two-dimensional convolutional layer,
	# calculate the mean and variance on the channel 
	# dimension (axis=1). Here we need to maintain the
	# shape of X, so that the broadcasting
	# operation can be carried out later
	mean = X.mean(dim=(0, 2, 3), keepdim=True)
	var = ((X - mean) ** 2).mean(dim=(0, 2, 3), keepdim=True)
	
	# In training mode, the current mean and variance are used
	X_hat = (X - mean) / torch.sqrt(var + eps)
	
	# Update the mean and variance using moving average
	moving_mean = (1.-momentum) * moving_mean + momentum * mean
	moving_var = (1.-momentum) * moving_var + momentum * var
	
	# Scale and shift
	Y = gamma * X_hat + beta
    return Y, moving_mean.data, moving_var.data

def batch_norm(X, gamma, beta, moving_mean, moving_var, eps, momentum):
    # Use is_grad_enabled to determine whether we are in training mode
    if not torch.is_grad_enabled():
        return batch_norm_test()
    else:
	    # should be either 1D 
		#   or 2D 
        assert len(X.shape) in (2, 4)
        if len(X.shape) == 2:
            return batch_norm_1d()
        elif len(X.shape) == 4:
            return batch_norm_2d()
    
    
class BatchNorm(nn.Module):
	"""
	Args:
		num_features (int): the number of outputs of a FC
			layer or channels of a CNN layer
		num_dims (int): 2 for FC, 4 for a CNN
			FC:  (batch, embedding)
			CNN: (batch, channels, length, width)
	"""
    def __init__(self, num_features, num_dims):
        super().__init__()
        shape = (1, num_features)
        # scale init to 1
        self.gamma = nn.Parameter(torch.ones(shape))
        # shift init to 0
        self.beta = nn.Parameter(torch.zeros(shape))
        # not model parameters
        self.moving_mean = torch.zeros(shape)
        self.moving_var = torch.ones(shape)

    def forward(self, X):
        # Save the updated moving_mean and moving_var
        Y, self.moving_mean, self.moving_var = batch_norm(
            X, self.gamma, self.beta, 
            self.moving_mean, self.moving_var,
            eps=1e-5, momentum=0.1
        )
        return Y
```

#### For CNNs
```python
def batch_norm_test():
	# In prediction mode, use mean and variance
	# obtained by moving average
	X_hat = (X - moving_mean) / torch.sqrt(moving_var + eps)
	Y = gamma * X_hat + beta  # Scale and shift
    return Y, moving_mean.data, moving_var.data

def batch_norm_2d():
	# When using a two-dimensional convolutional layer,
	# calculate the mean and variance on the channel 
	# dimension (axis=1). Here we need to maintain the
	# shape of X, so that the broadcasting
	# operation can be carried out later
	mean = X.mean(dim=(0, 2, 3), keepdim=True)
	var = ((X - mean) ** 2).mean(dim=(0, 2, 3), keepdim=True)
	
	# In training mode, the current mean and variance are used
	X_hat = (X - mean) / torch.sqrt(var + eps)
	
	# Update the mean and variance using moving average
	moving_mean = (1.-momentum) * moving_mean + momentum * mean
	moving_var = (1.-momentum) * moving_var + momentum * var
	
	# Scale and shift
	Y = gamma * X_hat + beta
    return Y, moving_mean.data, moving_var.data

def batch_norm(X, gamma, beta, moving_mean,
			   moving_var, eps, momentum):
    if not torch.is_grad_enabled():
        return batch_norm_test()
    else:
	    return batch_norm_2d()
    
    
class BatchNorm(nn.Module):
	"""
	Args:
		num_features (int): the number of outputs of a FC
			layer or channels of a CNN layer
		num_dims (int): 2 for FC, 4 for a CNN
			FC:  (batch, embedding)
			CNN: (batch, channels, length, width)
	"""
    def __init__(self, num_features, num_dims):
        super().__init__()
        shape = (1, num_features, 1, 1)
        # scale init to 1
        self.gamma = nn.Parameter(torch.ones(shape))
        # shift init to 0
        self.beta = nn.Parameter(torch.zeros(shape))
		# not model params
        self.moving_mean = torch.zeros(shape)
        self.moving_var = torch.ones(shape)

    def forward(self, X):
        # Save the updated moving_mean and moving_var
        Y, self.moving_mean, self.moving_var = batch_norm(
            X, self.gamma, self.beta, 
            self.moving_mean, self.moving_var,
            eps=1e-5, momentum=0.1
        )
        return Y
```

# Why did we need layer normalization
```python
class LayerNorm(nn.Module):
    "Construct a layernorm module (See citation for details)."

    def __init__(self, features, eps=1e-6):
        super(LayerNorm, self).__init__()
        self.a_2 = nn.Parameter(torch.ones(features))
        self.b_2 = nn.Parameter(torch.zeros(features))
        self.eps = eps

    def forward(self, x):
        mean = x.mean(-1, keepdim=True)
        std = x.std(-1, keepdim=True)
        return self.a_2 * (x - mean) / (std + self.eps) + self.b_2
```


