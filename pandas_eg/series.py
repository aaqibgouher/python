import pandas as pd
import numpy as np

# empty series
s = pd.Series()
print(s)

# series from numpy array
arr = np.array([1,2,3,4,5])
s = pd.Series(arr)
print(s)

# access the data
print(s[1])
print(s[:3])
print(s[2:])

print("data")

# series with list
s = pd.Series([1,2,3,4,5])
print(s)

# with custom index
s = pd.Series(arr, [100, 101, 102, 103, 105])
print(s)

# series from dict
mydict = {
    "name" : "nazish",
    "age" : 25
}
s = pd.Series(mydict)
print(s)