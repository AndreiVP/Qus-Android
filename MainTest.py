import unittest
import SignIn.test_signIn
import user_tests.test_demo
import SignUp.test_signUp

if __name__ == '__main__':
    #test_classes_to_run = [user_tests.test_demo.DemoTest]
    test_classes_to_run = [SignIn.test_signIn.signInTest]
    # test_classes_to_run = [SignUp.test_signUp.SignUpTest]
    #test_classes_to_run = [SignUp.test_signUp.SignUpTest, SignIn.test_signIn.signInTest,user_tests.test_demo.DemoTest]
    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)
