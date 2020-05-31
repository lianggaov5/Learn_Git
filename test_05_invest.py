# -*- coding: utf-8 -*-
"""
********************************
@Time     :2019/9/29 2:11
@Author   :gaoliang
@Email    :337901080@qq.com
@File     :test_05_invest.py
@Software :PyCharm
********************************
"""
# 接口之间的依赖  获得loan_id
# 问题：使用全局变量：1.多次导入相同的模块，只有第一次有效，不能实时更新，2.循环导入
# 解决：使用反射
import unittest    # 单元测试框架
import json

from libs.ddt import ddt, data
from scripts.handle_excel import HandleExcel
from scripts.handle_config import do_config
from scripts.handle_log import do_log
from scripts.handle_request import HandleRequest
from scripts.constants import TEST_DATAS_FILE_PATH
from scripts.handle_context import HandleContext
from scripts.handle_mysql import HandleMysql


@ddt
class TestInvest(unittest.TestCase):
    """
    测试投资功能
    """

    do_excel = HandleExcel(TEST_DATAS_FILE_PATH, "invest")  # 类属性
    cases_list = do_excel.get_cases()    # 返回一个嵌套元组的列表

    @classmethod
    def setUpClass(cls) -> None:  # setUpClass是unittest框架的方法，会被unittest框架自动调用
        """
        在当前类中所有实例方法执行之前会被调用一次
        重写父类的类方法
        :return:
        """
        cls.send_request = HandleRequest()
        cls.handle_mysql = HandleMysql()
        do_log.info("\n\n{:=^40s}".format("开始执行投资功能用例"))

    @classmethod
    def tearDownClass(cls) -> None:
        """
        在当前类中所有实例方法执行结束之后会被调用一次
        :return:
        """
        do_log.info("\n{:=^40s}\n".format("投资功能用例执行结束"))
        cls.send_request.close()
        cls.handle_mysql.close()

    @data(*cases_list)
    def test_invest(self, data_namedtuple):
        """
        测试投资功能
        :return:
        """
        do_log.info("\n正在运行的测试用例为：{}".format(data_namedtuple.title))
        method = data_namedtuple.method
        url = do_config("api", "url") + data_namedtuple.url
        print(url)
        new_data = HandleContext().invest_parameterization(data_namedtuple.data)
        print(new_data)
        response = self.send_request(method=method, url=url, data=new_data)
        print(response.text)
        # 判断服务器是否有异常
        try:
            self.assertEqual(200, response.status_code,
                             msg="测试【{}】失败，http请求状态码为【{}】".
                             format(data_namedtuple.title, response.status_code))
        except AssertionError as e:
            do_log.error("\n具体异常信息为：{}\n".format(e))
            raise e

        # 判断是否加标成功，加标成功，获取loan_id
        if response.json().get("msg") == "加标成功":
            check_sql = data_namedtuple.check_sql
            if check_sql:
                check_sql = HandleContext().invest_parameterization(check_sql)
                mysql_data = self.handle_mysql(sql=check_sql)  # 获取一条记录
                HandleContext.loan_id = mysql_data["Id"]  # 动态添加属性,获取标的Id
                # setattr(HandleContext, "loan_id", mysql_data["Id"])   # 动态创建类属性,获取标的Id

        # 验证预期结果是否与实际结果相同
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

