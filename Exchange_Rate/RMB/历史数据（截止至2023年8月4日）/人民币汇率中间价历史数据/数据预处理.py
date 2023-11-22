import pandas as pd

# 加载文件
file_path1 = "D:\Code Work\Financial Analysis\Exchange_Rate\RMB\历史数据（截止至2023年8月4日）\Rawdata\人民币汇率历史数据_原始数据\人民币汇率中间价历史数据.xlsx"
data1 = pd.read_excel(file_path1)

# 清理缺失或异常值：将非数字字符转换为NaN
data1_cleaned = data1.replace('---', float('nan'))

# 转换汇率列为适当的数字类型
for column in data1_cleaned.columns[1:]:
    data1_cleaned[column] = pd.to_numeric(data1_cleaned[column], errors='coerce')

# 格式化日期列
data1_cleaned['日期'] = pd.to_datetime(data1_cleaned['日期'])
