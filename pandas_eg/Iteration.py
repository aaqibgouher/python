import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6,3),columns=["x","y","z"])

print(df)

# Iteration through column :

for key, values in df.iteritems() :
    print(key,values)

# Iteration through row :

for row_index,row in df.iterrows() :
    print(row_index,row)

# Iteration through in rows but in tuples

for row in df.itertuples() :
    print(row)