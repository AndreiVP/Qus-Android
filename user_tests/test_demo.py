from libs.Search_home import searchQus as src
from libs import loginQus as log
import libs.locators as loc
from libs import helpers as h
import unittest
from config.config import setup, setup_inapp_test, tear_down_test, teardown

login_details = {'username': 'apopatest@mailinator.com',
                'passwd': '111111'}
search_text = 'Major Lazer'

class DemoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        setup(cls)

    @classmethod
    def tearDownClass(cls):
        teardown(cls)

    def setUp(self):
        setup_inapp_test(self)

    def tearDown(self):
        tear_down_test(self)


    def test_search(self):
        src.perform_search(self, search_text)
        h.wait_for_search(self)

if __name__ == '__main__':
    unittest.main()
