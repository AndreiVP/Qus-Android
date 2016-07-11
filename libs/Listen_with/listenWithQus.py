import libs.helpers as h
import libs.locators as loc
import libs.Drawer_menu.navigationQus as nav
import time


def search_user(self, user):
	self.driver.find_element_by_id(loc.search_button).click()
	rec_title = self.driver.find_element_by_id(loc.lw_recommended)
	rec_title_text = rec_title.text
	self.assertEqual(rec_title_text, 'RECOMMENDED USERS')
	h.input_text_to_element(self, loc.search_input_text, user)


# def wait_for_search(self):
# 	spinner = self.driver.find_element_by_class_name('android.widget.ProgressBar')
# 	while h.is_not_visible_by_id(self, spinner, 60):
# 		try:
# 			self.self.driver.find_element_by_class_name('android.widget.ProgressBar') == 0
# 		except:
# 			time.sleep(1)
# 		if self.driver.find_element_by_class_name('android.widget.ProgressBar'):
# 			break

def wait_for_search(self):
	h.is_visible_by_id(self, loc.lw_follow_card)


def open_user_card(self, index):
	users_list = self.driver.find_elements_by_id(loc.lw_follow_card)
	detail_section = users_list[index]
	detail_section.click()


# def open_user_details_list(self, index):
# 	user_details_list = self.driver.find_element_by_class_name('android.widget.RelativeLayout')
# 	#user_details_list = self.driver.find_elements_by_id(loc.lw_options_list)
# 	detail_section = user_details_list[index]
# 	detail_section.click()

def open_user_section(self, section):
	user_section = self.driver.find_element_by_name(section)
	user_section.click()


def follow_user_lw(self):
	follow_button_state = self.driver.find_element_by_id(loc.lw_follow_button).text
	self.assertEqual(follow_button_state, 'FOLLOW')
	h.find_and_click_element(self, loc.lw_follow_button)
	# time.sleep(5)
	# follow_button_state = self.driver.find_element_by_id(loc.lw_profile_follow).text
	# self.assertEqual(follow_button_state, 'STOP FOLLOWING')


def stop_following_user_lw(self):
	h.find_and_click_element(self, loc.lw_follow_button)
	follow_button_state = self.driver.find_element_by_id(loc.lw_profile_follow).text
	self.assertEqual(follow_button_state, 'STOP FOLLOWING')
	h.find_and_click_element(self, loc.lw_follow_button)
	time.sleep(5)
	follow_button_state = self.driver.find_element_by_id(loc.lw_profile_follow).text
	self.assertEqual(follow_button_state, 'FOLLOW')


def follow_user_up(self):
	follow_button_state = self.driver.find_element_by_id(loc.lw_profile_follow).text
	self.assertEqual(follow_button_state, 'FOLLOW')
	# h.find_and_click_element(self, loc.lw_profile_follow)
	self.driver.find_element_by_id(loc.lw_profile_follow).click()
	time.sleep(5)
	follow_button_state = self.driver.find_element_by_id(loc.lw_profile_follow).text
	self.assertEqual(follow_button_state, 'STOP FOLLOWING')
	self.driver.find_element_by_class_name('android.widget.ImageButton').click()
	self.driver.find_elements_by_id(loc.lw_options_list)[0].click()
	# follow_button_state = self.driver.find_element_by_id(loc.lw_profile_follow).text
	self.assertNotEqual(follow_button_state, 'FOLLOW')


def stop_following_user_up(self):
	follow_button_state = self.driver.find_element_by_id(loc.lw_profile_follow).text
	self.assertEqual(follow_button_state, 'STOP FOLLOWING')
	# h.find_and_click_element(self, loc.lw_profile_follow)
	self.driver.find_element_by_id(loc.lw_profile_follow).click()
	time.sleep(5)
	follow_button_state = self.driver.find_element_by_id(loc.lw_profile_follow).text
	self.assertEqual(follow_button_state, 'FOLLOW')
	self.driver.find_element_by_class_name('android.widget.ImageButton').click()
	self.driver.find_elements_by_id(loc.lw_options_list)[0].click()
	# follow_button_state = self.driver.find_element_by_id(loc.lw_profile_follow).text
	self.assertNotEqual(follow_button_state, 'STOP FOLLOWING')


def get_nickname_usercard(self, nickname):
	nickname_text = self.driver.find_element_by_id(loc.lw_follow_card)
	nicknametxt = nickname_text.text
	self.assertEqual(nicknametxt, nickname)


