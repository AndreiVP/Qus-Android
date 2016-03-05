import libs.locators as loc


def perform_search(self, search_text):
        search_btn = self.driver.find_element_by_id(loc.search_magn_glass)
        search_btn.click()
        search_text_box = self.driver.find_element_by_id(loc.search_input_text)
        search_text_box.send_keys(str(search_text))
        self.driver.keyevent(66)       # KEYCODE_EVENT = 84 - code for Done key of android keyboard



