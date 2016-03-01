import unittest
import Login.test_login
import user_tests.test_demo
import Registration.test_registration

if __name__ == '__main__':
    test_classes_to_run = [user_tests.test_demo.DemoTest]
    #test_classes_to_run = [Registration.test_registration.RegistrationTest]
    #test_classes_to_run = [Login.test_login.LoginTest]
    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)
