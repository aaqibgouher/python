import pandas as pd

# df from list of dict
mydict = {
    "name" : ["nazish", "aaqib", "danish", "shahnaj", "nicey"],
    "age" : [25, 20, 30, 29, 23],
    "sex" : ["m", "m", "m", "f", "f"]
}
df = pd.DataFrame(mydict)
print(df)

# get the sum
print(df["age"].sum())

# get the summary
print(df.describe())