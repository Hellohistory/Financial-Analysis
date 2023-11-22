import matplotlib.pyplot as plt
import pandas as pd

# 设置字体为微软雅黑
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 加载数据
data_path = "中国宏观杠杆率.xlsx"  # 请替换为实际的文件路径
df = pd.read_excel(data_path)

# 将'年份'列转换为日期时间格式
df['年份'] = pd.to_datetime(df['年份'])

# 创建一个图形
fig, ax = plt.subplots(figsize=(15, 8), dpi=500)

# 绘制趋势图
df.plot(x='年份', y='居民部门', ax=ax, label='居民部门', color='blue')
df.plot(x='年份', y='非金融企业部门', ax=ax, label='非金融企业部门', color='green')
df.plot(x='年份', y='政府部门', ax=ax, label='政府部门', color='red')

# 设置标题
ax.set_title('中国宏观杠杆率趋势')

# 设置标签
ax.set_xlabel('年份')
ax.set_ylabel('杠杆率 (%)')

# 显示图例
ax.legend()

# 标记关键点
for column in ['居民部门', '非金融企业部门', '政府部门']:
    max_value = df[column].max()
    min_value = df[column].min()
    max_year = df.loc[df[column] == max_value, '年份'].iloc[0]
    min_year = df.loc[df[column] == min_value, '年份'].iloc[0]

    ax.annotate(f"Max: {max_value:.2f}", xy=(max_year, max_value), xytext=(max_year, max_value + 5),
                arrowprops=dict(arrowstyle='->', color='black'), ha='center', va='bottom')

    ax.annotate(f"Min: {min_value:.2f}", xy=(min_year, min_value), xytext=(min_year, min_value - 5),
                arrowprops=dict(arrowstyle='->', color='black'), ha='center', va='top')

# 显示图形
plt.show()