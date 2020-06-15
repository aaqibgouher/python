import pandas as pd
import numpy as np

class DataTransformer:

    def __init__(self, country):
        self.country_name = country

    def filter_crd(self, df):
        return df.loc[df["Country/Region"].str.lower() == self.country_name].drop("Country/Region",axis=1).T

    def get_all_crd(self, dflist):
        list_all_crd = [self.filter_crd(x) for x in dflist]
        list_all_crd_new = pd.concat(list_all_crd,axis=1).reset_index()
        list_all_crd_new.columns = ["Dates","Confirmed","Recovered","Deaths"]
        list_all_crd_new["Active"] = list_all_crd_new["Confirmed"] - list_all_crd_new["Recovered"] - list_all_crd_new["Deaths"]
        list_all_crd_new['Dates'] = pd.to_datetime(list_all_crd_new['Dates'])
        list_all_crd_new.set_index("Dates",inplace=True)
        # print(list_all_crd_new)
        return list_all_crd_new

    def get_percent_inc(self, df,col) :
        ser = np.round(100 * df[col+"_inc"]/(df[col] - df[col+"_inc"]),2)
        ser = ser.replace(np.nan,0)
        ser = ser.astype(str) + "%"
        return ser

    def get_all_crd_inc(self,df):
        df_diff = df.diff()
        df_diff.columns = ["Confirmed_inc","Recovered_inc","Deaths_inc","Active_inc"]
        df_diff_concat = pd.concat([df,df_diff],axis=1)
        df_diff_concat["Confirmed_inc_%"] = self.get_percent_inc(df_diff_concat,"Confirmed")
        df_diff_concat["Recovered_inc_%"] = self.get_percent_inc(df_diff_concat,"Recovered")
        df_diff_concat["Deaths_inc_%"] = self.get_percent_inc(df_diff_concat,"Deaths")
        df_diff_concat["Active_inc_%"] = self.get_percent_inc(df_diff_concat,"Active")
        
        # print(df_diff_concat)
        df_diff_concat_new = df_diff_concat.replace(np.nan,0)
        df_diff_concat_new = df_diff_concat_new.astype(str)
        df_diff_concat_new.reset_index(inplace = True)
        df_diff_concat_new['Dates'] = df_diff_concat_new['Dates'].astype(str)
        return df_diff_concat_new

    def get_response_list(self, df):
        my_list = []
        for i in range(len(df)):
            my_list.append(df.iloc[i].to_dict())
        return my_list

    def get_response_list_one(self, df):
        return df.iloc[-1].to_dict()
    
    def get_response_list_top_10(self,df):
        df_new = pd.DataFrame()
        df_new["Country/Region"] = df["Country/Region"]
        df_new["Confirmed"] = df.iloc[:,-1]
        df_all_new = df_new.sort_values("Confirmed",ascending=False).head(10)
        return df_all_new