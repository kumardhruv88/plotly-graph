import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')


df=pd.read_csv('final_district_data.csv')

list_of_states=list(df['State'].unique())

list_of_states.insert(0,'overall india')

st.sidebar.title('INDIA CENSUS VIZ')

selected_state=st.sidebar.selectbox('select a state',list_of_states)



primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[5:]))


plot=st.sidebar.button('plot graph')

if plot:
    st.text('size reprensts primary parameter')
    st.text('color represents secondary parameter')
    if selected_state=='overall india':
        fig=px.scatter_map(df,lat='Latitude',lon='Longitude',zoom=3,size=primary,color=secondary,mapbox_style='carto-positron',width=1200,height=700,size_max=35,hover_name='District')

        st.plotly_chart(fig,use_container_width=True)

    else:
        state_df=df[df['State']==selected_state]

        fig=px.scatter_map(state_df,lat='Latitude',lon='Longitude',zoom=3,size=primary,color=secondary,mapbox_style='carto-positron',width=1200,height=700,size_max=35)

        st.plotly_chart(fig,use_container_width=True)
        
