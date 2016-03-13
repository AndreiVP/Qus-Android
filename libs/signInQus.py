import libs.helpers as h
import libs.locators as loc
import time


def signIn(self, login_details):
	if h.is_visible(self, loc.sign_in_submit, 60):
		self.driver.find_element_by_id(loc.sign_in_email).clear()
		self.driver.find_element_by_id(loc.sign_in_email).send_keys(login_details['username'])
		h.hide_keys(self)
		self.driver.find_element_by_id(loc.sign_in_password).clear()
		self.driver.find_element_by_id(loc.sign_in_password).send_keys(login_details['password'])
		h.hide_keys(self)
		self.driver.find_element_by_id(loc.sign_in_submit).click()


def signIn_valid(self, username, password):
	if h.is_visible(self, loc.sign_in_submit, 60):
		self.driver.find_element_by_id(loc.sign_in_email).clear()
		self.driver.find_element_by_id(loc.sign_in_email).send_keys(username)
		h.hide_keys(self)
		self.driver.find_element_by_id(loc.sign_in_password).clear()
		self.driver.find_element_by_id(loc.sign_in_password).send_keys(password)
		h.hide_keys(self)
		self.driver.find_element_by_id(loc.sign_in_submit).click()
		wait_for_sign_in(self)



def wait_for_sign_in(self):
	page_loaded = 0
	counter = 0
	while page_loaded == 0:
		try:
			current_title = h.get_page_title(self)
			self.assertEqual(current_title, 'SEARCH')
			page_loaded = 1
		except:
			time.sleep(1)
		counter += 1
		if counter == 60:
			self.assertTrue(False, "SignIn wasn't successful in 60 sec.")