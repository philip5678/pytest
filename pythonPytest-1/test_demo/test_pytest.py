import logging

import pytest
from ddt import ddt, file_data


def test02():
    print('test01')


log = logging.getLogger(__name__)


@ddt
class TestCaseDemo1:
    @file_data('../yaml_data/data1.yaml')
    def test_0222(self, **kwargs):
        log.info('test_0222---DDT from YAML')
        print("kwargs:")
        print(kwargs)
        print(kwargs.get('cherry'))


if __name__ == '__main__':
    pytest.main()
