# -*- coding: utf-8 -*-
"""
********************************
@Time     :2019/9/6 18:14
@Author   :gaoliang
@Email    :337901080@qq.com
@File     :excel_rewrite_unittest_03.py
@Software :PyCharm
********************************
"""
# 使用ddt来重构之前的单元测试
# 重构之前的单元测试
import unittest    # 单元测试框架

from libs.ddt import ddt, data
from scripts.handle_excel import HandleExcel
from scripts.handle_config import do_config
from scripts.handle_log import do_log
from scripts.handle_request import HandleRequest
from scripts.constants import TEST_DATAS_FILE_PATH
from scripts.handle_context import HandleContext


@ddt
class TestLogin(unittest.TestCase):
    """
    测试登录功能
    """

    do_excel = HandleExcel(TEST_DATAS_FILE_PATH, "login")  # 类属性
    login_cases_list = do_excel.get_cases()    # 返回一个嵌套元组的列表

    @classmethod
    def setUpClass(cls) -> None:  # setUpClass是unittest框架的方法，会被unittest框架自动调用
        """
        在当前类中所有实例方法执行之前会被调用一次
        重写父类的类方法
        :return:
        """
        cls.send_request = HandleRequest()
        do_log.info("\n\n{:=^40s}".format("开始执行登录功能用例"))

    @classmethod
    def tearDownClass(cls) -> None:
        """
        在当前类中所有实例方法执行结束之后会被调用一次
        :return:
        """
        do_log.info("\n{:=^40s}\n".format("登录功能用例执行结束"))
        cls.send_request.close()

    @data(*login_cases_list)
    def test_login(self, data_namedtuple):
        """
        测试登录功能
        :return:
        """
        url = do_config("api", "url") + data_namedtuple.url
        new_data = HandleContext().login_parameterization(data_namedtuple.data)

        do_log.info("\n正在运行的测试用例为：{}".format(data_namedtuple.title))
        response = self.send_request(method=data_namedtuple.method, url=url, data=new_data)

        # 判断服务器是否有异常
        try:
            self.assertEqual(200, response.status_code,
                             msg="测试【{}】失败，http请求状态码为【{}】".
                             format(data_namedtuple.title, response.status_code))
        except AssertionError as e:
            do_log.error("\n具体异常信息为：{}\n".format(e))
            raise e

        try:
            self.assertEqual(data_namedtuple.expected,
                             response.text,
                             msg="测试{}失败".format(data_namedtuple.title))
        except AssertionError as e:
            do_log.error("\n具体异常信息为：{}\n".format(e))
            self.do_excel.write_result(row=data_namedtuple.case_id+1,
                                       actual=response.text,
                                       result=do_config("msg", "fail_result"))
            raise e
        else:
            self.do_excel.write_result(row=data_namedtuple.case_id+1,
                                       actual=response.text,
                                       result=do_config("msg", "success_result"))


if __name__ == '__main__':   # 空两行
    unittest.main()

