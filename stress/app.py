#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: appo.py
@time: 2021/3/4 0:49
"""
import os
from time import sleep

from stress.main_page import MainPage
from utils.sever import Server
from selenium.common.exceptions import NoSuchElementException
from base.base_driver import BaseDriver
from utils.get_file import GetFile
from base.base_page import BasePage

file_path = fr'{os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + ".")}\cts_verifier\datas\user_config.yaml'
data = GetFile(file_path=file_path)
device_list = Server().get_device()


class App(BasePage):
    def start_driver(self, i, device):
        """
        启动主测试apk cts_verifier
        :param :device_name
        :param :int, user_config.yml对应的端口号位置
        :return:
        """
        port = data.get_value(f'user_info_{i}')['port']
        self.driver = BaseDriver().android_driver(
            str(device),
            "com.android.camera2",
            "com.android.camera.IdleSleepActivity",
            port
        )
        return self.driver

    def goto_main_page(self):
        return MainPage(self.driver)

    def stop_driver(self):
        self.driver.quit()

    def click_back(self):
        self.driver.keyevent(4)

    def click_home(self):
        self.driver.keyevent(3)

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
