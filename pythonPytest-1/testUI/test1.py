import os

import pytest
# from ddt import ddt, file_data
import allure


def test01():
    print('test01')


# @ddt
class TestCaseDemo:
    # @file_data('../data/data1.yaml')
    kwargs = {"cherry": 3, "apple": 5}

    def test_01111(self, **kwargs):
        print("kwargs:")
        print(kwargs)
        print(kwargs.get('cherry'))




