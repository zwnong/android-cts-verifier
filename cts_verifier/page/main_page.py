#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: main_page.py
@time: 2021/3/11 23:13
"""
from base.base_page import BasePage
from cts_verifier.page.audio.midi_test_page import MidiTestPage
from cts_verifier.page.camera.camera_bokeh_page import CameraBokehPage
from cts_verifier.page.camera.camera_flashlight_page import CameraFlashlightPage
from cts_verifier.page.camera.camera_performance_page import CameraPerformancePage
from cts_verifier.page.car.car_dock_test_page import CarDockTestPage
from cts_verifier.page.clock.AlarmAndTimersTestsPage import AlarmAndTimersTestsPage
from cts_verifier.yaml.audio.audio_acoustic_echo_cancellation_AEC_test_page import \
    AudioAcousticEchoCancellationAECTestPage


class MainPage(BasePage):

    def audio_acoustic_echo_cancellation_AEC_test(self):
        """
        :return:进入Audio Acoustic Echo Cancellation（AEC）Test 页面
        """
        self.parse(fr'{self.father_path()}\yaml\main_page.yml', 'audio_acoustic_echo_cancellation_AEC_test')
        return AudioAcousticEchoCancellationAECTestPage(self.driver)

    def MIDI_Test(self):
        """
        :return:进入MIDI Test 页面
        """
        self.parse(fr'{self.father_path()}\yaml\main_page.yml', 'MIDI_Test')
        return MidiTestPage(self.driver)

    # CAMERA------------------------------------------------------------------------------------

    def camera_bokeh(self):
        """
        :return:进入Camera Bokeh 页面
        """
        self.swipe_find('camera_bokeh')
        return CameraBokehPage(self.driver)

    def camera_flashlight(self):
        """
        :return:进入Flashlight页面
        """
        self.swipe_find('camera_flashlight')
        return CameraFlashlightPage(self.driver)

    def camera_performance(self):
        """
        :return: 进入Camera Performance测试页
        """
        self.swipe_find('camera_flashlight')
        return CameraPerformancePage(self.driver)

    # car---------------------------------------------------------------------------------------
    def car_dock_test(self):
        """
        :return:进入Car Dock Test测试页
        """
        self.swipe_find('car_dock_test')
        return CarDockTestPage(self.driver)

    # CLOCK-------------------------------------------------------------------------------------
    def clock_alarms_and_timers_tests(self):
        """
        :return:进入 Alarms and Timers Tests测试项
        """
        self.swipe_find('clock_alarms_and_timers_tests', 10)
        # self.parse(fr'{self.father_path()}\yaml\main_page.yml', 'clock_alarms_and_timers_tests')
        return AlarmAndTimersTestsPage(self.driver)

    # Device Administration----------------------------------------------------------------------
    def device_admin_tapjacking_test(self):
        """
        :return: 进入Device Admin Tapjacking Test测试页
        """
        self.swipe_find('device_admin_tapjacking_test', 10)
