import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 数据加载和清理
data = pd.read_excel("2022年12月全国彩票销售情况表.xlsx")
data = data.iloc[3:]
data.columns = ['月份', '福利彩票-乐透数字型', '福利彩票-即开型', '福利彩票-基诺型', '福利彩票-小计',
                '体育彩票-乐透数字型', '体育彩票-竞猜型', '体育彩票-即开型', '体育彩票-视频型', '体育彩票-小计']
data = data.dropna()
data['月份'] = data['月份'].str.replace(' ', '')
data = data.replace('-', float('nan'))

for col in data.columns[1:]:
    data[col] = data[col].astype(float)

# 设置中文字体为微软雅黑
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']
mpl.rcParams['axes.unicode_minus'] = False

# 创建折线图
plt.figure(figsize=(10, 6))

# 绘制每种彩票类型的折线图
for column in data.columns[1:]:
    plt.plot(data['月份'], data[column], marker='o', label=column)

plt.title('2022年每月彩票销售额变化趋势')
plt.xlabel('月份')
plt.ylabel('销售额（亿元）')
plt.legend()
plt.grid(True)

# 提高Y轴精度
plt.gca().yaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%.2f'))

# 提高图像清晰度
plt.savefig('2022年彩票销售额变化趋势图.image', dpi=300)

plt.show()
