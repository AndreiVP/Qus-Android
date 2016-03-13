import libs.signUpQus as sUp
import libs.helpers as h
import libs.locators as loc
import unittest
from time import strftime
from config.config import setup, set_up_test, tear_down_test, teardown

#unic = strftime("%a%d%b%Y")
unic = strftime("%a%d%b%Y%H%M")
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


class SignUpTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        setup(cls)

    @classmethod
    def tearDownClass(cls):
        teardown(cls)

    def setUp(self):
        set_up_test(self)
        sUp.check_welcome(self)
        sUp.check_tour(self)

    def tearDown(self):
        tear_down_test(self)

    def test_01_register_empty_details(self):
        sUp.registration(self, registration_empty_details)
        h.is_visible(self, loc.register_invalid_nickname)
        h.is_visible(self, loc.register_invalid_email)
        h.is_visible(self, loc.register_invalid_pswrd)

    def test_02_register_invalid_email_format(self):
        sUp.registration(self, registration_invalid_email_format)
        h.is_visible(self, loc.register_invalid_email)

    def test_03_register_duplicate_email(self):
        sUp.registration(self, registration_duplicate_email)
        h.is_visible(self, loc.register_invalid_email)

    def test_04_register_invalid_pswrd(self):
        sUp.registration(self, registration_invalid_password)
        h.is_visible(self, loc.register_invalid_pswrd)

    def test_05_register_valid_data(self):
        sUp.registration(self, registration_details)
        sUp.wait_for_registration(self)
        sUp.signin_after_signup(self,registration_details)
        h.sign_out(self)


if __name__ == '__main__':
    unittest.main()
