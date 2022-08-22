from __future__ import print_function

import logging
import unittest
from unittest import TestCase

import HTMLTestRunner
import pytest
from selenium import webdriver

log = logging.getLogger(__name__)


class TestClass(TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('setup_class()')
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://www.baidu.com")
        log.info("xxxxxxxxxxxxxxx")

    @classmethod
    def teardown_class(cls):
        log.info('teardown_class()')

    def setUp(self):
        log.info('\nsetup_method()')
        self.addCleanup(self.screen_shot)

    def screen_shot(self):
        log.info("yyyyyyyyyyyyyy")
        log.info("sereen_shot")

    def qqq(self):
        log.info("xxxxxxxxxxxqqqq")
        assert 4 == 5

    # def teardown_method(self, method):
    def tearDown(self):
        log.info("ffjiafuiodafdfj___teardown")

    @pytest.mark.slow
    def test_7(self):
        import time
        time.sleep(10)
        log.info('- test_7()')

    @pytest.mark.qq
    def test_4(self):
        # import pdb
        # pdb.set_trace()
        # self.result = self.addCleanup(self.qqq)
        log.info('- test_4()')

    def test_5(self):
        log.info('- test_4()')
        assert 4 == 5


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_error(self):
        """ This test should be marked as error one. """
        log.info('- test_error()')
        raise ValueError

    def test_fail(self):
        """ This test should fail. """
        self.assertEqual(1, 2)

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass


if __name__ == '__main__':
    unittest.main()
