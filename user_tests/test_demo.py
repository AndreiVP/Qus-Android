import libs.Search.searchQus as src
from libs import signInQus as sIn
import libs.locators as loc
import libs.helpers as h
import libs.More_options_menu.moreOptionsMenu as mom
import libs.Queue.queueQus as qu
import libs.Drawer_menu.navigationQus as nav
import libs.Playlists.playlistsQus as pla
import libs.signUpQus as sUp
import libs.Listen_with.listenWithQus as lw
import unittest
from time import strftime
from config.config import setup, set_up_test, tear_down_test, teardown

login_details = {'username': 'apopatest@mailinator.com',
                 'passwd': '111111'}
search_text = 'Major Lazer'

unic = strftime("%a%d%b%Y%H%M")
email = 'auto{}'.format(unic)

registration_details = {'nickname': '{}'.format(email),
                        'email': '{}@mailinator.com'.format(email),
                        'password': '111111'
                        }

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

	def test_search(self):
		try:
			sUp.registration(self, registration_details)
			sUp.wait_for_registration(self)
			sUp.signin_after_signup(self, registration_details)
			src.perform_search(self, search_text)
			h.is_not_visible_by_id(self, loc.search_loading_spinner)
			h.expand_music_section(self, 2)
			h.tap_add_button(self, 0)
			mom.play_now(self)
			h.open_queue(self)
			qu.open_track_more_menu(self, 2)
			mom.add_to_new_playlist(self)
			nav.navigate_to_playlists(self)
			pla.open_playlist(self, 0)
			pla.return_to_playlists_list(self)
			pla.delete_playlist(self, 0)
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
			h.sign_out(self)
		except:
			h.take_screenshot(self, self.id())
			raise
	#print('Happy flow scenario was tested')


if __name__ == '__main__':
	unittest.main()
