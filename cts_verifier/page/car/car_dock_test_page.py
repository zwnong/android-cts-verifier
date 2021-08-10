# coding=utf-8
"""
@project_name:  ui_framework
@file:          car_dock_test_page.PY
@Author:        nong
@Time:          2021/7/29 13:57

"""
from base.base_page import BasePage


class CarDockTestPage(BasePage):
    def click_enable_car_mode(self):
        """
        点击单击Enable Car Mode按钮
        :return:
        """
        self.parse(fr'{self.father_path()}\yaml\car\enable_car_mode_page.yml', 'click_enable_car_mode')
