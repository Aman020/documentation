import plotly.plotly as py
from plotly.graph_objs import *

py.sign_in('theengineear', 'o9zlr0hy6z')

data = Data([
    Heatmap(
        z=[[1, 20, 30], [20, 1, 60], [30, 60, 1]]
    )
])

plot_url = py.plot(data, filename='basic-heatmap', auto_open=False)