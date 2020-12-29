import logging

import pytest
from ddt import ddt, file_data


log = logging.getLogger(__name__)


@ddt
class TestCaseDemo1:
    @file_data('../yaml_data/data1.yaml')
    def test_01(self, **kwargs):
        log.info('test_01---DDT from YAML')
        print(type(kwargs))
        print("kwargs:")
        print(kwargs)
        print(kwargs.get('cherry'))


if __name__ == '__main__':
    pytest.main(["./test_pytest1.py"])
