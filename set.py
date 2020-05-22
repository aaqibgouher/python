# declare
myset = {"nazish", "aaqib", "danish"}
print(myset)

# you cannot access using index value
# access through loop
for i in myset:
    print(i)

# check from value in set
print("nazish" in myset)

# you cannot modify a value because you dont have access for a speciac index
# only adding new value allow
myset.add("saqib")
print(myset)

# insert multiple item
myset.update(["nicey", "asif"])
print(myset)

# remove
# remove -> if value does not exist then it will through error
# discard -> not through error
myset.remove("asif")
myset.discard("nicey")
print(myset)

# join two set
# union
set1 = {1,2,3,4}
set2 = {3,4,5,6}
set3 = set1.union(set2)
print(set3)

# intersection
set4 = set1.intersection(set2)
print(set4)

# a-b
set5 = set1.difference(set2) #set1-set2
print(set5)