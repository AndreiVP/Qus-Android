import libs.first_runQus as ins
import unittest
import time
import libs.locators as loc
from libs import helpers as h
from config import config as conf
from config.config import setup, set_up_test, tear_down_test, teardown


class InstallTest(unittest.TestCase):
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

    def welcome_screen(self):
        ins.check_welcome_Qus(self)

    def open_register(self):
        ins.open_sign_up(self)

    def open_login(self):
        ins.open_sign_in(self)



if __name__ == '__main__':
    unittest.main()
