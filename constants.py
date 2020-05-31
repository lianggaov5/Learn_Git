# -*- coding: utf-8 -*-
"""
********************************
@Time     :2019/9/12 2:06
@Author   :gaoliang
@Email    :337901080@qq.com
@File     :constants.py
@Software :PyCharm
********************************
"""
import os

# __file__   # 固定变量

os.path.abspath(__file__)

# 获取当前文件夹所在路径
os.path.dirname(os.path.abspath(__file__))

# 获取项目根目录路径(当前文件夹的上一级文件夹所在路径)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取测试数据datas目录所在的路径   拼接
DATAS_DIR = os.path.join(BASE_DIR, "datas")
TEST_DATAS_FILE_PATH = os.path.join(DATAS_DIR, "cases.xlsx")

# 获取配置文件configs目录所在的路径
CONFIGS_DIR = os.path.join(BASE_DIR, "configs")
CONFIGS_FILE_PATH = os.path.join(CONFIGS_DIR, "testcase.conf")
USER_ACCOUNTS_FILE_PATH = os.path.join(CONFIGS_DIR, "user_account.conf")

# 获取日志文件logs目录所在的路径
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# 获取日志文件reports目录所在的路径
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
pass

# 获取用例cases目录所在的路径
CASES_DIR = os.path.join(BASE_DIR, "cases")
