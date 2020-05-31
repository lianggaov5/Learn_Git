# -*- coding: utf-8 -*-
"""
********************************
@Time     :2019/9/8 7:25
@Author   :gaoliang
@Email    :337901080@qq.com
@File     :handle_log.py
@Software :PyCharm
********************************
"""
import time
import os
import logging
from logging.handlers import RotatingFileHandler
from scripts.handle_config import do_config
from scripts.constants import LOGS_DIR
# pip install concurrent-log-handler    第三方日志插件
# from concurrent_log_handle import ConcurrentRotatingFileHandle  # 解决多个程序同时操作同一个日志文件的问题


class HandleLog:
    """
    定义一个处理日志的类
    """

    def __init__(self):
        self.case_logger = logging.getLogger(do_config("log", "logger_name"))

        self.case_logger.setLevel(do_config("log", "logger_level"))

        console_handle = logging.StreamHandler()
        # ConcurrentRotatingFileHandle,其它一样
        file_handle = RotatingFileHandler(os.path.join(LOGS_DIR, do_config("log", "logging_file")),
                                          maxBytes=do_config("log", "file_size")*1024,
                                          backupCount=do_config("log", "backupCount"),
                                          encoding="utf8")

        console_handle.setLevel(do_config("log", "console_level"))
        file_handle.setLevel(do_config("log", "file_level"))

        simple_formatter = logging.Formatter(do_config("log", "simple_formatter"))   # 简单的日志格式
        complex_formatter = logging.Formatter(do_config("log", "complex_formatter"))
        console_handle.setFormatter(simple_formatter)
        file_handle.setFormatter(complex_formatter)

        self.case_logger.addHandler(console_handle)
        self.case_logger.addHandler(file_handle)

    def get_logger(self):
        """
        获取logger日志对象
        :return:
        """
        return self.case_logger


do_log = HandleLog().get_logger()

if __name__ == '__main__':
    case_logger = HandleLog().get_logger()
    for _ in range(500):
        time.sleep(0.5)
        case_logger.error("这是error日志")
