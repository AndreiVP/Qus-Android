import libs.locators as loc
import time, platform, os
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.touch_actions import TouchActions

adb_path = "D:\Programs\Android-SDK\platform-tools/adb.exe"


def is_visible_by_id(self, locator, timeout=60):
	try:
		ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.ID, locator)))
		return True
	except TimeoutException:
		return False


def is_visible_by_class(self, locator, timeout=60):
	try:
		ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, locator)))
		return True
	except TimeoutException:
		return False


def is_not_visible_by_id(self, locator, timeout=60):
	try:
		ui.WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located((By.ID, locator)))
		return True
	except TimeoutException:
		return False


def is_not_visible_by_class(self, locator, timeout=60):
	try:
		ui.WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located((By.CLASS_NAME, locator)))
		return True
	except TimeoutException:
		return False


def find_and_click_element(self, element_id, parent=None):
	touch = TouchActions(self.driver)
	if parent is None:
		element = self.driver.find_element_by_id(element_id)
	else:
		element = parent.find_element_by_id(element_id)
	touch.tap(element).perform()


def find_and_clear_field(self, element_id):
	self.driver.find_element_by_id(element_id).click()
	self.driver.find_element_by_id(element_id).send_keys('')


# touch = TouchActions(self.driver)
# if parent is None:
# 	element = self.driver.find_element_by_id(element_id)
# else:
# 	element = parent.find_element_by_id(element_id)
# touch.long_press(element).perform()
# self.driver.keyevent(67) # KEYCODE_EVENT = 66 - code for Delete key of android keyboard


def get_page_title(self):
	title_text = self.driver.find_elements_by_class_name(loc.view_title)
	title_text = title_text[0]
	return title_text.text


def tap_back_button(self):
	self.driver.find_element_by_class_name('android.widget.ImageButton').click()


def expand_music_section(self, index):
	touch = TouchActions(self.driver)
	dropdowns_list = self.driver.find_elements_by_id(loc.dropdown_button)
	dropdown_sections = dropdowns_list[index]
	touch.tap(dropdown_sections).perform()


def tap_add_button(self, index):
	touch = TouchActions(self.driver)
	add_buttons_list = self.driver.find_elements_by_id(loc.search_add_button)
	add_button = add_buttons_list[index]
	touch.tap(add_button).perform()


def open_queue(self):
	self.driver.find_element_by_id(loc.mini_player_track_details).click()


# current_title = get_page_title(self)
# self.assertEqual(current_title, 'Now Playing')


def wait_for_search(self):
	while is_visible_by_id(self, loc.search_loading_spinner, 60):
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


def input_text_to_element(self, input_id, text):
	location = self.driver.find_element_by_id(input_id)
	location.clear()
	location.send_keys(str(text))
	self.driver.keyevent(66)  # KEYCODE_EVENT = 84 - code for search key of android keyboard


def perform_search(self, input_id, search_text):
	location = self.driver.find_element_by_id(input_id)
	location.clear()
	location.send_keys(str(search_text))
	self.driver.keyevent(84)  # KEYCODE_EVENT = 84 - code for search key of android keyboard


def sign_out(self):
	self.driver.find_element_by_class_name('android.widget.ImageButton').click()
	find_and_click_element(self, loc.drawer_sign_out_button)
	is_visible_by_id(self, loc.sign_in_title, 10)


def check_no_items(self):
	message = self.driver.find_element_by_id(loc.listen_with_no_items)
	message_text = message.text
	self.assertEqual(message_text, 'No items to display')


def screenshot_when_exception(self):
	self.driver.save_screenshot(self.id() + "/ERROR.png")


def take_screenshot(self, name):
	reports_path = 'test-reports/'
	self.driver.save_screenshot(reports_path + name + 'ERROR.png')
