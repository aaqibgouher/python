# no return, no input
def printmyname():
    print("hello nazish")


printmyname()

# no return with input
def printname(name):
    print("hello "+name)

printname("aaqib")

# return with no input
def get_my_name():
    return "nazish"

name = get_my_name()
print(name)
print(get_my_name())

# return with input
def get_min(a, b):
    return a if a<b else b

print(get_min(5,2))

# infinite no of input
def get_sum(*mylist):
    sum=0
    for i in mylist:
        sum += i
    return sum

print(get_sum(1,2,3,4,5))

# parameter
def full_name(first_name, last_name):
    return " ".join([first_name, last_name])

# named parameter
print(full_name(last_name="fraz", first_name="nazish"))

# named unknown no of paramater
def get_name(**name):
    return " ".join([name["name1"], name["name2"], name["name3"]])

print(get_name(name1="aaqib", name2="nazish", name3="danish"))

def get_something(something = "default"):
    return something

print(get_something("nnn"))