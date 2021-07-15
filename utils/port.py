#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 19:19
# @Author  : zwnong
# @File    : port.py
# @Software: win10 Tensorflow1.13.1 python3.9.5
from utils.dos_cmd import DosCmd


class Port:
    def port_is_used(self, port_num):
        """
        判断端口是否可用
        :param port_num:
        :return:
        """
        flag = None
        self.dos = DosCmd()
        command = 'netstat -ano | findstr ' + str(port_num)
        result = self.dos.excute_cmd_result(command)
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag

    def create_port_list(self, start_port, device_list):
        """
        start_port 4701
        生成可用端口
        :param start_port:
        :param device_list:
        :return:
        """
        port_list = []
        if device_list is not None:
            while len(port_list) != len(device_list):
                if not self.port_is_used(start_port):
                    port_list.append(start_port)
                start_port = start_port + 1
            return port_list
        else:
            print("生成可用端口失败")
            return None


if __name__ == '__main__':
    port = Port()
    li = [1, 2, 3, 4, 5]
    print(port.create_port_list(4722, li))
