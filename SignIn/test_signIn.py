import libs.signInQus as log
import libs.locators as loc
import libs.helpers as h
import unittest
import time
from config.config import setup, setup_signIn_test, tear_down_test, teardown

signIn_details = {'username': 'apopatest@mailinator.com',
                 'password': '111111'}

signInDetailsNoPassword = {'username': 'apopatest2@mailinator.com',
                          'password': ''}

signInDetailsBadPassword = {'username': 'apopatest3@mailinator.com',
                           'password': '111112'}

signInDetailsNoUsername = {'username': '',
                          'password': '111111'}

signInDetailsBadUsername = {'username': 'apopatest00@mailinator.com',
                           'password': '111111'}


class signInTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		setup(cls)

	@classmethod
	def tearDownClass(cls):
		teardown(cls)

	def setUp(self):
		setup_signIn_test(self)

	def tearDown(self):
		tear_down_test(self)

	def test_01_signIn_no_username(self):
		log.signIn(self, signInDetailsNoUsername)
		time.sleep(1)
		try:
			self.driver.find_element_by_id(loc.sign_in_alert_title)
			self.driver.find_element_by_id(loc.sign_in_alert_message)
			h.find_and_click_element(self, loc.sign_in_alert_OK)
		except:
			pass

	def test_02_signIn_no_password(self):
		log.signIn(self, signInDetailsNoPassword)
		time.sleep(1)
		try:
			self.driver.find_element_by_id(loc.sign_in_alert_title)
			self.driver.find_element_by_id(loc.sign_in_alert_message)
			h.find_and_click_element(self, loc.sign_in_alert_OK)
		except:
			pass

	def test_03_signIn_bad_username(self):
		log.signIn(self, signInDetailsBadUsername)
		time.sleep(1)
		try:
			self.driver.find_element_by_id(loc.sign_in_alert_title)
			self.driver.find_element_by_id(loc.sign_in_alert_message)
			h.find_and_click_element(self, loc.sign_in_alert_OK)
		except:
			pass

	def test_04_signIn_bad_password(self):
		log.signIn(self, signInDetailsBadPassword)
		time.sleep(1)
		try:
			self.driver.find_element_by_id(loc.sign_in_alert_title)
			self.driver.find_element_by_id(loc.sign_in_alert_message)
			h.find_and_click_element(self, loc.sign_in_alert_OK)
		except:
			pass

	def test_05_signIn_valid_data(self):
		log.signIn(self, signIn_details)
		log.wait_for_sign_in(self)


if __name__ == '__main__':
	unittest.main()
