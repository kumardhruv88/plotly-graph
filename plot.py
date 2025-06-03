import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'browser'



##plotly is a data viz lirary by company plotly used for creting the 3d graph
#and interacting they are more dynamic than matla graphs and creae sone beautiful graphs
## cannot work with live graphs but we can use dash library to resolve this issue
## plotly express,plotly go,plotly dash
gap=px.data.gapminder()
temp_df=gap[gap['year']==2007]
trace1=go.Scatter(x=temp_df['lifeExp'],y=temp_df['gdpPercap'],mode='markers')
trace2=go.Scatter(x=[0,1,2],y=[0,90,200],mode='lines')

data=[trace1,trace2]
layout=go.Layout(title='life exp vs gdp in 2007',xaxis={'title':'life exp'},yaxis={'title':'gdp'})
fig=go.Figure(data,layout)
fig.show()

##this is plotly go and it is vey diffult to show the graaph on the browser hencce we use plotly express


