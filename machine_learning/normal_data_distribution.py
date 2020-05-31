import numpy as np
import matplotlib.pyplot as plt

# mean, std dev, no of sample
arr = np.random.normal(5.0, 1.0, 100000)

plt.hist(arr, 1000)
plt.show()