import numpy as np

# 1. 
#Adding using simple iteration
# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
# c = []

# for i,j in zip(a,b) :
#     c.append(i+j)

# print(c)
# print(type(c))

# 2.
#Adding using ufunc ie vectorisation add()

# x = [1,2,3,4,5]
# y = [6,7,8,9,10]
# # w = [3,6,9,12,15]  #we cant do the sum of more than 2 lists using add() ufunc
# z = []

# z = np.add(x,y)
# print(z)
# print(type(z))

# 3.
# How To Create Your Own ufunc

# def find_sum(a,b,c):      #defining a funct
#     return a + b + c

# find_sum = np.frompyfunc(find_sum,3,1)       #converting simple funct to ufunc and parameter are func_name,no. of inputs and no. of output

# a = [1,2,3,4,5]
# b = [1,3,5,7,9]
# c = [2,4,6,8,10]

# print(find_sum(a,b,c))        #calling a func and passing the parameters
# print(type(find_sum))           #checking that find_sum is ufunc or not
# print(type(np.concatenate))

# 4.
#how to check that a func is ufunct or not 

# if type(np.add) == np.ufunc :         #if it will true then print yes else will print no        
#     print("Yes it is")
# else :
#     print("No its not")
