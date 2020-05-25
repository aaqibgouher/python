# import a single file module
import mymath
print(mymath.square(4))

# alias
import mymath as m
print(m.square(3))

# import specific function from module
from mymath import square, sum
print(square(5))

# import module from a folder/package
import custom_package.mystring as ms
print(ms.getstr())

from custom_package import myconvertor,mystring
print(myconvertor.strtoint('3'))