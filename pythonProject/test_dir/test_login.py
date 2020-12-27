import os
import time
import allure
import pytest

product_list = [['apple', 2], ['cherry', 5]]

@allure.step(title="first step")
@allure.title('测试用例标题2')
@allure.description('这是测试用例用例2的描述信息')
@allure.feature('search')
@allure.story('utility')
@pytest.mark.run(order=3)
@pytest.mark.smoke  # 在pytest.ini中还要设置markers
@pytest.mark.parametrize('product,price', product_list)
def test_google_search_product(product, price):
    print(product, price)
    time.sleep(1)


def test1():
    time.sleep(1)
    print('run 第一个 test')


class TestCase:
    def test_something(self):
        # self.assertEqual(True, False)
        time.sleep(1)
        print('run 第二个 test')
        assert 1 == 1


if __name__ == '__main__':
    pytest.main()
    # pytest.main(['test_login.py', '-vs'])  # -v verbose, -n 运行线程数 reruns是让失败的测试再运行的次数 这行运行不是很好
    # terminal运行命令：pytest -vs -n=2 --reruns=6 test_login.py  #这个运行不出错
    # os.system("allure serve ../report/allure-json")
    # os.system("allure open ../report/allure-json")
    os.system("allure generate ../report/allure-json -o ../report/allure-html -c")  # 生成html形式的报告
    os.system("allure open ../report/allure-html")  # 打开html形式的报告
