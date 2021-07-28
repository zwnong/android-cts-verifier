# coding=utf-8
"""
@project_name:  android-cts-verifier
@file:          audioa_coustic_echo_cancellation_AEC_page.PY
@Author:        nong
@Time:          2021/7/28 10:44

"""
from base.base_page import BasePage


class AudioAcousticEchoCancellationAECPage(BasePage):
    def yes(self):
        self.parse('audioa_coustic_echo_cancellation_AEC_page.yml', 'yes')

    def no(self):
        self.parse('audioa_coustic_echo_cancellation_AEC_page.yml', 'no')

    def _TEST(self):
        self.parse('audioa_coustic_echo_cancellation_AEC_page.yml', 'TEST')

    def _pass(self):
        self.parse('audioa_coustic_echo_cancellation_AEC_page.yml', 'pass_button')

    def _fail(self):
        self.parse('audioa_coustic_echo_cancellation_AEC_page.yml', 'fail_button')

    def result_massage(self):
        self.parse('audioa_coustic_echo_cancellation_AEC_page.yml', 'result_massage')
