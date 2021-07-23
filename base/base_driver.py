# coding = utf-8
import time
from appium import webdriver
from utils.write_user_command import WriteUserCommand


class Driver:
    def __init__(self):
        self.write_file = WriteUserCommand()

    def android_driver(self):
        # 从\config\user_config.yml中读取设备信息
        devices = self.write_file.get_yaml_value('user_info_' + str(0), 'deviceName')
        # 从\config\user_config.yml中读取端口号
        port = self.write_file.get_yaml_value('user_info_' + str(0), 'port')
        capabilities = {
            "platformName": "Android",
            # "automationName": "UiAutomator2",
            "deviceName": devices,
            "appPackage": "com.android.cts.verifier",
            "appActivity": "com.android.cts.verifier.CtsVerifierActivity",
            "noReset": "True"
        }
        driver = webdriver.Remote("http://127.0.0.1:"+port+"/wd/hub", capabilities)
        time.sleep(5)
        return driver

    def quit_driver(self, i):
        self.android_driver().quit()

    def ios_driver(self):
        pass

    # 如果设备是android 就getandroi_driver 如果是ios ...
    def get_driver(self):
        pass
