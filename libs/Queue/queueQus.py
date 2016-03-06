import libs.locators as loc


def open_queue_more_menu(self):
    more_menu_btns_list = self.driver.find_elements_by_id(loc.queue_more_options_menu)
    queue_more_menu = more_menu_btns_list[0]
    queue_more_menu.click()


def open_track_more_menu(self, index):
    tracks_list = self.driver.find_elements_by_id(loc.queue_more_options_menu)
    selected_track = tracks_list[index]
    selected_track.click()