import libs.locators as loc
import libs.helpers as h


def navigate_to_queue(self):
    self.driver.find_element_by_class_name('android.widget.ImageButton').click()
    self.driver.find_elements_by_id(loc.drawer_section_button)[0].click()
    title_text = self.driver.find_elements_by_class_name(loc.view_title)
    title_text = title_text[0].text
    self.assertEqual(title_text, 'Now Playing')


def navigate_to_search(self):
    self.driver.find_element_by_class_name('android.widget.ImageButton').click()
    self.driver.find_elements_by_id(loc.drawer_section_button)[1].click()
    title_text = self.driver.find_elements_by_class_name(loc.view_title)
    title_text = title_text[0].text
    self.assertEqual(title_text, 'SEARCH')


def navigate_to_listen_with(self):
    self.driver.find_element_by_class_name('android.widget.ImageButton').click()
    self.driver.find_elements_by_id(loc.drawer_section_button)[2].click()
    title_text = self.driver.find_elements_by_class_name(loc.view_title)
    title_text = title_text[0].text
    self.assertEqual(title_text, 'LISTEN WITH')


def navigate_to_playlists(self):
    self.driver.find_element_by_class_name('android.widget.ImageButton').click()
    self.driver.find_elements_by_id(loc.drawer_section_button)[3].click()
    title_text = self.driver.find_elements_by_class_name(loc.view_title)
    title_text = title_text[0].text
    self.assertEqual(title_text, 'Playlists')