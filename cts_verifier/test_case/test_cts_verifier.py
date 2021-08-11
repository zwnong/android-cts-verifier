# coding=utf-8
"""
@project_name:  ui_framework
@file:          test_cts_verifier.PY
@Author:        nong
@Time:          2021/7/28 19:15

"""
from time import sleep

from cts_verifier.page.app import App
import pytest

from utils.sever import Server


class TestCtsVerifier:

    def setup_class(self):
        print('启动appium server')
        self.server = Server()
        self.server.main()
        print('初始化')
        self.app = App()
        self.app.device_init()
        self.cts_driver = self.app.start_driver()
        self.settings_driver = self.app.start_other_device_cts_driver()
        self.app.goto_other_device_cts_driver_page().camera_performance()

    def teardown_class(self):
        print('******所有用例结束******')
        print('关闭cts_driver')
        self.app.stop_cts_driver()
        print('停止settings_driver')
        self.app.stop_setting_driver()
        self.app.stop_other_device()
        print('关闭appium server')
        self.server.kill_server()

    def setup(self):
        sleep(1)

    def teardown(self):
        if 'CTS Verifier 11_r4' in self.app.cts_page_source():
            print("")
        else:
            self.app.cts_driver_restart()
        sleep(2)

    # -----------------------------------------------audio------------------------------------------------
    @pytest.mark.run(order=1)
    def test_audioAcoustic_echo_cancellation_AEC_Test(self):
        """
        进入Audio Acoustic Echo Cancellation（AEC）Test测试，此测试项需要安静的环境，无需插耳机。
        单击Yes按钮，再单击TEST
        :return:
        """
        test = self.app.goto_cts_main_page().audio_acoustic_echo_cancellation_AEC_test()
        test.no_btn()
        test.pass_btn()

    @pytest.mark.run(order=2)
    def test_audio_MIDI_Test(self):
        """
        直接点击pass
        """
        self.app.goto_cts_main_page().MIDI_Test().pass_btn()

    # -----------------------------------------------Camera------------------------------------------------
    @pytest.mark.run(order=3)
    def test_camera_bokeh(self):
        bokeh_page = self.app.goto_cts_main_page().camera_bokeh()
        bokeh_page.next_btn()
        bokeh_page.pass_btn()

    @pytest.mark.run(order=4)
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

    # """test_camera_performance_page"""
    @pytest.mark.run(order=5)
    def test_single_capture(self):
        """
        点击 test_single_capture项
        :return:
        """
        camera_performance_page = self.app.goto_cts_main_page().camera_performance()
        global n
        # steps = self.app.goto_main_page().camera_performance()
        # steps.click_test_single_capture()
        camera_performance_page.click_test_single_capture()
        # 处理等待自动测试时间，以开始下一条测试用例进行
        self.app.camera_performance_page_opinion(20)
        assert 'CTS Verifier 11_r4' in self.app.cts_page_source()

    @pytest.mark.run(order=6)
    def test_reprocessing_latency(self):
        """
        点击test_reprocessing_latency 项
        :return:
        """
        camera_performance_page = self.app.goto_cts_main_page().camera_performance()
        camera_performance_page.click_test_reprocessing_latency()
        self.app.camera_performance_page_opinion(5)
        assert 'CTS Verifier 11_r4' in self.app.cts_page_source()

    @pytest.mark.run(order=7)
    def test_reprocessing_capture_stall(self):
        """
        点击 test_reprocessing_capture_stall 项
        :return:
        """
        camera_performance_page = self.app.goto_cts_main_page().camera_performance()
        camera_performance_page.click_test_reprocessing_capture_stall()
        self.app.camera_performance_page_opinion(5)
        assert 'CTS Verifier 11_r4' in self.app.cts_page_source()

    @pytest.mark.run(order=8)
    def test_legacy_api_performance(self):
        """
        点击 test_legacy_api_performance
        :return:
        """
        global n
        camera_performance_page = self.app.goto_cts_main_page().camera_performance()
        camera_performance_page.click_test_legacy_api_performance()
        # 处理等待自动测试时间，以开始下一条测试用例进行
        self.app.camera_performance_page_opinion(10)
        assert 'CTS Verifier 11_r4' in self.app.cts_page_source()

    @pytest.mark.run(order=9)
    def test_high_quality_reprocessing_latency(self):
        """
        点击test_high_quality_reprocessing_latency
        :return:
        """
        camera_performance_page = self.app.goto_cts_main_page().camera_performance()
        camera_performance_page.click_test_high_quality_reprocessing_latency()
        self.app.camera_performance_page_opinion(5)
        assert 'CTS Verifier 11_r4' in self.app.cts_page_source()

    @pytest.mark.run(order=10)
    def test_reprocessing_throughput(self):
        """
        点击test_reprocessing_throughput
        :return:
        """
        camera_performance_page = self.app.goto_cts_main_page().camera_performance()
        camera_performance_page.click_test_reprocessing_throughput()
        self.app.camera_performance_page_opinion(2)
        assert 'CTS Verifier 11_r4' in self.app.cts_page_source()

    @pytest.mark.run(order=11)
    def test_high_quality_reprocessing_throughput(self):
        """
        点击test_high_quality_reprocessing_throughput
        :return:
        """
        camera_performance_page = self.app.goto_cts_main_page().camera_performance()
        camera_performance_page.click_test_high_quality_reprocessing_throughput()
        self.app.camera_performance_page_opinion(2)
        assert 'CTS Verifier 11_r4' in self.app.cts_page_source()

    @pytest.mark.run(order=12)
    def test_multiple_capture(self):
        """
        点击 test_multiple_capture
        :return:
        """
        global n
        camera_performance_page = self.app.goto_cts_main_page().camera_performance()
        camera_performance_page.click_test_multiple_capture()
        sleep(1)
        # 处理等待自动测试时间，以开始下一条测试用例进行
        self.app.camera_performance_page_opinion(15)
        assert 'CTS Verifier 11_r4' in self.app.cts_page_source()

    @pytest.mark.run(order=13)
    def test_camera_launch(self):
        """
        点击 test_camera_launch
        :return:
        """
        global n
        camera_performance_page = self.app.goto_cts_main_page().camera_performance()
        camera_performance_page.click_test_camera_launch()
        sleep(1)
        # 处理等待自动测试时间，以开始下一条测试用例进行
        self.app.camera_performance_page_opinion(10)
        assert 'CTS Verifier 11_r4' in self.app.cts_page_source()

    @pytest.mark.run(order=14)
    def test_click_camera_performance_page_pass_btn(self):
        camera_performance_page = self.app.goto_cts_main_page().camera_performance()
        camera_performance_page.pass_btn()
        sleep(1)
        if 'testSingleCapture' in self.app.cts_page_source():
            camera_performance_page.fail_btn()
        else:
            print('有异常，具体查看camera_performance项')

    # -----------------------------------------------CAR------------------------------------------------
    @pytest.mark.run(order=15)
    def test_car_dock_test(self):
        car_dock_test_page = self.app.goto_cts_main_page().car_dock_test()
        car_dock_test_page.click_enable_car_mode()
        self.app.click_home()

    # -----------------------------------------------Device Administration------------------------------
    @pytest.mark.run(order=16)
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

    @pytest.mark.run(order=17)
    def test_admin_uninstall_test(self):
        # 安装辅助程序并断言是否安装成功
        self.app.install_device_admin()
        assert 'Success' in self.app.install_device_admin()
        print('install CtsEmptyDeviceAdmin.apk:Success')
        # 设置 Activate device admin app
        self.app.start_settings()
        self.app.goto_setting_main_page().set_activate_this_device_admin_app()
        # self.app.start_activity('com.android.cts.verifier', 'com.android.cts.verifier.CtsVerifierActivity')
        # device_admin_uninstall_test_page = self.app.goto_cts_main_page().device_admin_uninstall_test()
        # device_admin_uninstall_test_page.enable_admin()
        # self.app.uninstall_device_admin()
        # sleep(1)
        # device_admin_uninstall_test_page.launch_settings()
        # device_admin_uninstall_test_page.pass_btn()
        # self.app.stop_setting_driver()

    # -----------------------------------------------DISPLAY CUTOUT------------------------------
    @pytest.mark.run(order=18)
    def test_display_cutout_test(self):
        screen_lock_test = self.app.goto_cts_main_page().display_cutout_test()
        screen_lock_test.click_numbers()
        sleep(2)
        screen_lock_test.pass_btn()

