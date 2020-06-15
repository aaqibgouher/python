import pandas as pd
import numpy as np

def get_response_list_top_10(df):
   df_new = pd.DataFrame()
   df_new["Country/Region"] = df["Country/Region"]
   df_new["Confirmed"] = df.iloc[:,-1]
   df_all_new = df_new.sort_values("Confirmed",ascending=False).head(10)
   print(df_all_new)
   print(df_all_new.to_dict())
   print(df_all_new.set_index('Country/Region'))
   print(df_all_new.set_index('Country/Region').to_dict())
   print(df_all_new.T)
   print(df_all_new.T.to_dict())
   return df_all_new.T.to_dict()

def delete_and_group_col(df):
   drop_col = ["Province/State","Lat","Long"]
   df = df.drop(drop_col,axis=1)
   return df.groupby("Country/Region",as_index=False).agg(sum)

if __name__ == '__main__':

   url_con = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
   url_recov = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
   url_death = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

   df_con = pd.read_csv(url_con)
   df_recov = pd.read_csv(url_recov)
   df_death = pd.read_csv(url_death)

   df_con_new = delete_and_group_col(df_con)
   response_list = get_response_list_top_10(df_con_new)
   # print(response_list)