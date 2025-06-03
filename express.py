import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'browser'

#using the plotly express
gap=px.data.gapminder()
temp_df=gap[gap['year']==2007]
#fig=px.scatter(temp_df,x='lifeExp',y='gdpPercap',color='continent',title='GDP VS LIFE EXPECTANCY IN 2007',size='pop',size_max=50,hover_name='country')
#fig.show()

## i want to plot thisgraph fir every year
fig=px.scatter(gap,x='lifeExp',y='gdpPercap',color='continent',title='GDP VS LIFE EXPECTANCY IN 2007',size='pop',size_max=80,hover_name='country',range_x=[30,95],animation_frame='year',animation_group='country')

fig.show()
