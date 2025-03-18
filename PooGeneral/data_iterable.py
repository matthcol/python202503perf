import numpy as np

data = np.random.normal(10, 2.5, 1_000_000)
print(len(data), data.mean(), np.std(data))