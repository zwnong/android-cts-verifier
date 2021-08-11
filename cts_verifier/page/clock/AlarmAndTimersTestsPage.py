# coding=utf-8
"""
@project_name:  ui_framework
@file:          AlarmAndTimersTests.PY
@Author:        nong
@Time:          2021/7/29 10:17

"""
from base.base_page import BasePage
from cts_verifier.page.clock.show_alarms_test_page import ShowAlarmsTestPage


class AlarmAndTimersTestsPage(BasePage):
    def show_alarms_test(self):
        """
        验证 SHOW_ALARMS API的功能。
        :return:
        """
        self.parse(fr'{self.father_path()}\yaml\clock\alarm_and_timers_tests_page.yml', 'show_alarms_test')
        return ShowAlarmsTestPage(self.driver)

    def set_alarm_test(self):
        """
        验证 SHOW_ALARMS API的功能。
        :return:
        """
        self.parse(fr'{self.father_path()}\yaml\clock\alarm_and_timers_tests_page.yml', 'show_alarms_test')
        return ShowAlarmsTestPage(self.driver)

    def start_alarm_test(self):
        pass

    def full_alarm_test(self):
        pass

    def set_timer_test(self):
        pass

    def start_timer_test(self):
        pass

    def start_timer_with_ui_test(self):
        pass
