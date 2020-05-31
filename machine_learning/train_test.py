import numpy
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

# find r value
r2 = r2_score(train_y, mymodel(train_x))
print(r2)

r2 = r2_score(test_y, mymodel(test_x))
print(r2)

myline = numpy.linspace(0, 6, 100)

#predict
print(mymodel(5))

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()