import plotly.graph_objects as go
import pandas as pd

# Read data from a csv
df = pd.read_excel('000001_平安银行.xlsx')

fig = go.Figure(data=[go.Candlestick(x=df['日期'],
                open=df['开盘'],
                high=df['最高'],
                low=df['最低'],
                close=df['收盘'])])

fig.show()