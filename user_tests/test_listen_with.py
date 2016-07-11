from libs import signInQus as sIn
import libs.locators as loc
import libs.helpers as h
import libs.Drawer_menu.navigationQus as nav
import libs.Listen_with.listenWithQus as lw
import unittest
from selenium import webdriver
from config.config import setup, setup_inApp_test, tear_down_test, teardown

login_details = {'username': 'apopatest@mailinator.com',
                 'passwd': '111111'}


class ListenWithTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		setup(cls)

	@classmethod
	def tearDownClass(cls):
		teardown(cls)

	def setUp(self):
		setup_inApp_test(self)
		#sIn.signIn_valid(self, 'apopatest@mailinator.com', '111111')

	def tearDown(self):
		tear_down_test(self)

	def test_search(self):
		try:
			nav.navigate_to_listen_with(self)
			h.check_no_items(self)
			lw.search_user(self, 'avp@mailinator.com')
			lw.wait_for_search(self)
			lw.follow_user_lw(self)
			lw.get_nickname_usercard(self, 'AVP')
			lw.open_user_card(self, 0)
			lw.open_user_section(self, 'Profile')
			lw.stop_following_user_up(self)
			h.tap_back_button(self)
			h.tap_back_button(self)
			h.tap_back_button(self)
			h.check_no_items(self)
		except:
			h.take_screenshot(self, self.id())
			raise



		print('Listen with flow scenario was tested')


if __name__ == '__main__':
	unittest.main()
