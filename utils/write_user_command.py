# coding = utf-8
"""
@All-project: Appium
@author: ZWNONG
@file: write_user_command.py
@time: 2020-06-22 19:07:45
"""
import os

import yaml


class WriteUserCommand:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = fr'{os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + ".")}\datas\user_config.yaml'
        else:
            self.file_path = file_path

    def read_data(self):
        """
        加载yaml数据
        :return:
        """
        with open(self.file_path, 'rb') as fr:
            data = yaml.load(fr, Loader=yaml.FullLoader)
        return data

    def write_data(self, i, device, bp, port):
        """
        写入数据
        :param port:
        :param bp:
        :param device:
        :param i:
        :return:
        """
        data = self.join_data(i, device, bp, port)
        with open(self.file_path, 'a') as fr:
            yaml.dump(data, fr)

    def join_data(self, i, device, bp, port):
        data = {
            "user_info_"+str(i): {
                "deviceName": device,
                "bp": bp,
                "port": port
            }
        }
        return data

    def clear_data(self):
        with open(self.file_path, 'w') as fr:
            fr.truncate()

    def get_yaml_lines(self):
        """
        获取yaml的行数 即字典的大小
        :return:
        """
        data = self.read_data()
        return len(data)

    def get_value(self, key, port):
        """
        获取yaml的值
        :return:
        """
        data = self.read_data()
        value = data[key][port]
        return value


if __name__ == '__main__':
    test = WriteUserCommand()

    print(test.get_value('user_info_0', 'port'))