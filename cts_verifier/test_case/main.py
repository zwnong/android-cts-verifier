# coding=utf-8
"""
@project_name:  ui_framework
@file:          main.PY
@Author:        nong
@Time:          2021/8/4 19:27

"""
import pytest

from utils.sever import Server

if __name__ == '__main__':
    server = Server()
    server.main()
    pytest.main(["-vs --alluredir ./allure_report", "test_demo.py"])
    server.kill_server()
