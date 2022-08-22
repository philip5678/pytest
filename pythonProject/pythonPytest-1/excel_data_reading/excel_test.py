# python3.6
# coding=utf-8
# author=刘一凡
'''
支持pytest excel数据驱动。
'''
import pytest
import xlrd   # pip install xlrd==1.2.0 #才可打开xlsx文件


# 把excel sheet解析为双层列表，每一个行是一个外层元素，每个单元格是一个内层元素。
def sheet_to_list(excel_file_path, sheet_name):
    lst = []
    with xlrd.open_workbook(excel_file_path, formatting_info=False) as f:
        table = f.sheet_by_name(sheet_name)
        # nrows是sheet的行数
        for row in range(0, table.nrows):
            lst.append([])
            # ncols是sheet的列数
            for col in range(0, table.ncols):
                # ctype为1是字符串，ctype为2是数值。
                cell_type = table.cell(row, col).ctype
                cell_value = table.cell_value(row, col)
                # 去掉字符串首尾空格。excel会自动去掉整数和浮点数前后的空格。
                if cell_type == 1:
                    lst[row].append(cell_value.strip())
                # xlrd读取cell时1变成1.0。如果是数值，并且原本是整数，则返回整数。
                elif cell_type == 2 and cell_value == round(cell_value):
                    lst[row].append(int(cell_value))
                # 浮点数则不用额外处理
                else:
                    lst[row].append(cell_value)
    print("\n_________________________________________________________________________")
    print(lst)
    return lst


# 从excel sheet中获取@pytest.mark.parametrize()所需要的参数名和数据
def get_data_from_sheet(excel_file_path, sheet_name):
    lst = sheet_to_list(excel_file_path, sheet_name)
    # 参数名格式化，格式为"a,b,c"
    param_name = ','.join(lst[0])
    # 去掉参数名行，剩下的就是数据
    data = lst[1:]
    print("_________________________________________________________________________")
    print(param_name, data)
    return param_name, data


# 使用举例：
@pytest.mark.parametrize(*get_data_from_sheet("./test_data.xlsx", "add_test"))
def test_add(CorporateID, CompanyName, StreetAddress):
    print("\n_________________________________________________________________________")
    print(CorporateID, CompanyName, StreetAddress)
    assert CorporateID + CompanyName == StreetAddress


if __name__ == '__main__':
    # print("_________________________________________________________________________")
    # param, data_ = get_data_from_sheet("./test_data.xlsx", "add_test")
    # print(param, data_)
    # print("_________________________________________________________________________")
    # list_ = sheet_to_list("./test_data.xlsx", "add_test")
    # print(list_)
    pytest.main(['-vs', 'excel_test.py'])

'''
运行结果如下：
>pytest pytest_ddt_excel.py -v
============================= test session starts =============================
collected 4 items
pytest_ddt_excel.py::test_add[1-2-3] PASSED                              [ 25%]
pytest_ddt_excel.py::test_add[abc-def-abcdef] PASSED                     [ 50%]
pytest_ddt_excel.py::test_add[abc-123-abc123] PASSED                     [ 75%]
pytest_ddt_excel.py::test_add[1.8-2.6-4.4] PASSED                        [100%]
========================== 4 passed in 0.11 seconds ===========================
'''
