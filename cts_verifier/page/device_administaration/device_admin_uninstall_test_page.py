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
    def set_device_admin(self):
        os.system("adb shell dpm set-device-owner com.android.cts.emptydeviceadmin/.EmptyDeviceAdmin")

    def install_test_device_admin_apk(self):
        os.system(fr'adb install {self.father_path()}\cts_test_apks\CtsEmptyDeviceAdmin.apk')

    def enable_admin(self):
        self.parse(fr'{self.father_path()}\yaml\device_administration\device_admin_uninstall_test_page.yml', 'enable_admin')

    def launch_settings(self):
        self.parse(fr'{self.father_path()}\yaml\device_administration\device_admin_uninstall_test_page.yml', 'launch_settings')

    def pass_btn(self):
        self.parse(fr'{self.father_path()}\yaml\device_administration\device_admin_uninstall_test_page.yml', 'pass_btn')