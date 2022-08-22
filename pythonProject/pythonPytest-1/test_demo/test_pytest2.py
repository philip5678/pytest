import logging

import pytest
from ddt import ddt, file_data

log = logging.getLogger(__name__)


@ddt
class TestCaseDemo1:

    @file_data('../yaml_data/data2.yaml')
    # def test_02(self, *args ):
    # def test_02(self, **kwargs ):
    def test_02(self, *args, **kwargs ):
        log.info('test_02---DDT from YAML')
        print(type(args), type(kwargs))
        print(f'"args:" {args}, "kwargs:" {kwargs}')
        if args:
           print(args[0])
           # print(args[0][0])


if __name__ == '__main__':
    pytest.main(["./test_pytest2.py"])
