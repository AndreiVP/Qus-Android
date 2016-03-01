import libs.locators as loc
import platform
import time
from appium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions


def take_screenshot(self,name):
    if platform.system() == 'Windows':
        reports_path = 'test-reports/'
    else:
        reports_path = '/Users/svuser/.jenkins/jobs/Android_tests/workspace/'
    self.driver.save_screenshot(reports_path+name+'.png')


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


def wait_for_search(self):
    search_ended = 0
    while search_ended == 0:
            try:
                self.driver.find_elements_by_id(loc.search_loading_spinner)
                search_ended = 0
            except:
                time.sleep(1)
            if self.driver.find_elements_by_id(loc.search_loading_spinner) == 0:
                break


def hide_keys(self):
    try:
        self.driver.hide_keyboard()
    except:
        pass