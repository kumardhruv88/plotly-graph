import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'browser'

##heirarchial data shown by the sunburst graph
gap=px.data.gapminder()
temp_df=gap[gap['year']==2007]
fig=px.sunburst(temp_df,path=['continent','country'],values='pop',color='lifeExp')
fig.show()

tips=px.data.tips()
fig=px.sunburst(tips,path=['sex','smoker','day','time'],values='total_bill',color='size')
fig.show()



fig=px.treemap(temp_df,path=[px.Constant('world'),'continent','country'],values='pop',color='lifeExp')
fig.show()


###3d plot

b=gap[gap['year']==2007]
fig=px.scatter_3d(b,x='lifeExp',y='pop',z='gdpPercap',log_y=True,color='continent',hover_name='country')
fig.show()
