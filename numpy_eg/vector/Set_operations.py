import numpy as np

# 1. finding unique elements in set

# arr = np.array([1,1,1,1,2,2,2,3,4,5,6,7,7,7])
# set_ = np.unique(arr)
# print(set_)
# print(type(set_))

# 2. Union for two sets :

# arr_1 = np.array([1,3,5,7,9])
# arr_2 = np.array([2,4,6,8])
# print(np.union1d(arr_1,arr_2))

# 3.Intersection for two sets :

# arr_1 = np.array([1,2,3,4,5])
# arr_2 = np.array([2,4,6,8])
# print(np.intersect1d(arr_1,arr_2))

# 4. Set Difference i.e A-B and B-A

# arr_1 = np.array([1,2,3,4,5])
# arr_2 = np.array([2,4,6,8])
# print(np.setdiff1d(arr_1,arr_1))

# 5. finding symmetric difference
# arr_1 = np.array([1,2,3,4])
# arr_2 = np.array([3,4,5,6])
# print(np.setxor1d(arr_1,arr_2,assume_unique=True))  #without using assu. fx it will also give output but that fx will speed the output