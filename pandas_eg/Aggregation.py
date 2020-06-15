import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

df = pd.read_csv(url)

# Aggregation for all columns :
print(df.aggregate(np.sum))

# Aggregation for a single col :
print(df["Lat"].aggregate(np.sum))
# or print(df.Lat.aggregate(np.sum))

# Aggregation in Dictionary order : 
print(df.aggregate({"Lat" : np.sum,"Long" : np.mean}))