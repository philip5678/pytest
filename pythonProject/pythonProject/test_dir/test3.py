import time
import pytest
import os
import allure
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver import Ie
from selenium.webdriver import Edge
from selenium.webdriver import Firefox

global driver


@pytest.fixture(scope='module', autouse=True)
def beforeEach():
    # https://www.selenium.dev/documentation/en/webdriver/driver_requirements/
    global driver
    print('open browser')
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    # driver = webdriver.Edge() #it does not work
    # driver = webdriver.Ie() #it does not work

    yield
    afterEach()


def afterEach():
    global driver
    print('close browser!')
    driver.quit()


searchList = ['cheese', 'apple', 'pearl', 'cherry']


@allure.title('测试用例标题1')
@allure.description('这是测试用例用例1的描述信息')
@allure.feature('search')
@allure.story('food')
@pytest.mark.parametrize('searchItem', searchList)
@pytest.mark.productmanagement  # 在pytest.ini中还要设置markers
def test_google_search(searchItem, qqq):
    global driver
    wait = WebDriverWait(driver, 10)
    driver.get("https://google.com/ncr")
    # driver.get("https://www.msn.com/en-us/")
    driver.maximize_window()  # 将浏览器最大化显示
    # driver.set_window_size(480, 800)  # 参数数字为像素点
    time.sleep(2)
    driver.find_element_by_name("q").send_keys(searchItem + Keys.RETURN)  # 加回车进行搜索
    first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "#rcnt")))
    driver.save_screenshot(f"C:/Users/zhb68/PycharmProjects/pythonProject/report/screenshot/test-{str(qqq)}-{searchItem}.png")
    # print(first_result.get_attribute("textContent"))
    print('title: ' + driver.title)
    assert 'Google' in driver.title
    print("fixture test - " + str(qqq) + searchItem)


product_list = [{'apple', 2}, {'cherry', 5}]


@allure.step(title="first step")
@allure.title('测试用例标题2')
@allure.description('这是测试用例用例2的描述信息')
@allure.feature('search')
@allure.story('utility')
@pytest.mark.run(order=3)
@pytest.mark.smoke  # 在pytest.ini中还要设置markers
@pytest.mark.parametrize('product', product_list)
def test_google_search_product(product):
    print(product)
    time.sleep(1)


# 0 > 正数 > 没有参与的用例 > 负数
# 正数和负数就是按照大小关系排列的
@pytest.mark.run(order=1)
@allure.feature('sales')
@allure.story('furniture')
@pytest.mark.usermanagement  # 在pytest.ini中还要设置markers
def test_google_search_furniture():
    print('search furniture')
    time.sleep(1)


@pytest.fixture(scope="function", params=['中国', '加拿大', '美国'], autouse=True, ids=['China', 'Canada', 'USA'], name="qqq")
def my_fixture(request):
    print("前置 fixture practice")
    yield request.param
    my_after_fixture()


def my_after_fixture():
    print("后置 fixture practice")


def test_fixture(qqq):  # 当autouse=False时，要手动加上用fixture
    print("fixture test - " + str(qqq))


if __name__ == '__main__':
    pytest.main()  # 按pytest.ini设置运行
    # pytest.main(['../test_dir'])  # 运行指定目录，并重载pytest.ini
    # pytest.main(['../test_dir/test3.py'])  # 运行指定文件（模块），并重载pytest.ini
    # pytest.main(['../test_dir/test3.py::test_google_search_furniture'])  # 运行指定函数，并重载pytest.ini
    # pytest.main(['../test_dir/main.py::TestStringMethods::test_upper'])  # 运行指定类中的方法，并重载pytest.ini
    # pytest.main(["test3.py", "-s", "--alluredir=../report/allure-json"])  # 设置在pytest.ini中
    # os.system("allure serve ../report/allure-json")  # 打开html形式的报告
    # os.system("allure open ../report/allure-json")  # 打开json形式的报告
    os.system("allure generate ../report/allure-json -o ../report/allure-html -c")  # 生成html形式的报告
    os.system("allure open ../report/allure-html")  # 打开html形式的报告
