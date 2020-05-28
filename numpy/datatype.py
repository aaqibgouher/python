import numpy as np

arr = np.array([1.1, 2.3, 3.4])
print(arr.dtype)

# convert this to int
arr = arr.astype("i")
print(arr.dtype)

arr = np.array(['1', '2', '3'])
print(arr.dtype)

arr = arr.astype(int)
print(arr.dtype)