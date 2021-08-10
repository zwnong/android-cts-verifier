# coding=utf-8
"""
@project_name:  ui_framework
@file:          test_camera.PY
@Author:        nong
@Time:          2021/8/4 18:32

"""
from time import sleep
from cts_verifier.page.app import App


class TestCamera:
    def __init__(self, app, camera_performance_page):
        self.app = app
        self.camera_performance_page = camera_performance_page

    def test_single_capture(self):
        """
        点击 test_single_capture项
        :return:
        """
        global n
        # steps = self.app.goto_main_page().camera_performance()
        # steps.click_test_single_capture()
        self.camera_performance_page.click_test_single_capture()
        # 处理等待自动测试时间，以开始下一条测试用例进行
        for i in range(90):
            sleep(20)
            n = len(self.app.find_elements(
                '//*[@resource-id="android:id/message" and @text="Running CTS performance test case..."]'))
            if n == 0:
                assert n == 0
                break

    def test_reprocessing_latency(self):
        """
        点击test_reprocessing_latency 项
        :return:
        """
        self.app.tap_screen(2, 2)
        # self.app.goto_main_page().camera_performance().click_test_reprocessing_latency()
        self.camera_performance_page.click_test_reprocessing_latency()
        sleep(1)

    def test_reprocessing_capture_stall(self):
        """
        点击 test_reprocessing_capture_stall 项
        :return:
        """
        # self.app.goto_main_page().camera_performance().click_test_reprocessing_capture_stall()
        self.camera_performance_page.click_test_reprocessing_capture_stall()
        sleep(1)

    def test_legacy_api_performance(self):
        """
        点击 test_legacy_api_performance
        :return:
        """
        global n
        # self.app.goto_main_page().camera_performance().click_test_legacy_api_performance()
        self.camera_performance_page.click_test_legacy_api_performance()
        sleep(1)
        # 处理等待自动测试时间，以开始下一条测试用例进行
        for i in range(180):
            n = len(self.app.find_elements(
                '//*[@resource-id="android:id/message" and @text="Running CTS performance test case..."]'))
            if n >= 1:
                sleep(10)
            else:
                break
        assert n == 0

    def test_high_quality_reprocessing_latency(self):
        """
        点击test_high_quality_reprocessing_latency
        :return:
        """
        # self.app.goto_main_page().camera_performance().click_test_high_quality_reprocessing_latency()
        self.camera_performance_page.click_test_high_quality_reprocessing_latency()

    def test_reprocessing_throughput(self):
        """
        点击test_reprocessing_throughput
        :return:
        """
        # self.app.goto_main_page().camera_performance().click_test_reprocessing_throughput()
        self.camera_performance_page.click_test_reprocessing_throughput()

    def test_high_quality_reprocessing_throughput(self):
        """
        点击test_high_quality_reprocessing_throughput
        :return:
        """
        # self.app.goto_main_page().camera_performance().click_test_high_quality_reprocessing_throughput()
        self.camera_performance_page.click_test_high_quality_reprocessing_throughput()

    def test_multiple_capture(self):
        """
        点击 test_multiple_capture
        :return:
        """
        global n
        # self.app.goto_main_page().camera_performance().click_test_multiple_capture()
        self.camera_performance_page.click_test_multiple_capture()
        sleep(1)
        # 处理等待自动测试时间，以开始下一条测试用例进行
        for i in range(180):
            n = len(self.app.find_elements(
                '//*[@resource-id="android:id/message" and @text="Running CTS performance test case..."]'))
            if n >= 1:
                sleep(10)
            else:
                break
        assert n == 0

    def test_camera_launch(self):
        """
        点击 test_camera_launch
        :return:
        """
        global n
        # self.app.goto_main_page().camera_performance().click_test_camera_launch()
        self.camera_performance_page.click_test_camera_launch()
        sleep(1)
        # 处理等待自动测试时间，以开始下一条测试用例进行
        for i in range(180):
            n = len(self.app.find_elements(
                '//*[@resource-id="android:id/message" and @text="Running CTS performance test case..."]'))
            if n >= 1:
                sleep(10)
            else:
                break
        assert n == 0
        sleep(10)

    def click_pass(self):
        self.camera_performance_page.pass_btn()
