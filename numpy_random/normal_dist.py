from numpy import random
import matplotlib.pyplot as pt
import seaborn as sns

# simple normal func for normal dist where loc = mean,scale = std dev
x = random.normal(loc=1,scale=2,size=10)
print(x)

# normal dist in graph so we have to import some modules
# x = random.normal(loc=1,scale=2,size=10)
# sns.distplot(x)         #so in this curve as well as histogram 
# pt.show()

# if you want only the curve then :
sns.distplot(x,hist=False)
pt.show()
