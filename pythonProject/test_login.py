import os
import time
import allure
import pytest


def test1():
    time.sleep(1)
    print('run 第一个 test')


class TestCase:
    def test_something(self):
        # self.assertEqual(True, False)
        time.sleep(1)
        print('run 第二个 test')
        assert 1 == 2


if __name__ == '__main__':
    pytest.main()
    # pytest.main(['test_login.py', '-vs'])  # -v verbose, -n 运行线程数 reruns是让失败的测试再运行的次数 这行运行不是很好
    # terminal运行命令：pytest -vs -n=2 --reruns=6 test_login.py  #这个运行不出错
    os.system("allure serve report/allure")
    # os.system("allure open report/allure")
