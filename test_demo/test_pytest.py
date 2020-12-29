import logging

import pytest
from ddt import ddt, file_data


def test02():
    print('test01')


log = logging.getLogger(__name__)


@ddt
class TestCaseDemo1:
    # @file_data('../yaml_data/data1.yaml')
    # def test_01(self, **kwargs):
    #     # pass
    #     log.info('test_01---DDT from YAML')
    #     print("kwargs:")
    #     print(kwargs)
    #     print(kwargs.get('cherry'))

    @file_data('../yaml_data/data3.yaml')
    def test_03(self, *kwargs):
        # pass
        log.info('test_03---DDT from YAML')
        print("kwargs:")
        print(kwargs)
        print(kwargs[0][1])


if __name__ == '__main__':
    pytest.main(["./test_pytest.py"])
