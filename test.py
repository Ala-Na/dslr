import numpy as np

# weights = np.random.randn(shape[0], 1) * np.sqrt(1/())

shape = 5
weights = np.zeros((shape, 1))
bias = np.zeros((1, 1))
param = np.concatenate([weights, bias])

print(param)
