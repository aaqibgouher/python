# create a list
mylist = ["nazish", "aaqib", "danish"]
print(mylist)

# access value
print(mylist[0]) # from specific position
print(mylist[0:2]) # from speciac start to epscific end
print(mylist[1:]) # from specific start to end

# modify value
mylist[1] = "aaqibgouher"
print(mylist)

for i in mylist:
    print(i)

# length of list
print(len(mylist))

# insert at end
mylist.append("shahnaj")
print(mylist)

mylist.append(["saqib", "nicey"])
print(mylist)
print(mylist[4][1])
mylist[4].append("asif")
print(mylist)

# insert at specific position
mylist.insert(1, "nesar")
print(mylist)

# remove a value - if not found the value it will through error
mylist.remove("nesar")
print(mylist)

# remove from end
mylist.pop()
print(mylist)

# remove from specific os
mylist.pop(3)
print(mylist)

# merge or join list
mylist.extend(["saqib", "nicey"])
print(mylist)

# join two list
print([1,2,3] + [4,5,6])

# sort
mylist = [2,1,4,3,5]
mylist.sort()
print(mylist)

# reverse
mylist.reverse()
print(mylist)