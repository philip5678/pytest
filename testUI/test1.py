import logging

import pytest
from ddt import ddt, file_data

log = logging.getLogger(__name__)
log.info('star')


def test01():
    print('test01')


@ddt
class TestCaseDemo:
    # kwargs = {"cherry": 3, "apple": 5}
    @file_data('../yaml_data/data1.yaml')
    def test_01111(self, *args, **kwargs):  # 将上面文件中（key-value）的value数据传进来，(如果是list，则将index想像为key)
        log.info('test_01111')
        print("kwargs:")
        print(kwargs)
        print(kwargs.get('cherry'))
        print(kwargs['cherry'])
        print("args:")
        print(args)


if __name__ == '__main__':
    pytest.main(['test1.py', '-vs'])
