import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'browser'
gap=px.data.gapminder()
temp_df=gap[gap['year']==2007]
fig=px.histogram(temp_df,x='lifeExp',nbins=20,text_auto=True)
fig.show()

##multiple histogram plot
iris=px.data.iris()

fig=px.histogram(iris,x='sepal_length',color='species',text_auto=True)
fig.show()



###pie chats in plotly express
a=gap[(gap['year']==2007) & (gap['continent']=='Europe')]

fig=px.pie(a,values='pop',names='country',hover_data=['lifeExp'],title='DISTRIBUTION OF EUROPE IN POPULATION')
fig.show()



temp=gap[gap['year']==1952].groupby('continent')['pop'].sum().reset_index()
fig=px.pie(temp,values='pop',names='continent')
fig.show()