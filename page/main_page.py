# coding=utf-8
"""
@project_name:  android-cts-verifier
@file:          main_page.PY
@Author:        nong
@Time:          2021/7/22 13:29

"""
from base.base_page import BasePage
from business.audio import Audio


class MainPage(BasePage):
    """
    主界面类
    每一个类文件对应一个yml文件，yml文件存放类中方法的页面元素
    """

    def audio_acoustic_echo_cancellation_AEC(self):
        """
        步骤 2 此测试项需要安静的环境，无需插耳机。
        步骤 2 单击Yes按钮，再单击TEST
        """
        self.parse('main_page.yml', 'audio_acoustic_echo_cancellation_AEC')
        return Audio.click_audio_acoustic_echo_cancellation_AEC(self.driver)
