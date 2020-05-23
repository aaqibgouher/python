try:
    n = input("Enter a positive number ")
    if type(n) != int: raise Exception("input should be integer")
    n = int(n)
    if n<0: raise Exception("number cannot be negative")
except Exception as e:
    print("error")
    print(e)