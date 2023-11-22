# 中国宏观杠杆率
import akshare as ak
import pandas as pd
import os

# 使用akshare库获取宏观经济数据
macro_cnbs_df = ak.macro_cnbs()

# 将数据保存到指定的Excel表格中
excel_file_path = '中国宏观杠杆率.xlsx'

# 检查文件是否存在，如果不存在则创建新的Excel文件
if not os.path.exists(excel_file_path):
    # 创建一个空的DataFrame
    empty_df = pd.DataFrame()
    # 将DataFrame保存为Excel文件，这样就创建了一个空的Excel文件
    empty_df.to_excel(excel_file_path, index=False, engine='openpyxl')

# 将数据保存到Excel文件中，注意指定sheet_name和index参数
macro_cnbs_df.to_excel(excel_file_path, sheet_name='宏观经济数据', index=False, engine='openpyxl')

print("数据已保存到Excel表格中：", excel_file_path)