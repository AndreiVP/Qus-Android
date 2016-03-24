import libs.locators as loc


def navigate_to_queue(self):
    self.driver.find_element_by_class_name('android.widget.ImageButton').click()
    self.driver.find_elements_by_id(loc.drawer_section_button)[0].click()


def navigate_to_search(self):
    self.driver.find_element_by_class_name('android.widget.ImageButton').click()
    self.driver.find_elements_by_id(loc.drawer_section_button)[1].click()


def navigate_to_listen_with(self):
    self.driver.find_element_by_class_name('android.widget.ImageButton').click()
    self.driver.find_elements_by_id(loc.drawer_section_button)[2].click()


def navigate_to_playlists(self):
    self.driver.find_element_by_class_name('android.widget.ImageButton').click()
    self.driver.find_element_by_class_name('android.widget.ImageButton').click()
    self.driver.find_element_by_class_name('android.widget.ImageButton').click()
    self.driver.find_elements_by_id(loc.drawer_section_button)[3].click()