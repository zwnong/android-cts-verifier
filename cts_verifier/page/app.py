#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: appo.py
@time: 2021/3/4 0:49
"""
import os
import subprocess
from time import sleep

from utils.dos_cmd import DosCmd
from utils.sever import Server
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from cts_verifier.page.main_page import MainPage
from utils.get_file import GetFile
from base.base_page import BasePage

file_path = fr'{os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + ".")}\datas\user_config.yaml'
data = GetFile(file_path=file_path)
device_list = Server().get_device()


class App(BasePage):
    def start_device_0_driver(self):
        """
        启动主测试apk cts_verifier
        :return:
        """
        device = data.get_value('user_info_0')['deviceName']
        port = data.get_value('user_info_0')['port']
        self.driver = BaseDriver().android_driver(
            str(device),
            "com.android.cts.verifier",
            "com.android.cts.verifier.CtsVerifierActivity",
            port
        )
        return self.driver

    def start_any_driver(self, package, activity):
        """ 启动一个传入的apk"""
        device = data.get_value('user_info_0')['deviceName']
        port = data.get_value('user_info_0')['port']
        any_driver = BaseDriver().android_driver(
            str(device),
            package,
            activity,
            port
        )
        return any_driver

    def start_device_1_driver(self):
        """
        # 启动 另一个设备中的cts-verifiver.apk
        :return:
        """
        device = data.get_value('user_info_1')['deviceName']
        port = data.get_value('user_info_1')['port']
        start_device_1_driver = BaseDriver().android_driver(
            str(device),
            "com.android.cts.verifier",
            "com.android.cts.verifier.CtsVerifierActivity",
            port
        )
        return start_device_1_driver

    def goto_main_page(self):
        return MainPage(self.driver)

    def stop_driver(self):
        self.driver.quit()

    def click_back(self):
        self.driver.keyevent(4)

    def click_home(self):
        self.driver.keyevent(3)

    def device_0_page_source(self):
        return self.driver.page_source

    def find_elements(self, element):
        msg = self.driver.find_elements(By.XPATH, element)
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
            if n == 0 and 'testSingleCapture' in self.device_0_page_source():
                break
            else:
                self.click_back()
        self.click_back()

    def tap_screen(self, x, y):
        self.driver.tap([(x, y)], 5)

    def cts_driver_restart(self):
        self.driver.launch_app()

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
                self.driver.find_element_by_id(ele)
            elif locator == "xpath":
                # self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath(ele)
            elif locator == "class":
                self.driver.find_element_by_class_name(ele)
            elif locator == "link text":
                self.driver.find_element_by_link_text(ele)
            elif locator == "partial link text":
                self.driver.find_element_by_partial_link_text(ele)
            elif locator == "name":
                self.driver.find_element_by_name(ele)
            elif locator == "tag name":
                self.driver.find_element_by_tag_name(ele)
            elif locator == "css selector":
                self.driver.find_element_by_css_selector(ele)
            flag = True
        except NoSuchElementException as e:
            flag = False
        finally:
            return flag
