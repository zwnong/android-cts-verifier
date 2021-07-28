# coding = utf-8
import time
from appium import webdriver
from utils.write_user_command import WriteUserCommand


class Driver:
    def __init__(self):
        self.write_file = WriteUserCommand()

    def android_driver(self):
        capabilities = {
            "platformName": "Android",
            # "automationName": "UiAutomator2",
            "deviceName": "DVKS232D20110300016",
            "appPackage": "com.android.cts.verifier",
            "appActivity": "com.android.cts.verifier.CtsVerifierActivity",
            "noReset": "True"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        time.sleep(10)

    def quit_driver(self, i):
        self.android_driver()

    def ios_driver(self):
        pass

    # 如果设备是android 就getandroi_driver 如果是ios ...
    def get_driver(self):
        pass
