import pandas as pd
import numpy as np

# String operations, so firstly we have taken a series object , so we cant use the function of string directly. therefore first we will convert it into string object

s = pd.Series(["AAQIB","GOUHER","DANISH"])

print(s)
print(s.str.lower())    # converts into lower case
print(s.str.upper())    # converts into upper case
print(s.str.len())      # finds the length
print(s.str.split('I'))     # split the series according to thr character we will pass !
# print(s.str.strip())
print(s.str.cat(sep=' '))   # concat the series element with the separation char between them
print(s.str.get_dummies())   # it will create a df, in which series element will become the col_name for df, and the its index, wherever be the comb will come there will be 1 as its value
print(s.str.contains("AAQIB"))  #it will return in boolean and if any match will there , it will show True
print(s.str.repeat(2))          #based on the inputs, it will repeat all of the elemnts insode the Series
print(s.str.count('A'))         # will count the number of occurence in each of the element at any index
