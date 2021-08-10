# coding=utf-8
"""
@project_name:  ui_framework
@file:          camera_flashlight_page.PY
@Author:        nong
@Time:          2021/7/29 13:33

"""
from base.base_page import BasePage


class CameraFlashlightPage(BasePage):
    def start_btn(self):
        """
        :return: 该测试项是对 Flashlight 功能进行测试。 点击 start 按钮
        """
        self.parse(fr'{self.father_path()}\yaml\camera\camera_flashlight_page.yml', 'start_btn')

    def on_btn(self):
        """
        :return:  点击ON按钮
        """
        self.parse(fr'{self.father_path()}\yaml\camera\camera_flashlight_page.yml', 'on_btn')

    def off_btn(self):
        """
        :return:  点击OFF按钮
        """
        self.parse(fr'{self.father_path()}\yaml\camera\camera_flashlight_page.yml', 'off_btn')

    def next_btn(self):
        """
        :return:  点击next按钮
        """
        self.parse(fr'{self.father_path()}\yaml\camera\camera_flashlight_page.yml', 'next_btn')

    def pass_btn(self):
        """
        :return:  点击PASS按钮
        """
        self.parse(fr'{self.father_path()}\yaml\camera\camera_flashlight_page.yml', 'pass_btn')

    def fail_btn(self):
        """
        :return:  点击fail按钮
        """
        self.parse(fr'{self.father_path()}\yaml\camera\camera_flashlight_page.yml', 'fail_btn')

    def done_btn(self):
        """
        :return:  点击fail按钮
        """
        self.parse(fr'{self.father_path()}\yaml\camera\camera_flashlight_page.yml', 'done_btn')
