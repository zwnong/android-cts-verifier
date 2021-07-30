# coding=utf-8
"""
@project_name:  ui_framework
@file:          midi_test_page.PY
@Author:        nong
@Time:          2021/7/29 13:16

"""
from base.base_page import BasePage


class MidiTestPage(BasePage):
    def pass_btn(self):
        """
        :return:点击NO按钮
        """
        self.parse(fr'{self.father_path()}\yaml\audio\audio_acoustic_echo_cancellation_AEC_test_page.yml', 'pass_btn')
