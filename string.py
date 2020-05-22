multiline_str = """
this is multiline string.
so this is multiline line
"""
print(multiline_str)

# access value from specific position
mystr = "Hello World"
print(mystr[0])
print(mystr[-1]) # from end

# slicing
print(mystr[0:4]) # from start to end
print(mystr[:4]) # from start to end
print(mystr[3:]) # from specific start to end
print(mystr[-5:])

# string length
print(len(mystr))

# remove white space from start and end
print("  hello   ".strip())

# to upper case
print("hello".upper())

# replace
print("hello world".replace("world", "nazish"))

# split to list
print("hello world nazish".split())

# check string in string
print("naz" in "hello nazish")

# reverse
print("nazish"[::-1])