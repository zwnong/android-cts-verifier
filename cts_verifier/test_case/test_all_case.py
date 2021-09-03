#!coding = 'utf-8'
"""
@author:zwnong
@project: ui_framework
@time:2021/8/24:13:10
"""
import allure
import pytest

from cts_verifier.page.app import App


@allure.feature("CtsVerifier 主页")
class TestAllCase:
    def setup_class(self):
        self.app = App()
        self.app.start_device_0_driver()

    def setup(self):
        pass

    def teardown(self):
        pass

    def teardown_class(self):
        pass

    @pytest.mark.run(order=1)
    @allure.story('AUDIO:click audioAcoustic_echo_cancellation_AEC_Test')
    def test_audioAcoustic_echo_cancellation_AEC_Test(self):
        step = self.app.goto_main_page().audio_acoustic_echo_cancellation_AEC_test()
        step.no_btn()
        step.pass_btn()
