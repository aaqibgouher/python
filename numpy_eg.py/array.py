import numpy as np

# create numpy array
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))
# access data
print(arr[0])

# create tupple as numpy array
arr = np.array((1,2,3,4,5))
print(arr)

# create a 2d array
arr = np.array([[1,2,3,4,5], [1,2,3,4,5]])
print(arr)
# print dimention of arr
print(arr.ndim)
# access data for 2d array
print(arr[1,2])

# get the shape of array
print(arr.shape)
