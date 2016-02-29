from libs import locators as loc
import time
from libs import helpers as h


def perform_search(self, search_text):
        search_btn = self.driver.find_element_by_id(loc.search_magn_glass)
        search_btn.click()
        search_text_box = self.driver.find_element_by_id(loc.search_input_text)
        search_text_box.send_keys(str(search_text))
        self.driver.keyevent(84)       # KEYCODE_EVENT = 84 - code for search key of android keyboard


#def wait_for_the_search(self):
