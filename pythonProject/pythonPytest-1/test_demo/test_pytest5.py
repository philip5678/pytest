import logging

import pytest
from ddt import ddt, file_data


log = logging.getLogger(__name__)


@ddt
class TestCaseDemo1:

    @file_data('../yaml_data/data5.yaml')
    def test_05(self, **kwargs):
        log.info('test_05---DDT from YAML')
        print(type(kwargs))
        print("kwargs:")
        print(kwargs)
        # print(kwargs[0][0])


if __name__ == '__main__':
    pytest.main(["./test_pytest5.py"])
