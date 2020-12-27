import logging
import os
import shutil

import pytest

log = logging.getLogger(__name__)

if __name__ == '__main__':
    log.info("Test start....")
    # pytest.main()  # 按pytest.ini设置运行

    # pytest.main(['./test_dir'])  # 运行指定目录，并重载pytest.ini
    # pytest.main(['./test_dir/test3.py'])  # 运行指定文件（模块），并重载pytest.ini
    # pytest.main(['./test_dir/test3.py::test_google_search_furniture'])  # 运行指定函数，并重载pytest.ini
    # pytest.main(['../test_dir/main.py::TestStringMethods::test_upper'])  # 运行指定类中的方法，并重载pytest.ini
    # pytest.main(["test3.py", "-s", "--alluredir=../report/allure-json"])  # 设置在pytest.ini中
    # os.system("allure serve ./report/allure_json")  # 打开html形式的报告
    # os.system("allure open ./report/allure_json")  # 打开json形式的报告
    # os.system("allure generate ./report/allure_json -o ./report/allure_html -c")  # 生成html形式的报告
    # os.system("allure open ./report/allure_html")  # 打开html形式的报告

    # root_path = "C:/Users/zhb68/PycharmProjects/pythonPytest-1/"
    # os.system(f"allure generate {root_path}report/allure_json -o {root_path}report/allure_html -c")  # 生成html形式的报告
    # os.system(f"allure open {root_path}report/allure_html")  # 打开html形式的报告

    # ————————————————————————————————————————————————————————————————————————————————————————————
    print(f'{(root_path := os.getcwd())=}')
    print(f'{(root_path := os.path.dirname(__file__))=}')
    print(f'{(root_path := os.path.curdir)=}')
    print(f'{(root_path := os.path.abspath("."))=}')  # use absolut dir is the best way
    print(f'{(root_path := os.path.realpath("."))=}')

    print(f'{(allure_json_dir := os.path.join(root_path, "report/allure_json"))=}')
    print(f'{(allure_html_dir := os.path.join(root_path, "report/allure_html"))=}')
    print(f'{(htmlcov_dir := os.path.join(root_path, "htmlcov"))=}')
    print(f'{(screenshot_dir := os.path.join(root_path, "report/screenshot"))=}')
    HtmlTestRunner_path = os.path.join(root_path, "report/report.html")

    if os.path.exists(allure_json_dir):
        shutil.rmtree(os.path.join(allure_json_dir, '..'))
    if os.path.exists(htmlcov_dir):
        shutil.rmtree(htmlcov_dir)
    if os.path.exists(screenshot_dir):
        shutil.rmtree(screenshot_dir)
    os.makedirs(allure_json_dir)
    os.makedirs(allure_html_dir)
    os.makedirs(htmlcov_dir)
    os.makedirs(screenshot_dir)

    pytest.main(
        [root_path, '-vs', f'--html={HtmlTestRunner_path}', f'--alluredir={allure_json_dir}', f'--cov={root_path}',
         '--cov-report=html'])  # 按pytest.ini设置运行

    os.system(f"allure generate {allure_json_dir} -o {allure_html_dir} -c")  # 生成html形式的报告
    os.system(f"allure open {allure_html_dir}")  # 打开html形式的报告
    # os.system(f"allure serve {allure_json_dir}")  # 打开html形式的报告
    # os.system(f"allure open {allure_json_dir}")  # 打开json形式的报告
