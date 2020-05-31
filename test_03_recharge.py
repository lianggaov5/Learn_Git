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
import json

from libs.ddt import ddt, data
from scripts.handle_excel import HandleExcel
from scripts.handle_config import do_config
from scripts.handle_log import do_log
from scripts.handle_request import HandleRequest
from scripts.constants import TEST_DATAS_FILE_PATH
from scripts.handle_context import HandleContext
from scripts.handle_mysql import HandleMysql

# do_log = HandleLog().get_logger()


@ddt
class TestRecharge(unittest.TestCase):
    """
    测试充值功能
    """

    do_excel = HandleExcel(TEST_DATAS_FILE_PATH, "recharge")  # 类属性
    recharge_cases_list = do_excel.get_cases()    # 返回一个嵌套元组的列表

    @classmethod
    def setUpClass(cls) -> None:  # setUpClass是unittest框架的方法，会被unittest框架自动调用
        """
        在当前类中所有实例方法执行之前会被调用一次
        重写父类的类方法
        :return:
        """
        cls.send_request = HandleRequest()
        cls.handle_mysql = HandleMysql()
        do_log.info("\n\n{:=^40s}".format("开始执行充值功能用例"))

    @classmethod
    def tearDownClass(cls) -> None:
        """
        在当前类中所有实例方法执行结束之后会被调用一次
        :return:
        """
        do_log.info("\n{:=^40s}\n".format("充值功能用例执行结束"))
        cls.send_request.close()
        cls.handle_mysql.close()

    @data(*recharge_cases_list)
    def test_recharge(self, data_namedtuple):
        """
        测试充值功能
        :return:
        """
        do_log.info("\n正在运行的测试用例为：{}".format(data_namedtuple.title))
        method = data_namedtuple.method
        url = do_config("api", "url") + data_namedtuple.url
        new_data = HandleContext().recharge_parameterization(data_namedtuple.data)
        check_sql = data_namedtuple.check_sql

        # 充值之前用户的剩余金额
        if check_sql:
            check_sql = HandleContext().recharge_parameterization(check_sql)
            mysql_data = self.handle_mysql(sql=check_sql)  # 获取一条记录
            amount_before_recharge = float(mysql_data["LeaveAmount"])   # decimal类型数据转换成float类型
            amount_before_recharge = round(amount_before_recharge, 2)  # 保留两位小数

        response = self.send_request(method=method, url=url, data=new_data)

        # 判断服务器是否有异常
        try:
            self.assertEqual(200, response.status_code,
                             msg="测试【{}】失败，http请求状态码为【{}】".
                             format(data_namedtuple.title, response.status_code))
        except AssertionError as e:
            do_log.error("\n具体异常信息为：{}\n".format(e))
            raise e

        response = response.text  # 获取json格式数据
        # 将复杂的数据赋值为空，之后单独验证
        if check_sql:
            response = json.loads(response, encoding="utf8")
            response["data"] = None
            response = json.dumps(response, ensure_ascii=False)  # ensure_ascii为False,可将乱码转换成中文

        # 验证预期结果是否与实际结果相同
        try:
            self.assertEqual(data_namedtuple.expected,
                             response,
                             msg="测试{}失败".format(data_namedtuple.title))

            # 充值之后用户的剩余金额
            if check_sql:
                check_sql = HandleContext().recharge_parameterization(check_sql)
                mysql_data = self.handle_mysql(sql=check_sql)
                amount_after_recharge = float(mysql_data["LeaveAmount"])
                actual_amount = round(amount_after_recharge, 2)
                recharge_amount = float(json.loads(new_data, encoding="utf8").get("amount"))
                excepted_amount = round(amount_before_recharge+recharge_amount, 2)
                # 服务器返回复杂数据的验证，这里验证充值金额
                self.assertEqual(excepted_amount, actual_amount, msg="数据库中充值的金额有误")

        except AssertionError as e:
            do_log.error("\n具体异常信息为：{}\n".format(e))
            self.do_excel.write_result(row=data_namedtuple.case_id+1,
                                       actual=response,
                                       result=do_config("msg", "fail_result"))
            raise e
        else:
            self.do_excel.write_result(row=data_namedtuple.case_id+1,
                                       actual=response,
                                       result=do_config("msg", "success_result"))


if __name__ == '__main__':   # 空两行
    unittest.main()

