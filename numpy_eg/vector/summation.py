import numpy as np
# 1. simple add element wise

# arr_1 = np.array([1,2,3,4,5])
# arr_2 = np.array([1,2,3,4,5])
# print(np.add(arr_1,arr_2))

# 2. summation - first it will sum the arr_1,arr_2 and arr_3 individually and then sum it at once and will give the output. also axis means it will sum and give the output in one axis

# arr_1 = np.array([1,2,3,4,5])
# arr_2 = np.array([1,2,3,4,5])
# arr_3 = np.array([2,4,6,8,10])
# new_arr = np.sum([arr_1,arr_2,arr_3],axis=1)
# print(new_arr)

# 3. cummulative sum

# arr_1 = np.array([1,2,3,4,5])
# print(np.cumsum(arr_1))

# 4. product

# arr_1 = np.array([1,2,3,4,5])
# print(np.prod(arr_1))


# 5. product of more than 2 arrays

# arr_1 = np.array([1,2,3,4,5])
# arr_2 = np.array([1,2,3,4,5])
# print(np.prod([arr_1,arr_2],axis=1))  #if will not give that axis,then it will give prod of both 2 arrays but after giving axis = 1, it will give individual product

# 6. cummulative product

# arr_1 = np.array([1,2,3,4,5])
# print(np.cumprod(arr_1))