import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

arr_bool = [True,True,False,True,True,True,False,True,False,False]

# filter based on bool array
print(arr[arr_bool])

# filter based on condition
print(arr[arr>5])