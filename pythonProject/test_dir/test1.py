import unittest

import time
import HtmlTestRunner


class AlienTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("TestCase  start running ")

    @staticmethod
    def test_1_run():
        print("hello world_1")

    @staticmethod
    def test_2_run():
        print("hello world_2")

    @staticmethod
    def test_3_run():
        print("hello world_3")


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_error(self):
        """ This test should be marked as error one. """
        raise ValueError

    def test_fail(self):
        """ This test should fail. """
        self.assertEqual(1, 2)

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass


if __name__ == '__main__':
    print('hello world')
    suite = unittest.makeSuite(AlienTest)
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    filename = now + "_result.html"
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='report/html'))
