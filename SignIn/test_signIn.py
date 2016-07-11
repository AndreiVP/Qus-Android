import libs.signInQus as sIn
import libs.locators as loc
import libs.helpers as h
import unittest
from config.config import setup, setup_first_signIn_test, tear_down_test, teardown

signIn_details = {'username': 'apopatest@mailinator.com',
				  'password': '111111'}

signInDetailsNoCredentials = {'username': '',
							  'password': ''}

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
		setup_first_signIn_test(self)

	def tearDown(self):
		tear_down_test(self)

	def test_signIn_scenarios(self):
		try:
			sIn.signIn(self, signInDetailsNoCredentials)
			sIn.check_error_message(self, 'Username is incorrect\nThe password needs to be at least 6 characters!')
			print('Sign In scenario with No Credentials was tested')
			h.find_and_click_element(self, loc.sign_in_alert_OK)
			sIn.signIn(self, signInDetailsNoUsername)
			sIn.check_error_message(self, 'Username is incorrect')
			h.find_and_click_element(self, loc.sign_in_alert_OK)
			print('Sign In scenario with No Username was tested')
			sIn.signIn(self, signInDetailsNoPassword)
			sIn.check_error_message(self, 'The password needs to be at least 6 characters!')
			h.find_and_click_element(self, loc.sign_in_alert_OK)
			print('Sign In scenario with No Password was tested')
			sIn.signIn(self, signInDetailsBadUsername)
			sIn.check_error_message(self, 'There was an error with your credentials. Please introduce valid ones.')
			h.find_and_click_element(self, loc.sign_in_alert_OK)
			print('Sign In scenario with Bad Username was tested')
			sIn.signIn(self, signInDetailsBadPassword)
			sIn.check_error_message(self, 'There was an error with your credentials. Please introduce valid ones.')
			h.find_and_click_element(self, loc.sign_in_alert_OK)
			print('Sign In scenario with Bad Password was tested')
			sIn.signIn(self, signIn_details)
			sIn.wait_for_sign_in(self)
			h.sign_out(self)
			print('Sign In scenario with Valid Credentials  was tested')
		except:
			h.take_screenshot(self, self.id())
			raise

	# def test_01_signIn_no_credentials(self):
	# 	sIn.signIn(self, signInDetailsNoCredentials)
	# 	sIn.check_error_message(self, 'Username is incorrect\nThe password needs to be at least 6 characters!')
	# 	h.find_and_click_element(self, loc.sign_in_alert_OK)
	#
	# def test_02_signIn_no_username(self):
	# 	sIn.signIn(self, signInDetailsNoUsername)
	# 	sIn.check_error_message(self, 'Username is incorrect')
	# 	h.find_and_click_element(self, loc.sign_in_alert_OK)
	#
	# def test_03_signIn_no_password(self):
	# 	sIn.signIn(self, signInDetailsNoPassword)
	# 	sIn.check_error_message(self, 'The password needs to be at least 6 characters!')
	# 	h.find_and_click_element(self, loc.sign_in_alert_OK)
	#
	# def test_04_signIn_bad_username(self):
	# 	sIn.signIn(self, signInDetailsBadUsername)
	# 	sIn.check_error_message(self, 'There was an error with your credentials. Please introduce valid ones.')
	# 	h.find_and_click_element(self, loc.sign_in_alert_OK)
	#
	# def test_05_signIn_bad_password(self):
	# 	sIn.signIn(self, signInDetailsBadPassword)
	# 	sIn.check_error_message(self, 'There was an error with your credentials. Please introduce valid ones.')
	# 	h.find_and_click_element(self, loc.sign_in_alert_OK)
	#
	# def test_06_signIn_valid_data(self):
	# 	sIn.signIn(self, signIn_details)
	# 	sIn.wait_for_sign_in(self)
	# 	h.sign_out(self)


if __name__ == '__main__':
	unittest.main()
