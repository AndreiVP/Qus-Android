import libs.locators as loc
import libs.helpers as h
import time


def check_welcome(self):
	counter = 0
	found = False
	while found == False:
		try:
			self.driver.find_element_by_id(loc.welcome_title)
			self.driver.find_element_by_id(loc.welcome_sign_up)
			self.driver.find_element_by_id(loc.welcome_sign_in)
			found = True
		except:
			counter += 1
			time.sleep(1)
		if counter == 30:
			break
	if found == False:
		raise Exception('Welcome view is not displayed')
	if found == True:
		self.driver.find_element_by_id(loc.welcome_sign_up).click()


def check_tour(self):
	counter = 0
	found = False
	while found == False:
		try:
			self.driver.find_element_by_id(loc.tour_title)
			found = True
		except:
			counter += 1
			time.sleep(1)
		if counter == 5:
			break
	if found == False:
		raise Exception('Tour view not displayed')
	if found == True:
		self.driver.find_element_by_id(loc.tour_next).click()


def check_sign_up(self):
	counter = 0
	found = False
	while found == False:
		try:
			self.driver.find_element_by_id(loc.register_title)
			found = True
		except:
			counter += 1
			time.sleep(1)
		if counter == 5:
			break
	if found == False:
		raise Exception('Signup view not displayed')
	if found == True:
		self.driver.find_element_by_id(loc.register_sign_in).click()


def open_sign_up(self):
	found = False
	elems = self.driver.find_elements_by_class_name(loc.welcome_view)
	for elem in elems:
		if elem.find_element_by_id(loc.welcome_title).text == 'Welcome to Q.us':
			# elem.click()
			elem.find_element_by_id(loc.welcome_sign_up).click()
			found == True
			break


def open_sign_in(self):
	found = False
	elems = self.driver.find_elements_by_class_name(loc.welcome_view)
	for elem in elems:
		if elem.find_element_by_id(loc.welcome_title).text == 'Welcome to Q.us':
			# elem.click()
			elem.find_element_by_id(loc.welcome_sign_in).click()
			found == True
			break


def registration(self, registration_details):
	if h.is_visible(self, loc.register_title, 60):
		self.driver.find_element_by_id(loc.register_nickname).clear()
		self.driver.find_element_by_id(loc.register_nickname).send_keys(registration_details['nickname'])
		h.hide_keys(self)
		self.driver.find_element_by_id(loc.register_email).clear()
		self.driver.find_element_by_id(loc.register_email).send_keys(registration_details['email'])
		h.hide_keys(self)
		self.driver.find_element_by_id(loc.register_pswrd).clear()
		self.driver.find_element_by_id(loc.register_pswrd).send_keys(registration_details['password'])
		h.hide_keys(self)
		self.driver.find_element_by_id(loc.register_checkbox).click()


def wait_for_registration(self):
	counter = 0
	found = False
	while found == False:
		try:
			self.driver.find_element_by_id(loc.sign_in_title)
			found = True
		except:
			counter += 1
			time.sleep(1)
		if counter == 30:
			break
	if found == False:
		raise Exception("Account wasn't created")
