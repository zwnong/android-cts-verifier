#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: base_page.py
@time: 2021/3/9 21:52
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from decorator.handle_black_list import handle_black
from utils.get_file import GetFile
from utils.logger import log
import os
import subprocess
import time
import yaml


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @handle_black
    def find(self, locator, element):
        """
        重构查找元素
        :param locator: 定位方式
        :param element: 元素信息
        :return:
        """
        log.debug('find' + element)
        return WebDriverWait(self.driver, 5).until(lambda x: x.find_element(locator, element))
        # return self.driver.find_element(locator, element)

    def find_and_click(self, locator, element):
        """
        重构查找元素并点击
        :param locator: 定位方式
        :param element: 元素信息
        :return:
        """
        self.find(locator, element).click()

    def find_and_sendkeys(self, locator, element, value):
        return self.find(locator, element).send_keys(value)

    def finds(self, locator, value):
        return self.driver.find_elements(locator, value)

    def web_driver_wait(self, locator, value):
        return WebDriverWait(self.driver, 10, 0.1).until(lambda x: x.find_element(locator, value))

    # 获取屏幕分辨率
    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向左滑动
    def swipe_left(self, duration=None):
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x, y1, duration)

    # 想右滑动
    def swipe_reight(self, duration=None):
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 9
        self.driver.swipe(x1, y1, x, y1, duration)

    # 向上滑动
    def swipe_up(self, duration=None):
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 9
        y = self.get_size()[1] / 10
        self.driver.swipe(x1, y1, x1, y, duration)

    # 想下滑动
    def swipe_down(self, duration=None):
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1] / 10 * 9
        self.driver.swipe(x1, y1, x1, y, duration)

    # 指定方向滑动
    def swip_on(self, direction):
        if direction == 'up':
            self.swipe_up()
        elif direction == 'down':
            self.swipe_down()
        elif direction == 'left':
            self.swipe_down()
        else:
            self.swipe_reight()

    def swipe_find(self, locator, element, num=3):
        """
        # 上下滑动查找元素
        :param element:
        :param locator:
        :param num: 滑动页数，默认为3页
        :param num:
        :return:
        """
        for i in range(num):
            # if i == num - 1:
            #     raise NoSuchElementException(f'滑动{num}次，没找到元素')
            try:
                return self.parse(locator, element)
            except Exception:
                self.swipe_up()
                return self.parse(locator, element)

    def parse(self, yaml_path, fun_name):
        """
        # 解析关键字 解析yaml文件并调用相应的方法 实现相应功能
        :param yaml_path: yaml文件路径
        :param fun_name: yaml文件定义的方法名
        :return:
        """
        with open(yaml_path, 'r+', encoding='utf-8') as f:
            functance = yaml.load(f)
        steps = functance.get(fun_name)
        for step in steps:
            if step.get('action') == 'find_and_click':
                self.find_and_click(step.get('locator'), step.get('element'))
            elif step.get('action') == 'find_and_sendkeys':
                self.find_and_sendkeys(step.get('locator'), step.get('element'), step.get('contents'))

    def screenshot(self):
        """
        截图
        :return:
        """
        return self.driver.get_screenshot_as_png()

    def input_enter(self):
        return self.driver.keyevent(66)

    def screenshot_as_file(self):
        '''
        截图功能
        :return:
        '''
        timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        file_name = fr'../app/images/{timestr}.png'
        return self.driver.get_screenshot_as_file(file_name)

    def base_unlock(self):
        """
        解锁手机
        :return:
        """
        os.system('adb shell input keyevent 82')
        time.sleep(0.5)
        os.system('adb shell input keyevent 82')

    def get_web_view(shelf, driver):
        webview = driver.contexts
        for viw in webview:
            if 'WEBVIEW_cn.com.open.mooc' in viw:
                driver.switch_to.context(viw)
                break
        driver.find_element_by_link_text('C').click()
        try:
            driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
        except Exception as e:
            driver.switch_to.context(webview[0])
            driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
            raise e

    def page_source(self):
        return self.driver.page_source

    def pwd_path(self):
        return os.getcwd()

    def father_path(self):
        father_path = os.path.abspath(os.path.dirname(self.pwd_path()) + os.path.sep + ".")
        return father_path

    def grader_father_path(self):
        grader_father_path = os.path.abspath(os.path.dirname(self.pwd_path()) + os.path.sep + "..")
        return grader_father_path

    def get_caps(self, param):
        get_data = GetFile(file_path=fr'{self.father_path()}\data\caps.yaml')
        if param == 'caps':
            return get_data.get_yaml_data('desirecaps_cts')
        elif param == 'IP':
            return get_data.get_yaml_data('server')['IP']
        else:
            return get_data.get_yaml_data('server')['port']
