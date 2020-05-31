# -*- coding: utf-8 -*-
"""
********************************
@Time     :2019/9/5 21:44
@Author   :gaoliang
@Email    :337901080@qq.com
@File     :lemon_unittest_08_result_to_file.py
@Software :PyCharm
********************************
"""
# 进一步美化报告
# pip install html-testRunner
import os
import unittest
from datetime import datetime

from libs.HTMLTestRunnerNew import HTMLTestRunner  # 网上大佬修改的
# from HTMLTestRunner_PY3 import HTMLTestRunner  # 我自己搜的
from scripts.handle_config import do_config
from scripts.constants import CASES_DIR, REPORTS_DIR, USER_ACCOUNTS_FILE_PATH
from scripts.handle_user import generate_users_config

# 如果用户配置文件不存在，则新建
if not os.path.isfile(USER_ACCOUNTS_FILE_PATH):
    generate_users_config()

# 加载CASES_DIR目录下，以test*开头的模块
one_suite = unittest.defaultTestLoader.discover(CASES_DIR)
# 3.执行用例
report_html_name = os.path.join(REPORTS_DIR, do_config("report", "report_html_name"))
report_html_name_full = report_html_name + "_" + datetime.strftime(datetime.now(), "%Y%m%d%H%M%S") + ".html"
with open(report_html_name_full, mode="wb") as save_to_file:
    one_runner = HTMLTestRunner(stream=save_to_file,
                                verbosity=do_config("report", "verbosity"),   # 日志详细程度
                                title=do_config("report", "title"),
                                description=do_config("report", "description"),
                                tester=do_config("report", "tester"))

    one_runner.run(one_suite)  # 批量执行套件中的用例
