from appium import webdriver
import libs.locators as loc
import os, platform, time
import selenium.webdriver.support.ui as ui
import selenium.common.exceptions as ex
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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

def hide_keys(self):
    try:
        self.driver.hide_keyboard()
    except:
        pass