import libs.locators as loc


def open_playlist(self, index):
    playlists_list = self.driver.find_elements_by_id(loc.playlist_title)
    selected_playlist = playlists_list[index]
    selected_playlist.click()


def return_to_playlists_list(self):
    self.driver.find_element_by_class_name('android.widget.ImageButton').click()


def delete_playlist(self, index):
    edit_buttons_list = self.driver.find_elements_by_id(loc.playlist_edit_button)
    selected_playlist = edit_buttons_list[index]
    selected_playlist.click()
    self.driver.find_element_by_name('Delete').click()
    self.driver.find_element_by_id(loc.playlist_delete_ok).click()
    self.assertTrue(loc.playlist_no_items, 'No items to display')
