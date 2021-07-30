# coding=utf-8
"""
@project_name:  ui_framework
@file:          audio_acoustic_echo_cancellation_AEC_test_page.PY
@Author:        nong
@Time:          2021/7/29 11:32

"""
from base.base_page import BasePage


class AudioAcousticEchoCancellationAECTestPage(BasePage):
    def no_btn(self):
        """
        :return:点击NO按钮
        """
        self.parse(fr'{self.father_path()}\yaml\audio\audio_acoustic_echo_cancellation_AEC_test_page.yml', 'no_btn')

    def yes_btn(self):
        """
        :return:点击YES按钮
        """
        self.parse(fr'{self.father_path()}\yaml\audio\audio_acoustic_echo_cancellation_AEC_test_page.yml', 'yes_btn')

    def TEST_btn(self):
        """
        :return:点击TEST按钮
        """
        self.parse(fr'{self.father_path()}\yaml\audio\audio_acoustic_echo_cancellation_AEC_test_page.yml', 'TEST_btn')

    def pass_btn(self):
        """
        :return:点击PASS按钮
        """
        self.parse(fr'{self.father_path()}\yaml\audio\audio_acoustic_echo_cancellation_AEC_test_page.yml', 'pass_btn')

    def fail_btn(self):
        """
        :return:点击PASS按钮
        """
        self.parse(fr'{self.father_path()}\yaml\audio\audio_acoustic_echo_cancellation_AEC_test_page.yml', 'fail_btn')
