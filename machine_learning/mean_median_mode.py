import numpy as np
from scipy import stats

arr = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# get the mean
print(np.mean(arr))

# get the median
print(np.median(arr))

# get the mode
print(stats.mode(arr))