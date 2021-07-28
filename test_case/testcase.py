#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 14:03
# @Author  : zwnong
# @File    : testcase.py
# @Software: win10 Tensorflow1.13.1 python3.9.5
import os
from time import sleep


class TestCase:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_car_dock(self):
        """
        4.1 Car Dock Test
        :return:
        """
        self.driver.swipe_find('xpath', '//*[@@text="Car Dock Test"]', 10)
        self.driver.find_and_click('xpath',
                                   '//*[@resource-id="com.android.cts.verifier:id/car_mode" and @text="ENABLE CAR MODE"]')
        os.system('adb shell input keyevent KEYCODE_HOME')
        sleep(2)
        assert 'from home button pass' in self.driver.page_source()
