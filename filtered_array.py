#how to filter array

import numpy as np

arr = np.array([1,2,3,4,5])
x = [False,True,False,True,False]
print(arr[x])

#creating the filtered array 
import numpy as np

arr = np.array([1,2,3,4,5])
filter_arr = []

for i in arr :
    if i > 2 :
        filter_arr.append(True)
    else :
        filter_arr.append(False)

new_arr = arr[filter_arr]
print(filter_arr)
print(new_arr)