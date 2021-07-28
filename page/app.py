# coding=utf-8
"""
@project_name:  android-cts-verifier
@file:          app.PY
@Author:        nong
@Time:          2021/7/28 11:40

"""
from appium import webdriver

from base.base_page import BasePage
from page.main_page import MainPage


class App(BasePage):

    # 复用driver 判断driver是否为None
    def start_android_driver(self):
        capabilities = {
            "platformName": "Android",
            # "automationName": "UiAutomator2",
            "deviceName": "DVKS232D20110300016",
            "appPackage": "com.android.cts.verifier",
            "appActivity": "com.android.cts.verifier.CtsVerifierActivity",
            "noReset": "True"
        }
        if self.driver is None:
            self.driver = webdriver.Remote(f"127.0.0.1:4723/wd/hub", capabilities)
            self.driver.implicitly_wait(6)
        else:
            self.driver.launch_app()
        return self

    def restart_android_driver(self):
        """
        # 重启
        :return:
        """
        self.driver.close()
        self.driver.launch_app()

    def stop_android_driver(self):
        self.driver.quit()

    def start_ios_driver(self):
        pass

    def goto_main_page(self):
        return MainPage(self.driver)

    def page_source(self):
        return self.driver.page_source

    def implicitly_wait(self, time):
        return self.driver.implicitly_wait(time)