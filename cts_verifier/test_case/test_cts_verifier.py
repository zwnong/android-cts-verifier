# coding=utf-8
"""
@project_name:  ui_framework
@file:          test_cts_verifier.PY
@Author:        nong
@Time:          2021/7/28 19:15

"""
from time import sleep

from cts_verifier.page.app import App


class TestCtsVerifier:
    def setup_class(self):
        self.app = App()
        self.app.start_android_driver()

    def teardown_class(self):
        self.app.stop_android_driver()

    def setup(self):
        sleep(1)

    def teardown(self):
        pass

    def test_audioAcoustic_echo_cancellation_AEC_Test(self):
        """
        进入Audio Acoustic Echo Cancellation（AEC）Test测试，此测试项需要安静的环境，无需插耳机。
        单击Yes按钮，再单击TEST
        :return:
        """
        test = self.app.goto_main_page().audio_acoustic_echo_cancellation_AEC_test()
        test.no_btn()
        test.pass_btn()

    def test_MIDI_Test(self):
        """
        直接点击pass
        """
        self.app.goto_main_page().MIDI_Test().pass_btn()

    def test_show_alarms(self):
        """
        测试目的：验证 SHOW_ALARMS API的功能。
        验证Clock应用的UI是否打开，同时是否显示闹钟列表
        :return:
        """
        self.app.goto_main_page().clock_alarms_and_timers_tests()
        sleep(5)
