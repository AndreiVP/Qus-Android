from libs import Search_home as search
import libs.locators as loc
from libs import helpers
import unittest
from config.config import setup, set_up_test, tear_down_test, teardown

class DemoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        setup(cls)

    @classmethod
    def tearDownClass(cls):
        teardown(cls)

    def setUp(self):
        set_up_test(self)

    def tearDown(self):
        tear_down_test(self)

#   def test_search(self):

if __name__ == '__main__':
    unittest.main()
