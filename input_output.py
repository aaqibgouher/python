print("Enter your name")
name = input()
print("hello "+name)

myinput = input("enter two number ")
num = myinput.split(" ")
print(myinput)
print(num)
num = list(map(int, num))
print(num)

n = int(input("enter n: "))
print(n*n)