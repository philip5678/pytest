# 导入pandas

import pandas as pd

# #方法一：默认读取第一个表单
# df=pd.read_excel('lemon.xlsx')#这个会直接默认读取到这个Excel的第一个表单
# data=df.head()#默认读取前5行的数据
# print("获取到所有的值:\n{0}".format(data))#格式化输出
# #方法二：通过指定表单名的方式来读取
# df=pd.read_excel('lemon.xlsx',sheet_name='student')#可以通过sheet_name来指定读取的表单
# data=df.head()#默认读取前5行的数据
# print("获取到所有的值:\n{0}".format(data))#格式化输出
# #方法三：通过表单索引来指定要访问的表单，0表示第一个表单
# #也可以采用表单名和索引的双重方式来定位表单
# #也可以同时定位多个表单，方式都罗列如下所示
# df=pd.read_excel('lemon.xlsx',sheet_name=['python','student'])#可以通过表单名同时指定多个
# # df=pd.read_excel('lemon.xlsx',sheet_name=0)#可以通过表单索引来指定读取的表单
# # df=pd.read_excel('lemon.xlsx',sheet_name=['python',1])#可以混合的方式来指定
# # df=pd.read_excel('lemon.xlsx',sheet_name=[1,2])#可以通过索引 同时指定多个
# data=df.values#获取所有的数据，注意这里不能用head()方法哦~
# print("获取到所有的值:\n{0}".format(data))#格式化输出

# usecols=[1,2]读取excel的第二第三列
df = pd.read_excel('test_data.xlsx', sheet_name=[0, 'add_test',2])
# df = pd.read_excel('test_data.xlsx', sheet_name='add_test', na_values='n/a')
print(df[0].values)
print(df['add_test'].values)
print(df[2].values)

a = df[0]  # 打开Sheet1
# 和 a = df["Sheet1"]效果相同
b = a["CompanyName"]  # 获取所有Name
# b[0] = "Name_a"
# b[1] = "Name_b"
# 想要修改b的参数，可以直接赋值
for i in range(len(b)):
    b[i] = i
# 现在b就发生了变化
print(df)

# 1. 当只需要写入一个sheet时
df[0].to_excel("1.xlsx", sheet_name="Sheet1")
# 2. 当需要写入多个sheet时
writer = pd.ExcelWriter('multiple.xlsx')
df[0].to_excel(writer, sheet_name="Sheet1")
df[2].to_excel(writer, sheet_name="Sheet2")
df['add_test'].to_excel(writer, sheet_name="Sheet3")
writer.save()

# https://www.cnblogs.com/liulinghua90/p/9935642.html

# pip install xlrd==1.2.0 #才可打开xlsx文件
#
# 问题描述：
# RuntimeError: The current Numpy installation ('D:\\soft1\\Python37\\lib\\site-packages\\numpy\\__init__.py') fails to pass a sanity check due to a bug in the windows runtime. See this issue for more information: https://tinyurl.com/y3dm3h86
# 解决方案：
# 先卸载numpy：pip uninstall numpy
# 在安装：pip install numpy==1.19.3
