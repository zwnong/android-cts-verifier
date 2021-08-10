# coding=utf-8
"""
@project_name:  ui_framework
@file:          test_cts_verifier.PY
@Author:        nong
@Time:          2021/7/28 19:15

"""
from time import sleep

from cts_verifier.business.test_camera import TestCamera
from cts_verifier.page.app import App
import pytest

from utils.sever import Server


class TestCtsVerifier:

    def setup_class(self):
        self.server = Server()
        self.server.main()
        self.app = App()
        self.cts_driver = self.app.start_cts_driver()
        self.settings_driver = self.app.start_android_settings_driver()

    def teardown_class(self):
        self.server.kill_server()
        self.app.stop_cts_driver()
        self.app.stop_setting_driver()


    def setup(self):
        self.app.start_cts_driver()
        sleep(1)

    def teardown(self):
        sleep(2)

    # -----------------------------------------------audio------------------------------------------------
    def test_audioAcoustic_echo_cancellation_AEC_Test(self):
        """
        进入Audio Acoustic Echo Cancellation（AEC）Test测试，此测试项需要安静的环境，无需插耳机。
        单击Yes按钮，再单击TEST
        :return:
        """
        test = self.app.goto_cts_main_page().audio_acoustic_echo_cancellation_AEC_test()
        test.no_btn()
        test.pass_btn()

    def test_audio_MIDI_Test(self):
        """
        直接点击pass
        """
        self.app.goto_cts_main_page().MIDI_Test().pass_btn()

    # -----------------------------------------------Camera------------------------------------------------
    def test_camera_bokeh(self):
        bokeh_page = self.app.goto_cts_main_page().camera_bokeh()
        bokeh_page.next_btn()
        bokeh_page.pass_btn()

    def test_camera_flashlight(self):
        camera_flashlight = self.app.goto_cts_main_page().camera_flashlight()
        camera_flashlight.start_btn()
        camera_flashlight.on_btn()
        camera_flashlight.next_btn()
        camera_flashlight.off_btn()
        for i in range(5):
            camera_flashlight.next_btn()
            sleep(1)
            if 'All tests passed. Press Done or Pass button.' in self.app.cts_page_source():
                sleep(2)
                camera_flashlight.done_btn()
                sleep(1)
                if self.app.isElement('xpath', '//*[@resource-id="com.android.cts.verifier:id/pass_button"'):
                    camera_flashlight.pass_btn()
                else:
                    break
            else:
                camera_flashlight.on_btn()
                camera_flashlight.next_btn()
                camera_flashlight.off_btn()

    def test_camera_performance_page(self):
        camera_performance_page = TestCamera(self.app, self.app.start_cts_driver().goto_cts_main_page().camera_performance())
        camera_performance_page.test_single_capture()
        camera_performance_page.test_reprocessing_capture_stall()
        camera_performance_page.test_legacy_api_performance()
        camera_performance_page.test_high_quality_reprocessing_latency()
        camera_performance_page.test_reprocessing_throughput()
        camera_performance_page.test_high_quality_reprocessing_throughput()
        camera_performance_page.test_multiple_capture()
        camera_performance_page.test_camera_launch()
        camera_performance_page.click_pass()

    # -----------------------------------------------CAR------------------------------------------------
    def test_car_dock_test(self):
        car_dock_test_page = self.app.goto_cts_main_page().car_dock_test()
        car_dock_test_page.click_enable_car_mode()
        self.app.click_home()

    # -----------------------------------------------Device Administration------------------------------
    def test_device_admin_tapjacking_test(self):
        device_admin_tapjacking_test = self.app.goto_cts_main_page().device_admin_tapjacking_test()
        device_admin_tapjacking_test.click_enable_device_admin()
        sleep(5)
        self.app.click_back()
        sleep(1)
        self.app.click_back()
        sleep(2)
        if '1. Launch the device admin add screen by pressing the button below' in self.app.cts_page_source():
            device_admin_tapjacking_test.pass_btn()
        else:
            print('不在device_admin_tapjacking_test页面')

    # -----------------------------------------------DISPLAY CUTOUT------------------------------
    def test_display_cutout_test(self):
        screen_lock_test = self.app.goto_cts_main_page().display_cutout_test()
        screen_lock_test.click_numbers()
        sleep(2)
        screen_lock_test.pass_btn()
