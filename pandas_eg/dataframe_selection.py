import pandas as pd

# df from list of dict
mydict = {
    "name" : ["nazish", "aaqib", "danish", "shahnaj", "nicey"],
    "age" : [25, 20, 30, 29, 23],
    "sex" : ["m", "m", "m", "f", "f"]
}
df = pd.DataFrame(mydict)
print(df)

# get index 1
print(df.loc[1])

# slicing rows start:end -> start inlude, end include
print(df.loc[1:3])

# add row
ht_df = pd.DataFrame([{"name" : "saqib", "age" : 10, "sex" : "m"}], [5])
df = df.append(ht_df)
print(df)

#delete a row
df = df.drop(5)
print(df)