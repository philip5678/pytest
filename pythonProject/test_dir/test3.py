import time
from _pytest import main
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
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    # driver = webdriver.Edge() #it does not work
    # driver = webdriver.Ie() #it does not work

    yield
    afterEach()


def afterEach():
    global driver
    driver.quit()


searchList = ['cheese', 'apple', 'pearl', 'cherry']


@allure.title('测试用例标题1')
@allure.description('这是测试用例用例1的描述信息')
@allure.feature('search')
@allure.story('food')
@pytest.mark.parametrize('searchItem', searchList)
@pytest.mark.productmanagement #在pytest.ini中还要设置markers
def test_google_search(searchItem):
    global driver
    wait = WebDriverWait(driver, 10)
    driver.get("https://google.com/ncr")
    # driver.get("https://www.msn.com/en-us/")
    driver.find_element_by_name("q").send_keys(
        searchItem + Keys.RETURN)  # 加回车进行搜索
    first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "#rcnt")))
    print(first_result.get_attribute("textContent"))
    print('title: ' + driver.title)
    assert 'Google' in driver.title


@allure.title('测试用例标题1')
@allure.description('这是测试用例用例1的描述信息')
@allure.feature('search')
@allure.story('utility')
@pytest.mark.run(order=3)
@pytest.mark.smoke #在pytest.ini中还要设置markers
def test_google_search_product():
    print('search item')
    time.sleep(1)


# 0 > 正数 > 没有参与的用例 > 负数
# 正数和负数就是按照大小关系排列的
@pytest.mark.run(order=1)
@allure.feature('sales')
@allure.story('furniture')
@pytest.mark.usermanagement #在pytest.ini中还要设置markers
def test_google_search_furniture():
    print('search furniture')
    time.sleep(1)


if __name__ == '__main__':
    pytest.main() #运行当前目录下所有 包括子目录
    # pytest.main(['../test_dir']) #运行指定目录
    # pytest.main(['../test_dir/test3.py']) #运行指定文件（模块）
    # pytest.main(['../test_dir/test3.py::test_google_search_furniture']) #运行指定函数
    # pytest.main(['../test_dir/main.py::TestStringMethods::test_upper']) #运行指定类中的方法
    # pytest.main(["test3.py", "-s", "--alluredir=../report/allure"]) #设置在pytest.ini中
    os.system("allure serve ../report/allure")
