import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from flask import Flask, request, jsonify, Response, make_response
from utils import DataTransformer

app = Flask(__name__)


# print(df_con.head())
# print(df_recov.head())
# print(df_death.head())

@app.route('/')
def home():
    return make_response(jsonify({'Result':'Hello There !!'}))


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found !!'}))

@app.route('/country_ts_data', methods = ['GET'])
def get_country_ts_data():

    print("Enter The Country Name :")
    country_name = request.args.get('country','').lower()
    # country_name = country_name.lower()
    # print(country_name)

    # Creating Transformer Instance
    transformer = DataTransformer(country_name)

    # Grouping Per Country
    df_con_new = transformer.delete_and_group_col(df_con)
    df_recov_new = transformer.delete_and_group_col(df_recov)
    df_death_new = transformer.delete_and_group_col(df_death)

    # print(df_con_new)
    # print(df_recov_new)
    # print(df_death_new)

    df_crd = transformer.get_all_crd([df_con_new,df_recov_new,df_death_new])
    df_crd_inc = transformer.get_all_crd_inc(df_crd)
    # final = df_crd_inc.iloc[-1].to_dict()
    # print(final)
    # df_crd_inc.plot()
    # plt.show()
    # print(df_crd_inc)
    response_list = transformer.get_response_list(df_crd_inc)
    # print(response_list)

    return jsonify({"Country":country_name,"Result":response_list, "Status": "success"})

@app.route('/country_ts_data_latest', methods = ['GET'])
def get_country_ts_data_latest():

    print("Enter The Country Name :")
    country_name = request.args.get('country','').lower()
    # country_name = country_name.lower()
    # print(country_name)

    # Creating Transformer Instance
    transformer = DataTransformer(country_name)

    # Grouping Per Country
    df_con_new = delete_and_group_col(df_con)
    df_recov_new = delete_and_group_col(df_recov)
    df_death_new = delete_and_group_col(df_death)

    # print(df_con_new)
    # print(df_recov_new)
    # print(df_death_new)

    df_crd = transformer.get_all_crd([df_con_new,df_recov_new,df_death_new])
    df_crd_inc = transformer.get_all_crd_inc(df_crd)
    # final = df_crd_inc.iloc[-1].to_dict()
    # print(final)
    # df_crd_inc.plot()
    # plt.show()
    # print(df_crd_inc)
    response_list = transformer.get_response_list_one(df_crd_inc)
    # print(response_list)

    return jsonify({"Country":country_name,"Result":response_list, "Status": "success"})

@app.route('/country_ts_data_top_10', methods = ['GET'])
def get_country_ts_data_top_10():

    df_con_new = delete_and_group_col(df_con)
    response_list = get_response_list_top_10(df_con_new)
    print(response_list)

    return jsonify({"Result":response_list, "Status": "success"})

def get_response_list_top_10(df):
    df_new = pd.DataFrame()
    df_new["Country/Region"] = df["Country/Region"]
    df_new["Confirmed"] = df.iloc[:,-1]
    df_all_new = df_new.sort_values("Confirmed",ascending=False).head(10)
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

    app.run(debug = True)

# if __name__ == '__main__':
#     main()