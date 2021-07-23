#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 14:03
# @Author  : zwnong
# @File    : testcase.py
# @Software: win10 Tensorflow1.13.1 python3.9.5
import time
from time import sleep

from appium import webdriver

from base.base_page import BasePage


class TestCase:
    def setup(self):
        capabilities = {
            "platformName": "Android",
            # "automationName": "UiAutomator2",
            "deviceName": "DVKS232D20110300016",
            "appPackage": "com.android.cts.verifier",
            "appActivity": "com.android.cts.verifier.CtsVerifierActivity",
            "noReset": "True"
        }
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        time.sleep(5)
        self.driver = BasePage(driver)

    def teardown(self):
        pass

    def test_call_1(self):
        self.driver.find_and_click('xpath', '//*[@resource-id="android:id/text1" and @text="Audio Frequency Line Test"]')
