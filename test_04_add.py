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
class TestAdd(unittest.TestCase):
    """
    测试加标功能
    """
    do_excel = HandleExcel(TEST_DATAS_FILE_PATH, "add")  # 类属性
    cases_list = do_excel.get_cases()    # 获取表单中所有的用例，返回一个嵌套元组的列表

    @classmethod
    def setUpClass(cls):  # setUpClass是unittest框架的方法，会被unittest框架自动调用
        """
        在当前类中所有实例方法执行之前会被调用一次
        重写父类的类方法
        :return:
        """
        cls.send_request = HandleRequest()
        do_log.info("\n\n{:=^40s}".format("开始执行加标功能用例"))

    @classmethod
    def tearDownClass(cls):
        """
        在当前类中所有实例方法执行结束之后会被调用一次
        :return:
        """
        do_log.info("\n{:=^40s}\n".format("加标功能用例执行结束"))
        cls.send_request.close()

    @data(*cases_list)
    def test_add(self, data_namedtuple):
        """
        测试加标功能
        :return:
        """
        url = do_config("api", "url") + data_namedtuple.url
        new_data = HandleContext().add_parameterization(data_namedtuple.data)
        print(new_data)
        do_log.info("\n正在运行的测试用例为：{}".format(data_namedtuple.title))
        # 接口不支持json格式，只支持form表单，is_json=False, 使用data
        response = self.send_request(method=data_namedtuple.method, url=url, data=new_data)
        print(response.text)

        # 判断服务器是否有异常
        try:
            self.assertEqual(200, response.status_code,
                             msg="测试【{}】失败，请求状态码为【{}】"
                             .format(data_namedtuple.title, response.status_code))
        except AssertionError as e :  # 出现异常，后面代码不会执行
            do_log.error("{},执行结果:{}\n具体异常信息:{}\n".format(data_namedtuple.title, "fail", e))
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

