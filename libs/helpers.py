import libs.locators as loc
import libs.More_options_menu.track_playlist_menu as mo
import platform
import time
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.touch_actions import TouchActions


def is_not_visible(self, locator, timeout=60):
    try:
        ui.WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located((By.ID, locator)))
        return True
    except TimeoutException:
        return False


def is_visible(self, locator, timeout=60):
    try:
        ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.ID, locator)))
        return True
    except TimeoutException:
        return False


def take_screenshot(self, name):
    if platform.system() == 'Windows':
        reports_path = 'test-reports/'
    else:
        reports_path = '/Users/svuser/.jenkins/jobs/Android_tests/workspace/'
    self.driver.save_screenshot(reports_path + name + '.png')


def find_and_click_element(self, element_id, parent=None):
    touch = TouchActions(self.driver)
    if parent is None:
        element = self.driver.find_element_by_id(element_id)
    else:
        element = parent.find_element_by_id(element_id)
    touch.tap(element).perform()


def get_page_title(self):
    title_text = self.driver.find_elements_by_class_name(loc.view_title)
    title_text = title_text[0]
    return title_text.text


def expand_music_section(self, index):
    touch = TouchActions(self.driver)
    dropdowns_list = self.driver.find_elements_by_id(loc.dropdown_button)
    dropdown_sections = dropdowns_list[index]
    touch.tap(dropdown_sections).perform()


def tap_add_button(self, index):
    touch = TouchActions(self.driver)
    add_buttons_list = self.driver.find_elements_by_id(loc.add_button)
    add_button = add_buttons_list[index]
    touch.tap(add_button).perform()


def open_queue(self):
    self.driver.find_element_by_id(loc.mini_player_track_details).click()
    # current_title = get_page_title(self)
    # self.assertEqual(current_title, 'Now Playing')


def wait_for_search(self):
    spinner = self.driver.find_elements_by_id(loc.search_loading_spinner)
    while len(spinner) > 0:
        try:
            self.driver.find_element_by_id(loc.search_loading_spinner)
        except:
            time.sleep(1)
        if self.driver.find_element_by_id(loc.search_loading_spinner) == 0:
            break


def hide_keys(self):
    try:
        self.driver.hide_keyboard()
    except:
        pass
