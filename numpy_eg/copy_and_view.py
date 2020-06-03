import numpy as np

# copy
arr = np.array([1,2,3,4,5])
arr_copy = arr.copy()

# editing value
arr[0] = 10

print(arr)
print(arr_copy)

# view
arr_new = np.array([1,2,3,4,5])
arr_view = arr_new.view()

# editing value
arr_new[0] = 10

print(arr_new)
print(arr_view)