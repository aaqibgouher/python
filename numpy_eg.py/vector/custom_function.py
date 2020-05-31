import numpy as np

def myadd(x, y):
    return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1,2,3,4], [1,2,3,4]))

print(type(np.add))
print(type(myadd))