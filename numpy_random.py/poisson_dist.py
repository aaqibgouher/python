from numpy import random
import matplotlib.pyplot as pt
import seaborn as sns


#simply poisson dist
x = random.poisson(lam=9,size=10)
print(x)

#visualisation of P.D :
# x = random.poisson(lam=9,size=10)
sns.distplot(x)
pt.show()

# relation between normal and poisson dist :
sns.distplot(random.poisson(lam=10,size=1000),hist=10)
sns.distplot(random.normal(loc=10,scale=5,size=1000),hist=10)
pt.show()