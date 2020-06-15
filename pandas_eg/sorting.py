import pandas as pd
import numpy as np

# Sorting by Label (Index) : Only Index will be sorted and according to the index the actual values will be shown.

unsorted_df = pd.DataFrame(np.random.randn(3,2),index=[3,2,1],columns=['x','y'])
sorted_df = unsorted_df.sort_index() # sort_index : by default it sorts in asc order, and for desc we have to do ascending=False
# print(unsorted_df)
# print(sorted_df)

# Sorting by Actual Vales : 

unsorted_df = pd.DataFrame(np.random.randn(3,2),index=[3,2,1],columns=['x','y'])
sorted_df = unsorted_df.sort_values(['x','y'],ascending=[True,True]) 
# print(unsorted_df)
# print(sorted_df)