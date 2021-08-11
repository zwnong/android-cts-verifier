# coding=utf-8
"""
@project_name:  ui_framework
@file:          device_admin_uninstall_test_page.PY
@Author:        nong
@Time:          2021/7/30 15:20

"""
import os

from base.base_page import BasePage


class DeviceAdminUninstallTestPage(BasePage):

    def enable_admin(self):
        self.parse(fr'{self.father_path()}\yaml\device_administration\device_admin_uninstall_test_page.yml', 'enable_admin')

    def launch_settings(self):
        self.parse(fr'{self.father_path()}\yaml\device_administration\device_admin_uninstall_test_page.yml', 'launch_settings')

    def pass_btn(self):
        self.parse(fr'{self.father_path()}\yaml\device_administration\device_admin_uninstall_test_page.yml', 'pass_btn')