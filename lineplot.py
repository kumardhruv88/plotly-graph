import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'browser'

##changes in india population with year
gap=px.data.gapminder()
temp_df=gap[gap['country']=='India']
fig=px.line(temp_df,x='year',y='pop',title='india popolation growth')
fig.show()

## variation of india pak china
temp_df=gap[gap['country'].isin(['India','China','Pakistan'])].pivot(index='year',columns='country',values='lifeExp')

fig=px.line(temp_df,x=temp_df.index,y=temp_df.columns)
fig.show()

temp_df=gap[gap['country']=='India']
fig=px.bar(temp_df,x='year',y='pop')
fig.show()

### three countrires grouped bar charts
temp_df=gap[gap['country'].isin(['India','China','Pakistan'])].pivot(index='year',columns='country',values='lifeExp')
fig=px.bar(temp_df,x=temp_df.index,y=temp_df.columns,barmode='group',log_y=True,text_auto=True) ## we can add log value and can group the grop data
fig.show()

###stacked bar chart
temp_df=gap[gap['year']==2007]
fig=px.bar(temp_df,x='continent',y='pop',color='country')
fig.show()

###animated bar chart
fig=px.bar(gap,x='continent',y='pop',color='continent',animation_frame='year',animation_group='country',range_y=[0,4000000000])
fig.show()

