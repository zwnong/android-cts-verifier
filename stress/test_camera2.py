#!coding = 'utf-8'
"""
@author:zwnong
@project: ui_framework
@time:2021/8/30:12:59
"""
import os
import sys
from time import sleep

import allure
import pytest
from appium import webdriver

sys.path.append(fr'{os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + ".")}')
from base.base_page import BasePage
from base.base_driver import BaseDriver
from utils.dos_cmd import DosCmd


@allure.feature('相机压测')
class TestCamera:
    def setup_class(self):
        self.cmd = DosCmd()
        desirecaps = {
            "platformName": "Android",
            # automationName: UiAutomator2
            "deviceName": "P2100950002B",
            "udid": "P2100950002B",
            "appPackage": "com.android.camera2",
            "appActivity": "com.android.camera.CameraLauncher",
            # 跳过安装uiautomator2 服务
            # "skipServerInstallation": True,
            # 跳过初始化
            #  "skipDeviceInstallation": True,
            "settings[waitForIdleTimeout]": 1,
            "newCommandTimeout": 2000,
            "noReset": True
        }
        self.driver = webdriver.Remote(f"http://127.0.0.1:4725/wd/hub", desirecaps)
        self.driver.implicitly_wait(10)

    def setup(self):
        pass

    def teardown(self):
        pass

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.repeat(10000)
    @pytest.mark.flaky(reruns=3)  # 失败重跑
    @allure.story('切换前后摄像头拍照压测')
    def test_switch_camera(self):
        self.d = BasePage(self.driver)
        self.d.parse(r'D:\ui_framework\stress\camera.yml', 'take_a_photos')
        sleep(1)
        self.d.parse(r'D:\ui_framework\stress\camera.yml', 'switch_camera')
        sleep(1)
        self.d.parse(r'D:\ui_framework\stress\camera.yml', 'take_a_photos')
        sleep(1)
        self.d.parse(r'D:\ui_framework\stress\camera.yml', 'switch_camera')
        sleep(1)

    @pytest.mark.repeat(500)
    @pytest.mark.flaky(reruns=3)  # 失败重跑
    @allure.story('重启后切换前后摄像头拍照压测')
    def test_reboot_switch_camera(self):
        device = 'P2100950002B'
        self.cmd.excute_cmd(f'adb -s {device} reboot')
        self.cmd.excute_cmd(f'adb -s {device} wait-for-device')
        sleep(25)
        self.cmd.excute_cmd(f'adb -s {device} shell input keyevent 82')
        self.cmd.excute_cmd(f'adb -s {device} shell input keyevent 82')
        driver = BaseDriver().android_driver(
            device=device,
            package='com.android.camera2',
            activity='com.android.camera.CameraLauncher',
            port=4725
        )
        self.d = BasePage(driver)
        sleep(2)
        self.d.parse(r'D:\ui_framework\stress\camera.yml', 'take_a_photos')
        sleep(2)
        self.d.parse(r'D:\ui_framework\stress\camera.yml', 'switch_camera')
        sleep(2)
        self.d.parse(r'D:\ui_framework\stress\camera.yml', 'take_a_photos')
        sleep(2)
        self.d.parse(r'D:\ui_framework\stress\camera.yml', 'switch_camera')
        sleep(2)
        self.cmd.excute_cmd(f'adb -s {device} shell input keyevent 3')
        sleep(12)
