import numpy as np

# 1. L.C.M - for two number

a = 2
b = 4
print(np.lcm(a,b))

# 2. L.C.M - more than 2 i.e in array

arr = np.array([2,4,6])
print(np.lcm.reduce(arr))

# 3. LCM - in a given range

arr = np.arange(1,11)
# print(type(arr))
print(np.lcm.reduce(arr))

# 4. GCD - for two numbers

a = 2
b = 4
print(np.gcd(a,b))

# 5. GCD - for more than 2 i.e in array

arr = np.array([2,4,6])
print(np.gcd.reduce(arr))
