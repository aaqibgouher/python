# declare
mydict = {
    "name": "nazish",
    "age": 25
}
print(mydict)

# access
print(mydict["name"])
print(mydict.get("name"))

# modify value
mydict["age"] = 26
print(mydict)

# loop
for i in mydict:
    print(i, mydict[i])

# loop through value
for i in mydict.values():
    print(i)

# loop through index and value
for index,value in mydict.items():
    print(index, value)

# insert a key value
mydict["email"] = "nfraz@gmail.com"
print(mydict)

# remove
mydict.pop("email")
print(mydict)