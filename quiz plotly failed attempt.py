import chart_studio.plotly as py
import plotly.graph_objs as go

import pandas as pd


df = pd.read_csv('xxx.csv')

trace = go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])

layout = go.Layout(
    xaxis = dict(
        rangeslider = dict(
            visible = False
        )
    )
)

data = [trace]

fig = go.Figure(data=data,layout=layout)
py.iplot(fig, filename='simple_candlestick_without_range_slider')
