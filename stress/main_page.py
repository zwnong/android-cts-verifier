#!coding = 'utf-8'
"""
@author:zwnong
@project: ui_framework
@time:2021/8/31:9:43
"""
from base.base_page import BasePage


class MainPage(BasePage):
    def take_a_photos(self):
        self.parse('./camera.yml', 'take_a_photos')

    def switch_camera(self):
        self.parse('./camera.yml', 'switch_camera')
