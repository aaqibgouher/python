import pandas as pd

# df from list of dict
mydict = {
    "name" : ["nazish", "aaqib", "danish", "shahnaj", "nicey"],
    "age" : [25, 20, 30, 29, 23],
    "sex" : ["m", "m", "m", "f", "f"]
}
df = pd.DataFrame(mydict)
print(df)

# get the column
print(df.axes)

# get the dimension
print(df.ndim)

# get total number of element
print(df.size)

# get mxn size
print(df.shape)

# print first n row, default 5
print(df.head())

# print last n row, default 5
print(df.tail(2))