import libs.locators as loc
from time import strftime

unic = strftime("%a%d%b%Y")
playlist_name = 'auto{}'.format(unic)


def play_now(self):
	button = self.driver.find_element_by_name('Play now')
	button.click()


def play_next(self):
	button = self.driver.find_element_by_name('Play next')
	button.click()


def add_to_queue(self):
	button = self.driver.find_element_by_name('Add to queue')
	button.click()


def remove_from_queue(self):
	button = self.driver.find_element_by_name('Remove song from queue')
	button.click()


def add_to_new_playlist(self):
	self.driver.find_element_by_name('Add to playlist').click()
	self.driver.find_element_by_name('Create New Playlist').click()
	self.driver.find_element_by_id(loc.more_playlist_input_text).clear()
	self.driver.find_element_by_id(loc.more_playlist_input_text).send_keys(playlist_name)
	self.driver.find_element_by_id(loc.more_playlist_save).click()


def search_track(self):
	button = self.driver.find_element_by_name('Search track')
	button.click()


def search_album(self):
	button = self.driver.find_element_by_name('Search album')
	button.click()


def search_artist(self):
	button = self.driver.find_element_by_name('Search artist')
	button.click()


def share_track(self):
	button = self.driver.find_element_by_name('Share track')
	button.click()


def share_playlist(self):
	button = self.driver.find_element_by_name('Share playlist')
	button.click()
