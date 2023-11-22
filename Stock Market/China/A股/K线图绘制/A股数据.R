# 加载所需库
library(plotly)

# 读取Excel文件，假设数据存储在'000001_平安银行.xlsx'中
library(readxl)
df <- read_excel('000001_平安银行.xlsx')

# 创建蜡烛图
fig <- df %>%
  plot_ly(x = ~日期, type="candlestick",
          open = ~开盘, close = ~收盘,
          high = ~最高, low = ~最低)

# 显示图表
fig
