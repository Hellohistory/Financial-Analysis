# 历史行情数据-东财
import akshare as ak
import os
from tqdm import tqdm

# 获取用户输入的保存地址
save_dir = input("请输入保存地址:")

# 获取所有A股股票的实时行情
stock_df = ak.stock_zh_a_spot_em()

# 获取总的股票数量
total = len(stock_df)

# 遍历每只股票，使用 tqdm 显示进度条
for index, row in tqdm(stock_df.iterrows(), total=total):
    # 获取股票代码和名称
    stock_code = row['代码']
    stock_name = row['名称']

    # 替换股票名称中的"*"为"#"
    stock_name = stock_name.replace('*', '#') #在Windows当中文件无法使用*命名，因此使用#替代*号

    # 获取股票的历史数据
    stock_hist_df = ak.stock_zh_a_hist(symbol=stock_code, period="daily", start_date="20000101", end_date='20230723', adjust="qfq")

    # 保存到Excel文件
    file_name = f"{stock_code}_{stock_name}.xlsx"
    file_path = os.path.join(save_dir, file_name)
    stock_hist_df.to_excel(file_path, index=False)