from libs import locators as loc
import time
from libs import helpers as h



def login(self, login_details):
    #self.driver.find_element_by_id(loc.welcome_sign_in).click()
    submit_btn = self.driver.find_elements_by_id(loc.sign_in_submit)
    if len(submit_btn) > 0:
        self.driver.find_element_by_id(loc.sign_in_email).clear()
        self.driver.find_element_by_id(loc.sign_in_email).send_keys(login_details['username'])
        h.hide_keys(self)
        self.driver.find_element_by_id(loc.sign_in_password).clear()
        self.driver.find_element_by_id(loc.sign_in_password).send_keys(login_details['passwd'])
        h.hide_keys(self)
        # find_and_click_button(self, 'SUBMIT')
        self.driver.find_element_by_id(loc.sign_in_submit).click()





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
            self.assertTrue(False, "Login wasn't successful in 60 sec.")


def check_login_button(self):
    counter=0
    found = False
    while found == False:
        try:
            self.driver.find_element_by_id(loc.sign_in_submit)
            found = True
        except:
            counter +=1
            time.sleep(1)
        if counter == 30:
            break
    if found == False:
        raise Exception('login button not available')

