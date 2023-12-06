import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

# 设置中文字体为微软雅黑
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']
mpl.rcParams['axes.unicode_minus'] = False

# 加载Excel文件
excel_file_path = 'Data/中国信贷数据（2017.3-2023.10）from 东方财富.xlsx'
df = pd.read_excel(excel_file_path)

# 预处理数据：转换日期格式，处理列名中的非打印字符
df['月\xa0\xa0\xa0份'] = pd.to_datetime(df['月\xa0\xa0\xa0份'].str.replace('年', '-').str.replace('月份', ''), format='%Y-%m')
df = df.rename(columns={'月\xa0\xa0\xa0份': '月份'})
df = df.sort_values(by="月份")

# 绘制同比增长和环比增长的趋势图
plt.figure(figsize=(15, 7), dpi=300)  # 提高图像清晰度

# 同比增长趋势
plt.subplot(1, 2, 1)
plt.plot(df["月份"], df["同比增长"], marker='o', color='b')
plt.title("同比增长率")
plt.xlabel("月份")
plt.ylabel("同比增长率 (%)")
plt.xticks(rotation=45)
plt.grid(True)

# 环比增长趋势
plt.subplot(1, 2, 2)
plt.plot(df["月份"], df["环比增长"], marker='o', color='r')
plt.title("环比增长率")
plt.xlabel("月份")
plt.ylabel("环比增长率 (%)")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()
