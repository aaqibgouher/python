import numpy as np
import matplotlib.pyplot as plt

# get the uniform random data between 0 to 5, total 10 datas
arr = np.random.uniform(0, 5, 100000)
# print(arr)

plt.hist(arr, 10)
plt.show()