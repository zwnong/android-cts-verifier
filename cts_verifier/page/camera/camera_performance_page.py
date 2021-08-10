# coding=utf-8
"""
@project_name:  ui_framework
@file:          camera_performance_page.PY
@Author:        nong
@Time:          2021/7/29 13:51

"""
from base.base_page import BasePage


class CameraPerformancePage(BasePage):
    def click_test_single_capture(self):
        """
        :return:点击 test_single_capture项 自动测试
        """
        self.parse(fr'{self.father_path()}\yaml\camera\camera_performance_page.yml', 'click_test_single_capture')

    def click_test_reprocessing_latency(self):
        """
        :return: click_test_reprocessing_latency
        """
        self.parse(fr'{self.father_path()}\yaml\camera\camera_performance_page.yml', 'click_test_reprocessing_latency')

    def click_test_reprocessing_capture_stall(self):
        """
        :return: click_test_reprocessing_capture_stall
        """
        self.parse(fr'{self.father_path()}\yaml\camera\camera_performance_page.yml', 'click_test_reprocessing_capture_stall')

    def click_test_legacy_api_performance(self):
        """
        :return: click_test_legacy_api_performance
        """
        self.parse(fr'{self.father_path()}\yaml\camera\camera_performance_page.yml', 'click_test_legacy_api_performance')

    def click_test_high_quality_reprocessing_latency(self):
        """
        :return: click_test_high_quality_reprocessing_latency
        """
        self.parse(fr'{self.father_path()}\yaml\camera\camera_performance_page.yml', 'click_test_high_quality_reprocessing_latency')

    def click_test_reprocessing_throughput(self):
        """
        :return: click_test_reprocessing_throughput
        """
        self.parse(fr'{self.father_path()}\yaml\camera\camera_performance_page.yml', 'click_test_reprocessing_throughput')

    def click_test_high_quality_reprocessing_throughput(self):
        """
        :return: click_test_high_quality_reprocessing_throughput
        """
        self.parse(fr'{self.father_path()}\yaml\camera\camera_performance_page.yml', 'click_test_high_quality_reprocessing_throughput')

    def click_test_multiple_capture(self):
        """
        :return: click_test_multiple_capture
        """
        self.parse(fr'{self.father_path()}\yaml\camera\camera_performance_page.yml', 'click_test_multiple_capture')

    def click_test_camera_launch(self):
        """
        :return: click_test_camera_launch
        """
        self.parse(fr'{self.father_path()}\yaml\camera\camera_performance_page.yml', 'click_test_camera_launch')

    def pass_btn(self):
        """
        :return: 点击pass
        """
        self.parse(fr'{self.father_path()}\yaml\camera\camera_performance_page.yml', 'pass_btn')

    def fail_btn(self):
        """
        :return: 点击fail
        """
        self.parse(fr'{self.father_path()}\yaml\camera\camera_performance_page.yml', 'fail_btn')
