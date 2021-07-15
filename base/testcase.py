#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 14:03
# @Author  : zwnong
# @File    : testcase.py
# @Software: win10 Tensorflow1.13.1 python3.9.5
from time import sleep

from base_driver import App
from base_page import BasePage


class TestCall(BasePage):
    def setup(self):
        self.driver = App().start_app()

    def test_call_1(self):
        for i in range(1000):
            self.find_and_click('xpath', '//*[@resource-id="com.android.dialer:id/fab"]')
            self.find_and_sendkeys('xpath', '//*[@resource-id="com.android.dialer:id/empty_list_view_message"]', '10011')
            sleep(10)
            self.find_and_click('xpath', '//*[@resource-id="com.android.dialer:id/incall_end_call"]')