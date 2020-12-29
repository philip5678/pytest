from ddt import ddt, file_data
import unittest


def test01():
    print('test01')


@ddt
class TestCaseDemo(unittest.TestCase):
    @file_data('../yaml_data/data1.yaml')
    def test_01111(self, **kwargs):
        print("kwargs:")
        print(kwargs)
        print(kwargs.get('cherry'))


if __name__ == '__main__':
    unittest.main()