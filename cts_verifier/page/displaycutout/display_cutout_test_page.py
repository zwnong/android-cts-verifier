# coding=utf-8
"""
@project_name:  ui_framework
@file:          displaycutout_test_page.PY
@Author:        nong
@Time:          2021/8/6 17:11

"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class DisplayCutoutTestPage(BasePage):
    def click_numbers(self):
        for i in range(0, 16):
            self.find_and_click(By.XPATH, f'//*[@text="{i}"]')

    def pass_btn(self):
        """
        :return:点击pass
        """
        self.parse(fr'{self.father_path()}\yaml\displaycutout\display_cutout_test_page.yml', 'pass_btn')


if __name__ == '__main__':
    DisplayCutoutTestPage().click_numbers()
