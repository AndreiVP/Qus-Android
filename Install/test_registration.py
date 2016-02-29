import libs.registrationQus as reg
import libs.locators as loc
import unittest
import time
from time import strftime
from config.config import setup, set_up_test, tear_down_test, teardown

unic = strftime("%a%d%b%Y")
# unic = strftime("%a%d%b%Y%H%M")
email = 'auto{}'.format(unic)

registration_details = {'nickname': '{}'.format(email),
                        'email': '{}@mailinator.com'.format(email),
                        'password': '111111'
                        }

registration_empty_details = {'nickname': '',
                              'email': '',
                              'password': ''
                              }

registration_invalid_email_format = {'nickname': '{}'.format(email),
                                     'email': 'apopamailinator.com',
                                     'password': '111111'
                                     }

registration_duplicate_email = {'nickname': '{}'.format(email),
                                'email': 'apopa@mailinator.com',
                                'password': '111111'
                                }

registration_invalid_password = {'nickname': '{}'.format(email),
                                 'email': '{}@mailinator.com'.format(email),
                                 'password': '12345'
                                 }


class RegistrationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        setup(cls)

    @classmethod
    def tearDownClass(cls):
        teardown(cls)

    def setUp(self):
        set_up_test(self)

    def tearDown(self):
        tear_down_test(self)

    def test_01_register_empty_details(self):
        reg.registration(self, registration_empty_details)
        self.driver.find_element_by_id(loc.register_invalid_nickname)
        self.driver.find_element_by_id(loc.register_invalid_email)
        self.driver.find_element_by_id(loc.register_invalid_pswrd)

    def test_02_register_invalid_email_format(self):
        reg.registration(self, registration_invalid_email_format)
        self.driver.find_element_by_id(loc.register_invalid_email)

    def test_03_register_duplicate_email(self):
        reg.registration(self, registration_duplicate_email)
        self.driver.find_element_by_id(loc.register_invalid_email)

    def test_04_register_invalid_pswrd(self):
        reg.registration(self, registration_invalid_password)
        self.driver.find_element_by_id(loc.register_invalid_pswrd)

    def test_05_register_valid_data(self):
        reg.registration(self, registration_details)
        reg.wait_for_registration(self)


if __name__ == '__main__':
    unittest.main()
