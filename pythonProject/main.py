import logging
import os

import pytest

if __name__ == '__main__':
    pytest.main()  # 按pytest.ini设置运行

    # pytest.main(['./test_dir'])  # 运行指定目录，并重载pytest.ini
    # pytest.main(['./test_dir/test3.py'])  # 运行指定文件（模块），并重载pytest.ini
    # pytest.main(['./test_dir/test3.py::test_google_search_furniture'])  # 运行指定函数，并重载pytest.ini
    # pytest.main(['../test_dir/main.py::TestStringMethods::test_upper'])  # 运行指定类中的方法，并重载pytest.ini
    # pytest.main(["test3.py", "-s", "--alluredir=../report/allure-json"])  # 设置在pytest.ini中
    # os.system("allure serve ./report/allure-json")  # 打开html形式的报告
    # os.system("allure open ./report/allure-json")  # 打开json形式的报告
    # os.system("allure generate ./report/allure-json -o ./report/allure-html -c")  # 生成html形式的报告
    # os.system("allure open ./report/allure-html")  # 打开html形式的报告

    root_path = "C:/Users/zhb68/PycharmProjects/pythonProject/"
    os.system(f"allure generate {root_path}report/allure-json -o {root_path}report/allure-html -c")  # 生成html形式的报告
    # os.system(f"allure open {root_path}report/allure-html")  # 打开html形式的报告
