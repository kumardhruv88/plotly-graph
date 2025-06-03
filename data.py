import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px


latlong=pd.read_csv('district wise centroids.csv')

census=pd.read_csv('india-districts-census-2011.csv')


##merging the data
cols=['District code','District name','Population','Male','Female','Households_with_Internet','Housholds_with_Electric_Lighting','Literate']
census=census[cols]

final_df=latlong.merge(census,left_on='District',right_on='District name').drop(columns=['District name'])
final_df['sex_ratio']=round((final_df['Female']/final_df['Male'])*100)
final_df['literacy_rate']=round((final_df['Literate']/final_df['Population'])*100)

final_df.drop(columns=['Male', 'Female', 'Literate'], inplace=True)

final_df.to_csv('final_district_data.csv', index=False)
print("CSV file saved as 'final_district_data.csv'")