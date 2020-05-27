import numpy as np

arr = np.array([1,2,3,4,5,6])
# [start:end] -> start is included, end is excluded
print(arr[1:3])

# from specific start to end
print(arr[2:])

# from start to specific end
print(arr[:3])

# step is a third para
# [start:end:step] -> how much steps to be taken - default 1
print(arr[::2])

# 2d array slice
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr[0,1]) # 2
print(arr[0,2]) # 3
print(arr[0, 1:]) # 2 3
print(arr[0:2, 1:]) # 2 3\n5 6