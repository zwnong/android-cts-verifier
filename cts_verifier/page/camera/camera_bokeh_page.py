# coding=utf-8
"""
@project_name:  ui_framework
@file:          camera_bokeh_page.PY
@Author:        nong
@Time:          2021/7/29 13:26

"""
from base.base_page import BasePage


class CameraBokehPage(BasePage):
    def pass_btn(self):
        """
        :return:点击yes按钮
        """
        self.parse(fr'{self.father_path()}\yaml\camera\camera_bokeh_page.yml', 'pass_btn')

    def next_btn(self):
        """
        :return:点击next 按钮
        """
        self.parse(fr'{self.father_path()}\yaml\camera\camera_bokeh_page.yml', 'next_btn')
