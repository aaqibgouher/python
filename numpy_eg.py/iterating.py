import numpy as np

arr = np.array([1, 2, 3])

# normal iterate
for x in arr:
  print(x)

# interate with index
for idx, i in np.ndenumerate(arr):
    print(idx, i)

arr = np.array([[1, 2, 3], [4, 5, 6]])
# normal 2d iterate
for i in arr:
    print(i)

# index
for idx, i in np.ndenumerate(arr):
    print(idx, i)

# normal 2d iterate
for i in arr:
    for j in i:
        print(j)

# loop through each element of n dim array
for i in np.nditer(arr):
    print(i)

# loop and change dtype
for i in np.nditer(arr, flags = ["buffered"], op_dtypes=["S"]):
    print(i)