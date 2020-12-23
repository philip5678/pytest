# 导入pandas

import pandas as pd

# usecols=[1,2]读取excel的第二第三列
pf = pd.read_excel('test_data.xlsx', sheet_name='add_test', na_values='n/a')
print(pf.values)


# pip install xlrd==1.2.0 #才可打开xlsx文件
#
# 问题描述：
# RuntimeError: The current Numpy installation ('D:\\soft1\\Python37\\lib\\site-packages\\numpy\\__init__.py') fails to pass a sanity check due to a bug in the windows runtime. See this issue for more information: https://tinyurl.com/y3dm3h86
# 解决方案：
# 先卸载numpy：pip uninstall numpy
# 在安装：pip install numpy==1.19.3