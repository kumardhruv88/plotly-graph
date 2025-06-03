import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
pio.renderers.default = 'browser'

##facet plot >>  1 figure multiple graph
tips=px.data.tips()
gap=px.data.gapminder()
#fig=px.scatter(tips,x='total_bill',y='tip',facet_col='smoker')  ##different graph using same graph
#fig.show()

temp_df=gap[gap['country']=='India']
#fig=px.scatter(gap,x='lifeExp',y='gdpPercap',facet_col='year',facet_col_wrap=4)
#fig.show()  ##in facet we can represent only same type of graph but in subplot different graphs can be ploted


##3d surface plot
x=np.linspace(-10,10,100)
y=np.linspace(-10,10,100)

xx,yy=np.meshgrid(x,y)
z=xx**2 + yy**2
trace=go.Surface(x=xx,y=yy,z=z)
data=[trace]
layout=go.Layout(title='3d surface plot')
#fig=go.Figure(data,layout)
#fig.show()

## subplots
fig=make_subplots(rows=1,cols=2)
fig.add_trace(
    go.Scatter(x=[1,2,3,4],y=[3,4,5,6]),
    row=1,
    col=1
)

fig.add_trace(
    go.Histogram(x=[1,6,7,5,7]),
    row=1,
    col=2
)
fig.update_layout(title='subplot demo')
fig.show()