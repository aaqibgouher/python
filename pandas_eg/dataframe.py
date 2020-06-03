import pandas as pd

df = pd.DataFrame()
print(df)
print(type(df))

# df from list
df = pd.DataFrame([1,2,3,4,5])
print(df)

# from list custom index
df = pd.DataFrame([1,2,3,4,5], columns=["Age"])
print(df)

# df from 2d list
arr = [
    ["nazish", 25],
    ["aaqib", 20],
    ["danish", 30]
]
df = pd.DataFrame(arr, columns=["Name", "Age"])
print(df)

# df from dict
mydict = {
    "name" : ["nazish", "aaqib", "danish", "bhabhi"],
    "age" : [25, 20, 30, 30]
}
df = pd.DataFrame(mydict)
print(df)

# df from list of dict
arr = [
    {
        "name" : "nazish",
        "age" : 25
    },
    {
        "name" : "aaqib",
        "age" : 20,
        "sex" : "male"
    }
]
df = pd.DataFrame(arr)
print(df)