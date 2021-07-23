import time

from appium import webdriver
from selenium.webdriver.common.by import By


class TestDemo:
    def setup(self):
        capabilities = {
            "platformName": "Android",
            # "automationName": "UiAutomator2",
            "deviceName": "DVKS232D20110300016",
            "appPackage": "com.android.cts.verifier",
            "appActivity": "com.android.cts.verifier.CtsVerifierActivity",
            "noReset": "True"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        time.sleep(5)

    def teardown(self):
        pass

    def test_demo(self):
        self.driver.find_element(By.XPATH,
                                 "//*[@resource-id='android:id/text1' and @text='Audio Frequency Line Test']").click()
