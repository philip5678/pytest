# 导入pandas

import pandas as pd

# usecols=[1,2]读取excel的第二第三列
pf = pd.read_excel('test_data.xlsx', sheet_name='add_test', na_values='n/a')
print(pf.values)
