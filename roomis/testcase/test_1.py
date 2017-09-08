import time
import unittest

import config
import initenv

url = config.domain


class Testmanagespace1(unittest.TestCase):
    def setUp(self):
        print('setup')

    def test_createspace1(self):
        print('case1')

    def test_deletespace(self):
        print('case2')

    def test_deletespace2(self):
        print('case3')

    def tearDown(self):
        print('teardown')


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Testmanagespace1)
    unittest.TextTestRunner(verbosity=2).run(suite)
