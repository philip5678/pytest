import logging
import unittest
import HtmlTestRunner
import pytest
from pytest import fixture

import logging

caplog = logging.getLogger(__name__)

caplog.info("logging information")

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_error(self):
        """ This test should be marked as error one. """
        caplog.set_level(logging.INFO)
        caplog.set_level(logging.CRITICAL, logger="root.baz")
        raise ValueError

    def test_fail(self):
        """ This test should fail. """
        self.assertEqual(1, 2)

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report/html'))
