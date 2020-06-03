from numpy import random
import matplotlib.pyplot as pt
import seaborn as sns

# for binomial dist
# x = random.binomial(n=10, p=0.5, size=10)
# print(x)

# visualisation of binomial dist:
# x = random.binomial(n=10,p=0.5,size=10)
# sns.distplot(x,hist=False)
# pt.show()

# normal dist vs binomial dist
# x = random.normal(loc=50,scale=5,size=1000)
# sns.distplot(x,hist=False,label='normal')
# y = random.binomial(n=100,p=0.8,size=1000)
# sns.distplot(y,hist=False,label='binomial')
# pt.show()