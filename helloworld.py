import numpy as np
import pandas as pd

import plotly_express as px
import streamlit as st

#读取疫情经纬度数据，可以先用excel观察数据
df_covid_loc=pd.read_csv('疫情经纬度New2.csv')

#截取数据的一部分给df_map用于数据展示，也可以将全部数据给df_map
df_map=df_covid_loc
df_map['lng']=df_map['lng']-0.0046
df_map['lat']=df_map['lat']+0.0018

#调用地图显示地址的画图函数，lat指定纬度列，lon指定经度列
#请百度查询scatter_mapbox的其他参数完成地图的定制化，
#     1. 如何放大缩小控制初始地图的大小
#     2. 如何按照日期date递增展现动画
#     3. 如何改变地址点的大小、颜色、透明度
#     4. 如何让鼠标移动到点上时候显示具体的地址
fig = px.scatter_mapbox(df_map, lat="lat", lon="lng",
                        #color_discrete_sequence=px.colors.sequential.Plasma_r, 
                        color_continuous_scale='Rainbow',
                          zoom=9, 
                        opacity=0.5,
                        color='date',
                        hover_data=['add'],
                        animation_frame = 'date',
                        height=800,
                       width=900
                       )

#地图显示风格相关，一般不需要动
fig.update_traces(marker={'size': 8})
fig.update_layout(mapbox_style="carto-positron")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#Streamlit展现交互图
st.plotly_chart(fig)

#附加题：把累计地址的数量，画出折线图，最好能叠加在地图上
