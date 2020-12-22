import os

import pytest

if __name__ == '__main__':
    pytest.main()
    os.system("allure generate ./report/allure-json -o ./report/allure-html -c")  # 生成html形式的报告
    os.system("allure open ./report/allure-html")  # 打开html形式的报告
