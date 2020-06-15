import pandas as pd

one = pd.DataFrame({
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5'],
   'Marks_scored':[98,90,87,69,78]},
   index=[1,2,3,4,5])

two = pd.DataFrame({
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5'],
   'Marks_scored':[89,80,79,97,88]},
   index=[1,2,3,4,5])

# Using CONCAT

# will simply concat the one df with the two df. default the axis = 0 i.e horizontally.In this, whatever their keys was, same it will show
# print(pd.concat([one,two]))         

# will show a new column of key
# print(pd.concat([one,two],keys=['x','y']))

# will ignore the index , and form new index starts with 0
# print(pd.concat([one,two],ignore_index=True))

# will concat vertically
# print(pd.concat([one,two],axis=1))

# using APPEND :

print(one.append(two))

