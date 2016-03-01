import subprocess
from appium import webdriver
import os, platform, time
import libs.helpers as h

loginDetails = {
                'username': 'apopatest@mailinator.com',
                'passwd': '111111',
                }

desired_caps = {'platformName': 'Android',
                # 'platformVersion': '5.1',
                # 'deviceName': 'CB5A260E1P',  # Z1 Compact,
                'platformVersion': '5.0',
                'deviceName': 'gt_i9505_b802fb37', #Galaxy S4
                # 'platformVersion': '4.4',
                # 'deviceName': 'TA4310FINM', #Xiaomi
                'noReset': 'true',
                'MobileCapabilityType.TAKES_SCREENSHOT': 'true'

                }


def set_up_test(self, res='r'):
    desired_caps['appWaitActivity'] = 'com.budtobud.qus.activities.WelcomeActivity'
    #desired_caps['appWaitActivity'] = 'com.budtobud.qus.activities.LoginActivity'
    if platform.system() == 'Windows':
        desired_caps['app'] = 'D:/Automation/Q.us_com.budtobud.qus.development.apk'
    else:
        print('App not installed')
    if res == 'r':
        desired_caps['noReset'] = 'false'
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def setup_login_test(self, res='r'):
    desired_caps['appWaitActivity'] = 'com.budtobud.qus.activities.LoginActivity'
    if platform.system() == 'Windows':
        desired_caps['app'] = 'D:/Automation/Q.us_com.budtobud.qus.development.apk'
    else:
        print('Error login')
    if res == 'r':
        desired_caps['noReset'] = 'true'
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

def setup_inapp_test(self, res='r'):
    desired_caps['appWaitActivity'] = 'com.budtobud.qus.activities.ToolbarActivity'
    if platform.system() == 'Windows':
        desired_caps['app'] = 'D:/Automation/Q.us_com.budtobud.qus.development.apk'
    else:
        print('Error login')
    if res == 'r':
        desired_caps['noReset'] = 'true'
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def setup(self):
    # Start appium server
    #if platform.system() == 'Windows':
    #    appium_start = ["D:/Automation/Appium/node", "D:/Automation/Appium/node_modules/appium/bin/appium.js",
    #                    "--log-level",
    #                    "error"]
    if platform.system() == 'Windows':
        appium_start = ["D:/Automation/Appium/node.exe", "D:/Automation\Appium/node_modules/appium/bin/appium.js",
                        "--log-level",
                        "error"]
    else:
        print('Appium srvr error')
    if platform.system() == 'Windows':
        os.system('taskkill /f /im node.exe')
    else:
        os.system('pkill -9 node')
    subprocess.Popen(appium_start)
    time.sleep(4)
    print('appium started')


def tear_down_test(self):
    h.take_screenshot(self, self.id())
    self.driver.quit()


def teardown(self):
    # kill appium server
    if platform.system() == 'Windows':
        os.system('taskkill /f /im node.exe')
    else:
        os.system('pkill -9 node')

