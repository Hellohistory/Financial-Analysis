import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# 从预处理文件中读取数据
file_path = r"D:\Code Work\Financial Analysis\Exchange_Rate\RMB\历史数据（截止至2023年8月4日）\人民币汇率中间价历史数据\中间价_处理后.xlsx"
data1_cleaned = pd.read_excel(file_path)

# 创建Dash应用
app = dash.Dash(__name__)

# 定义布局
app.layout = html.Div([
    # 顶部行，包括货币选择下拉框和日期选择器
    html.Div([
        # 货币选择下拉框，左上角
        html.Div([
            dcc.Dropdown(
                id='currency-selector',
                options=[{'label': currency, 'value': currency} for currency in data1_cleaned.columns[1:]],
                value=['USD/CNY'],
                multi=True,
            )
        ], style={'width': '48%', 'display': 'inline-block'}),

        # 日期选择器，右上角
        html.Div([
            dcc.DatePickerRange(
                id='date-picker',
                start_date=data1_cleaned['日期'].min(),
                end_date=data1_cleaned['日期'].max(),
                display_format='YYYY-MM-DD'
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    # 图表，居中
    html.Div([
        dcc.Graph(id='time-series-plot')
    ], style={'margin': 'auto', 'width': '80%'})
])


# 定义回调
@app.callback(
    Output('time-series-plot', 'figure'),
    [Input('currency-selector', 'value'),
     Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date')]
)
def update_time_series(selected_currencies, start_date, end_date):
    filtered_data = data1_cleaned[(data1_cleaned['日期'] >= start_date) & (data1_cleaned['日期'] <= end_date)]
    data_long_format = filtered_data.melt(id_vars='日期', value_vars=selected_currencies, var_name='货币',
                                          value_name='汇率')
    fig = px.line(data_long_format, x='日期', y='汇率', color='货币', title='多种货币汇率时间序列')

    # 更新X轴的日期格式
    fig.update_xaxes(tickformat="%Y年%m月%d日")

    # 更新坐标轴框的大小
    fig.update_layout(
        xaxis_title='日期',
        yaxis_title='汇率',
        width=1200,  # 设置图表宽度
        height=800, # 设置图表高度
        xaxis=dict(
            title_font=dict(size=18),  # X轴标题字体大小
            tickfont=dict(size=10)  # X轴刻度字体大小
        ),
        yaxis=dict(
            title_font=dict(size=18),  # Y轴标题字体大小
            tickfont=dict(size=16)  # Y轴刻度字体大小
        )
    )


    return fig


# 运行应用
if __name__ == '__main__':
    app.run_server(debug=True)
