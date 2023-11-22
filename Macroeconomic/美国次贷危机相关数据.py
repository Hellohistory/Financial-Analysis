import matplotlib.pyplot as plt
import matplotlib as mpl

# 准备数据
years = ['2001', '2004', '2006', '2007']
household_debt = [77, 100, 127, 127]  # 债务占年度可支配个人收入的百分比
subprime_market = [10, 18, 21, 21]  # 次级抵押贷款占总贷款的百分比
foreclosure_rates = [5, 16, 25, 25]  # 可调整利率抵押贷款的逾期率（90天或房屋拍卖）
housing_price_decline = [0, 0, -20, -20]  # 房价自2006年中期以来的下降百分比

# 设置中文字体为微软雅黑
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']
mpl.rcParams['axes.unicode_minus'] = False

# 创建图表
fig, ax1 = plt.subplots(figsize=(10, 6))

# 双轴图表
ax2 = ax1.twinx()
ax1.plot(years, household_debt, 'g-', label='家庭债务占可支配收入比例 (%)')
ax2.plot(years, subprime_market, 'b-', label='次级抵押贷款占总贷款比例 (%)')
ax2.plot(years, foreclosure_rates, 'r-', label='抵押贷款逾期率 (%)')
ax2.plot(years, housing_price_decline, 'y-', label='房价下跌比例 (%)')

# 标题和标签
ax1.set_xlabel('年份')
ax1.set_ylabel('家庭债务占可支配收入比例 (%)', color='g')
ax2.set_ylabel('贷款比例 / 逾期率 / 房价下跌比例 (%)', color='b')
ax1.set_title('2007年次贷危机关键数据指标')

# 图例
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# 提高Y轴精度
plt.gca().yaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%.2f'))

# 提高图像清晰度
plt.savefig('2007年美国次贷危机.png', dpi=300)

plt.show()
