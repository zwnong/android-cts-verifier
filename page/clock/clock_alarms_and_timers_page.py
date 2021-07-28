# coding=utf-8
"""
@project_name:  android-cts-verifier
@file:          clock_alarms_and_timers_page.PY
@Author:        nong
@Time:          2021/7/28 11:24

"""
from base.base_page import BasePage


class ClockAlarmsAndTimersPage(BasePage):
    def alarm_show_alarms_test(self):
        self.parse('clock_alarms_and_timers_page.yml', 'alarm_show_alarms_test')

    def alarm_set_alarm_test(self):
        self.parse('clock_alarms_and_timers_page.yml', 'alarm_set_alarm_test')

    def alarm_start_alarm_test(self):
        self.parse('clock_alarms_and_timers_page.yml', 'alarm_start_alarm_test')

    def alarm_full_alarm_test(self):
        self.parse('clock_alarms_and_timers_page.yml', 'alarm_full_alarm_test')

    def timers_set_timer_test(self):
        self.parse('clock_alarms_and_timers_page.yml', 'timers_set_timer_test')

    def timer_start_timer_test(self):
        self.parse('clock_alarms_and_timers_page.yml', 'timer_start_timer_test')

    def timer_start_timer_with_ui_test(self):
        self.parse('clock_alarms_and_timers_page.yml', 'timer_start_timer_with_ui_test')
