import matplotlib.pyplot as plt
import seaborn as sns

# dist_plt is for plotting graph for distribution func, we have to pass array inside it
sns.distplot([1,2,3,4,5])       #it will give curve as well as histogram
plt.show()      #calling a show fx 

#if only need curve nor histogram :
sns.distplot([1,2,3,4,5],hist=False)
plt.show()