from libs import locators as loc
import time
from libs import helpers as h
from libs import first_runQus as frun


def registration(self, registration_details):
    frun.check_welcome_Qus(self)
    frun.check_Tour(self)
    registration_view_title = self.driver.find_elements_by_id(loc.register_title)
    if len(registration_view_title) > 0:
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