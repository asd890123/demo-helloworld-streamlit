import streamlit as st
import numpy as np
import pandas as pd

st.title("my first app")

x = st.slider("x")
y = x + 3
y

'''
@st.cache
def load_data():
    df = pd.read_csv("crime_data_20200508.csv")
    #df = df[['EVENT_TYPE', 'CREATE_TIME', 'COUNTY', 'LAT', 'LON']]
    crime,locname,incidentdatetime,publicadress,agency,accuracy
    #df.columns = ['event_type', 'time', 'county', 'lat', 'lon']
    return df

df = load_data()

st.table(df.head())

event_list = df["event_type"].unique()

event_type = st.sidebar.selectbox(
    "Which kind of event do you want to explore?",
    event_list
)

county_list = df["county"].unique()

county_name = st.sidebar.selectbox(
    "Which county?",
    county_list
) 

part_df = df[(df["event_type"]==event_type) & (df['county']==county_name)]

st.write(f"根据你的筛选，数据包含{len(part_df)}行")

st.map(part_df)
'''
