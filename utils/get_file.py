# coding = utf-8
"""
@File     :  get_file.py
@project  :  
@Author   :  zwnong
@Time     :  2021/1/30  3:07
"""
import os

import yaml
import sys

sys.path.append('..')


class GetFile:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = fr'{os.path.abspath(os.path.dirname(os.getcwd() + os.path.sep + "."))}\datas\user_config.yaml'
        else:
            self.file_path = file_path
        self.data = self.get_yaml()

    def get_yaml(self):
        data = yaml.safe_load(open(str(self.file_path), 'r', encoding='utf-8'))
        return data

    def join_data(self, i, device, bp, port):
        data = {
            "user_info_" + str(i): {
                "deviceName": device,
                "bp": bp,
                "port": port
            }
        }
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

    # 传入key获取value
    def get_value(self, *args):

        try:
            value = self.data.get(*args)
        except EOFError:
            value = None
        return value


if __name__ == '__main__':
    data = GetFile()
