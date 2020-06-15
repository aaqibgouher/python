import pandas as pd
import numpy as np

# url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

# df = pd.read_csv(url)

# # Aggregation for all columns :
# print(df.aggregate(np.sum))

# # Aggregation for a single col :
# print(df["Lat"].aggregate(np.sum))
# # or print(df.Lat.aggregate(np.sum))

# # Aggregation in Dictionary order : 
# print(df.aggregate({"Lat" : np.sum,"Long" : np.mean}))

# created a random df having 5 x 3 size , and changed the col_name.
# df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
# 'h'],columns=['one', 'two', 'three'])

# now we are reindexing means, we are changing the rows 5 to 8.also I our df one datas of 5 rows is there, so after reindexing, the new rows will not have any type values i.e NAN (not a number).
# df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

# print(df["one"].isnull())       #selecting a particular col, and checking where is the data is null. it will return a series of boool .

# print(df.fillna(0))             # fillna(value) will fill the nan place in the df with scaler values

# print(df.fillna(method="pad"))  
# print(df.fillna(method="bfill"))
# print(df.dropna())     # it will drop all those values, which has nan values.
# df = pd.DataFrame({"one" : [1,2,3,4,5000],"two" : [7,6,5,4,90]},index=[1,2,3,4,5])
# print(df.replace({5000 : 5,90 : 9}))      #will replace the values with some new values.

