# coding=utf-8
"""
@project_name:  ui_framework
@file:          device_admin_tapjacking_test_page.PY
@Author:        nong
@Time:          2021/7/30 15:24

"""
from base.base_page import BasePage


class DeviceAdminTapjackingTestPage(BasePage):
    def click_enable_device_admin(self):
        """
        :return:单击ENABLE DEVICE ADMIN
        """
        self.parse(fr'{self.father_path()}\yaml\device_administration\device_admin_tapjacking_test_page.yml', 'click_enable_device_admin')

    def pass_btn(self):
        """
        :return点击pass
        """
        self.parse(fr'{self.father_path()}\yaml\device_administration\device_admin_tapjacking_test_page.yml', 'pass_btn')