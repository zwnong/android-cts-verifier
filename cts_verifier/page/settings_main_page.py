# coding=utf-8
"""
@project_name:  ui_framework
@file:          settings_main_page.PY
@Author:        nong
@Time:          2021/8/11 13:12

"""
from base.base_page import BasePage


class SettingsMainPage(BasePage):
    def set_activate_this_device_admin_app(self):
        """
        :return:
        """
        # 1 - 点击 Security
        self.swipe_find(fr'{self.father_path()}\yaml\settings_page.yml', 'Security')
        # 2 - 点击 Device admin apps
        self.swipe_find(fr'{self.father_path()}\yaml\settings_page.yml', 'device_admin_apps')
        # 3 - 点击 Test Device Admin
        self.swipe_find(fr'{self.father_path()}\yaml\settings_page.yml', 'test_device_admin')
        # 4 - 点击 Activate this device admin app
        self.swipe_find(fr'{self.father_path()}\yaml\settings_page.yml', 'activate_this_device_admin_app')
