import libs.locators as loc
import libs.helpers as h
import libs.signInQus as sIn
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
			self.driver.find_element_by_id(loc.sign_up_title)
			found = True
		except:
			counter += 1
			time.sleep(1)
		if counter == 5:
			break
	if found == False:
		raise Exception('Signup view not displayed')
	if found == True:
		self.driver.find_element_by_id(loc.sign_up_sign_in).click()


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
	self.driver.find_element_by_id(loc.welcome_sign_up).click()
	self.driver.find_element_by_id(loc.tour_next).click()
	if h.is_visible_by_id(self, loc.sign_up_title, 60):
		#self.driver.find_element_by_id(loc.sign_up_nickname).clear()
		self.driver.find_element_by_id(loc.sign_up_nickname).send_keys(registration_details['nickname'])
		h.hide_keys(self)
		#self.driver.find_element_by_id(loc.sign_up_email).clear()
		self.driver.find_element_by_id(loc.sign_up_email).send_keys(registration_details['email'])
		h.hide_keys(self)
		#self.driver.find_element_by_id(loc.sign_up_password).clear()
		self.driver.find_element_by_id(loc.sign_up_password).send_keys(registration_details['password'])
		h.hide_keys(self)
		self.driver.find_element_by_id(loc.sign_up_checkbox).click()
		self.driver.find_element_by_id(loc.sign_up_submit).click()




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


def signin_after_signup (self, registration_details):
	self.driver.find_element_by_id(loc.sign_in_password).clear()
	self.driver.find_element_by_id(loc.sign_in_password).send_keys(registration_details['password'])
	h.hide_keys(self)
	self.driver.find_element_by_id(loc.sign_in_submit).click()
	sIn.wait_for_sign_in(self)


def check_validation_message(self, expected_validation_nickname, expected_validation_email, expected_validation_password):
	if self.driver.find_elements_by_id(loc.sign_up_invalid_nickname):
		validation_message = self.driver.find_element_by_id(loc.sign_up_invalid_nickname).text
		self.assertEqual(validation_message, expected_validation_nickname, "Validation message is not the expected one")
	if self.driver.find_elements_by_id(loc.sign_up_invalid_email):
		validation_message = self.driver.find_element_by_id(loc.sign_up_invalid_email).text
		self.assertEqual(validation_message, expected_validation_email, "Validation message is not the expected one")
	if self.driver.find_elements_by_id(loc.sign_up_invalid_password):
		validation_message = self.driver.find_element_by_id(loc.sign_up_invalid_password).text
		self.assertEqual(validation_message, expected_validation_password, "Validation message is not the expected one")


def return_to_sign_up(self):
	self.driver.find_element_by_id(loc.sign_up_sign_in).click()
	self.driver.find_element_by_id(loc.sign_in_sign_up).click()
