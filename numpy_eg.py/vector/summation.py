import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([2,3,4,5,6])

print(np.sum(arr1))
print(np.sum([arr1, arr2]))

print(np.sum([arr1, arr2], axis=1))

print(np.cumsum(arr1))
print(np.cumprod(arr1))

print(np.diff(arr1))
print(np.diff(arr1, n=2))