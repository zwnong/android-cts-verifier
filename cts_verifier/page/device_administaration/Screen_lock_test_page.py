# coding=utf-8
"""
@project_name:  ui_framework
@file:          Screen_lock_test_page.PY
@Author:        nong
@Time:          2021/7/30 15:29

"""
from base.base_page import BasePage


class ScreenLockTestPage(BasePage):
    def force_lock(self):
        self.parse(fr'{self.father_path()}\yaml\device_administration\screen_lock_test_page.yml', 'force_lock')

    def pass_btn(self):
        self.parse(fr'{self.father_path()}\yaml\device_administration\screen_lock_test_page.yml', 'pass_btn')
