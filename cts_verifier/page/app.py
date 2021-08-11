#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: appo.py
@time: 2021/3/4 0:49
"""
import numbers
import os
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from appium.webdriver.webdriver import WebDriver

from base.base_driver import BaseDriver
from cts_verifier.page.main_page import MainPage
from utils.get_file import GetFile
from base.base_page import BasePage

file_path = fr'{os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + ".")}\datas\user_config.yaml'
data = GetFile(file_path=file_path)


class App(BasePage):
    def start_cts_driver(self):
        """
        启动主测试apk cts_verifier
        :return:
        """
        cts_device = data.get_value('user_info_0')['deviceName']
        cts_port = data.get_value('user_info_0')['port']
        self.cts_driver = BaseDriver().android_driver(
            str(cts_device),
            "com.android.cts.verifier",
            "com.android.cts.verifier.CtsVerifierActivity",
            cts_port
        )
        return self

    def start_android_settings_driver(self):
        """
        # 启动 settings apk
        :return:
        """
        settings_driver = data.get_value('user_info_1')['deviceName']
        settings_port = data.get_value('user_info_1')['port']
        self.settings_driver = BaseDriver().android_driver(
            str(settings_driver),
            "com.android.settings",
            "com.android.settings.Settings",
            settings_port,
            5000
        )

    def goto_cts_main_page(self):
        return MainPage(self.cts_driver)

    def goto_settings_main_page(self):
        return MainPage(self.settings_driver)

    def stop_cts_driver(self):
        self.cts_driver.quit()

    def stop_setting_driver(self):
        self.settings_driver.quit()

    def implicitly_wait(self, time):
        return self.cts_driver.implicitly_wait(time)

    def click_back(self):
        self.cts_driver.keyevent(4)

    def click_home(self):
        self.cts_driver.keyevent(3)

    def cts_page_source(self):
        return self.cts_driver.page_source

    def find_elements(self, element):
        msg = self.cts_driver.find_elements(By.XPATH, element)
        return msg

    def camera_performance_page_opinion(self, time):
        """
        camera_performance页面用例运行等待完成后的处理
        :return:
        """
        for i in range(100):
            sleep(time)
            n = len(self.find_elements(
                '//*[@resource-id="android:id/message" and @text="Running CTS performance test case..."]'))
            if n == 0 and 'testSingleCapture' in self.cts_page_source():
                break
            else:
                self.click_back()
        self.click_back()

    def tap_screen(self, x, y):
        self.cts_driver.tap([(x, y)], 5)

    def cts_driver_restart(self):
        self.cts_driver.launch_app()

    def isElement(self, locator, ele):
        """
        Determine whether elements exist
        Usage:
        isElement(By.XPATH,"//a")
        """
        sleep(1)
        flag = None
        try:
            if locator == "id":
                # self.driver.implicitly_wait(60)
                self.cts_driver.find_element_by_id(ele)
            elif locator == "xpath":
                # self.driver.implicitly_wait(60)
                self.cts_driver.find_element_by_xpath(ele)
            elif locator == "class":
                self.cts_driver.find_element_by_class_name(ele)
            elif locator == "link text":
                self.cts_driver.find_element_by_link_text(ele)
            elif locator == "partial link text":
                self.cts_driver.find_element_by_partial_link_text(ele)
            elif locator == "name":
                self.cts_driver.find_element_by_name(ele)
            elif locator == "tag name":
                self.cts_driver.find_element_by_tag_name(ele)
            elif locator == "css selector":
                self.cts_driver.find_element_by_css_selector(ele)
            flag = True
        except NoSuchElementException as e:
            flag = False
        finally:
            return flag
