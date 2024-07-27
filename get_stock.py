import akshare as ak
import pandas as pd

stock_info_a_code_name_df = ak.stock_info_a_code_name()
df = pd.DataFrame(stock_info_a_code_name_df)
df.to_csv("stock_info_a_code_name_df.csv", index=False)
