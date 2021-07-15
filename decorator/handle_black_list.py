#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: handle_black_list.py
@time: 2021/3/16 18:06
"""
import allure
from appium.webdriver.common.mobileby import MobileBy
import sys

sys.path.append('../')


def handle_black(fun):
    def run(*args, **kwargs):
        """
        # fun-->需要装饰的函数名
        # *arg fun()函数的参数  **kwargs 字典型参数
        :param args:
        :param kwargs:
        :return:
        """
        black_list = [
            "//android.widget.Button[@resource-id='com.google.android.apps.messaging:id/conversation_list_spam_popup_positive_button' and @text='OK']",
            '//*[@resource-id="android:id/button1" and @text="OK"]'
        ]
        # 相当于self
        instance = args[0]

        try:
            # log.debug('finds' + instance[2])
            return fun(*args, **kwargs)
        except Exception:
            # 使用allure打开截图
            allure.attach(instance.screenshot(), attachment_type=allure.attachment_type.PNG)
            # 截图到本地
            # instance.screenshot_as_file()
            for i in black_list:
                ele_path = instance.finds(MobileBy.XPATH, i)
                if len(ele_path) > 0:
                    ele_path[0].click()
            return fun(*args, **kwargs)

    return run
