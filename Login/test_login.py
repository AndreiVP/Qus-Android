
import libs.loginQus as log
import unittest
import time
import libs.locators as loc
from libs import helpers as h
from config.config import setup, setup_login_test, tear_down_test, teardown

login_details = {'username': 'apopatest@mailinator.com',
                'passwd': '111111'}

loginDetailsNoPassword = {'username': 'apopatest2@mailinator.com',
                'passwd': ''}

loginDetailsBadPassword = {'username': 'apopatest3@mailinator.com',
                'passwd': '111112'}

loginDetailsNoUsername = {'username': '',
                'passwd': '111111'}

loginDetailsBadUsername = {'username': 'apopatest00@mailinator.com',
                'passwd': '111111'}


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        setup(cls)

    @classmethod
    def tearDownClass(cls):
        teardown(cls)

    def setUp(self):
        setup_login_test(self)

    def tearDown(self):
        tear_down_test(self)

    def test_01_login_no_username(self):
        log.login(self, loginDetailsNoUsername)
        time.sleep(1)
        try:
            self.driver.find_elemet_by_id(loc.sign_in_alert_title)
            self.driver.find_elemet_by_id(loc.sign_in_alert_message)
            h.find_and_click_element(self, loc.sign_in_alert_OK)
        except:
            pass

    def test_02_login_no_password(self):
        log.login(self, loginDetailsNoPassword)
        time.sleep(1)
        try:
            self.driver.find_elemet_by_id(loc.sign_in_alert_title)
            self.driver.find_elemet_by_id(loc.sign_in_alert_message)
            h.find_and_click_element(self, loc.sign_in_alert_OK)
        except:
            pass

    def test_03_login_bad_username(self):
        log.login(self, loginDetailsBadUsername)
        time.sleep(1)
        try:
            self.driver.find_elemet_by_id(loc.sign_in_alert_title)
            self.driver.find_elemet_by_id(loc.sign_in_alert_message)
            h.find_and_click_element(self, loc.sign_in_alert_OK)
        except:
            pass

    def test_04_login_bad_password(self):
        log.login(self, loginDetailsBadPassword)
        time.sleep(1)
        try:
            self.driver.find_elemet_by_id(loc.sign_in_alert_title)
            self.driver.find_elemet_by_id(loc.sign_in_alert_message)
            h.find_and_click_element(self, loc.sign_in_alert_OK)
        except:
            pass

    def test_05_login_valid_data(self):
        log.login(self, login_details)
        log.wait_for_sign_in(self)



if __name__ == '__main__':
    unittest.main()
