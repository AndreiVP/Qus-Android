import libs.Search.searchQus as src
from libs import signInQus as sIn
import libs.locators as loc
import libs.helpers as h
import libs.More_options_menu.moreOptionsMenu as mom
import libs.Queue.queueQus as qu
import libs.Drawer_menu.navigationQus as nav
import libs.Playlists.playlistsQus as pla
import unittest
from config.config import setup, setup_signIn_test, tear_down_test, teardown

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
		setup_signIn_test(self)

	def tearDown(self):
		tear_down_test(self)

	def test_search(self):
		sIn.signIn_valid(self, 'apopatest@mailinator.com', '111111')
		src.perform_search(self, search_text)
		h.is_not_visible(self, loc.search_loading_spinner)
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
		h.sign_out(self)
		print('Happy flow scenario was tested')


if __name__ == '__main__':
	unittest.main()
