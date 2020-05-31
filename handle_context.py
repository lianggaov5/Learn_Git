# -*- coding: utf-8 -*-
"""
********************************
@Time     :2019/9/18 23:20
@Author   :gaoliang
@Email    :337901080@qq.com
@File     :handle_context.py
@Software :PyCharm
********************************
"""
import re
from scripts.handle_mysql import HandleMysql
from scripts.handle_config import HandleConfig
from scripts.constants import USER_ACCOUNTS_FILE_PATH


class HandleContext:
    """
    处理excel中参数化的数据，反射（动态添加属性，实时更新）
    """
    not_existed_tel_pattern = re.compile(r"\$\{not_existed_tel\}")  # 配置${not_existed_tel} 的正则表达式
    invest_user_tel_pattern = re.compile(r"\$\{invest_user_tel\}")  # 配置${invest_user_tel} 的正则表达式
    invest_user_pwd_pattern = re.compile(r"\$\{invest_user_pwd\}")  # 配置${invest_user_pwd} 的正则表达式
    admin_user_tel_pattern = re.compile(r"\$\{admin_user_tel\}")
    admin_user_pwd_pattern = re.compile(r"\$\{admin_user_pwd\}")  # 配置${admin_user_pwd} 的正则表达式

    borrow_user_id_pattern = re.compile(r"\$\{borrow_user_id\}")
    not_existed_borrow_user_id_pattern = re.compile(r"\$\{not_existed_borrow_user_id\}")
    invest_user_id_pattern = re.compile(r"\$\{invest_user_id\}")
    not_existed_invest_user_id_pattern = re.compile(r"\$\{not_existed_invest_user_id\}")
    loan_id_pattern = re.compile(r"\$\{loan_id\}")  # 配置${loan_id} 的正则表达式
    not_existed_loan_id_pattern = re.compile(r"\$\{not_existed_loan_id\}")

    @classmethod
    def not_existed_tel_replace(cls, data):
        """
        替换参数化的未注册手机号
        :param data:
        :return:
        """
        do_mysql = HandleMysql()
        new_mobile = do_mysql.create_not_existed_tel()
        if re.search(cls.not_existed_tel_pattern, data):
            data = re.sub(cls.not_existed_tel_pattern, new_mobile, data)

        do_mysql.close()  # 关闭数据库连接
        return data

    @classmethod
    def invest_user_tel_pwd_replace(cls, data):
        """
        替换参数化的投资人手机号
        :param data:
        :return:
        """
        do_config = HandleConfig(USER_ACCOUNTS_FILE_PATH)
        invest_user_tel = do_config("invest_user", "mobilephone")
        # 替换手机号
        if re.search(cls.invest_user_tel_pattern, data):
            # sub函数中第二个和第三个参数一定要为字符串类型
            data = re.sub(cls.invest_user_tel_pattern, str(invest_user_tel), data)
        # 替换密码
        if re.search(cls.invest_user_pwd_pattern, data):
            data = re.sub(cls.invest_user_pwd_pattern, do_config("invest_user", "pwd"), data)

        return data

    @classmethod
    def admin_user_tel_pwd_replace(cls, data):
        """
        替换参数化的管理人手机号
        :param data:
        :return:
        """
        do_config = HandleConfig(USER_ACCOUNTS_FILE_PATH)
        admin_user_tel = do_config("admin_user", "mobilephone")
        # 替换手机号
        if re.search(cls.admin_user_tel_pattern, data):
            # sub函数中第二个和第三个参数一定要为字符串类型
            data = re.sub(cls.admin_user_tel_pattern, str(admin_user_tel), data)
        # 替换密码
        if re.search(cls.admin_user_pwd_pattern, data):
            data = re.sub(cls.admin_user_pwd_pattern, do_config("admin_user", "pwd"), data)

        return data

    @classmethod
    def borrow_user_id_replace(cls, data):
        """
        替换参数化的借款用户id
        :param data:
        :return:
        """
        do_config = HandleConfig(USER_ACCOUNTS_FILE_PATH)
        borrow_user_id = do_config("borrow_user", "id")
        if re.search(cls.borrow_user_id_pattern, data):
            data = re.sub(cls.borrow_user_id_pattern, str(borrow_user_id), data)

        if re.search(cls.not_existed_borrow_user_id_pattern, data):
            handle_mysql = HandleMysql()
            sql = "SELECT MAX(Id) AS max_id FROM member;"
            cls.not_existed_user_id = str(handle_mysql(sql)["Id"]+800)
            data = re.sub(cls.not_existed_borrow_user_id_pattern,
                          cls.not_existed_user_id,
                          data)

        return data

    @classmethod
    def invest_user_id_replace(cls, data):
        """
        替换参数化的投资用户id
        :param data:
        :return:
        """
        do_config = HandleConfig(USER_ACCOUNTS_FILE_PATH)
        invest_user_id = do_config("invest_user", "id")
        if re.search(cls.invest_user_id_pattern, data):
            data = re.sub(cls.invest_user_id_pattern, str(invest_user_id), data)

        if re.search(cls.not_existed_invest_user_id_pattern, data):
            handle_mysql = HandleMysql()
            sql = "SELECT MAX(Id) AS max_id FROM member;"
            cls.not_existed_user_id = str(handle_mysql(sql)["Id"]+1000)
            data = re.sub(cls.not_existed_invest_user_id_pattern,
                          cls.not_existed_user_id,
                          data)
        return data

    @classmethod
    def loan_id_replace(cls, data):
        """
        替换参数化的loan_id
        :param data:
        :return:
        """
        # 替换存在的loan_id
        if re.search(cls.loan_id_pattern, data):
            # getattr(对象, 字符类型的属性名)
            # setattr(对象, 字符类型的属性名, 属性值)
            # 类似java中的反射概念
            loan_id = getattr(cls, "loan_id")
            data = re.sub(cls.loan_id_pattern, str(loan_id), data)

        # 替换不存在的loan_id
        if re.search(cls.not_existed_loan_id_pattern, data):
            handle_mysql = HandleMysql()
            sql = "SELECT MAX(Id) AS max_loan_id FROM loan;"  # 获取loan表中最大的Id，并重命名为max_loan_id
            cls.not_existed_loan_id = str(handle_mysql(sql)["max_loan_id"]+1000)
            data = re.sub(cls.not_existed_loan_id_pattern, cls.not_existed_loan_id, data)
            handle_mysql.close()

        return data

    @classmethod
    def register_parameterization(cls, data):
        """
        实现注册功能的参数化
        :param data:
        :return:
        """
        data = cls.invest_user_tel_pwd_replace(data)
        data = cls.not_existed_tel_replace(data)

        return data

    @classmethod
    def login_parameterization(cls, data):
        """
        实现登录功能的参数化
        :param data:
        :return:
        """
        data = cls.not_existed_tel_replace(data)
        data = cls.invest_user_tel_pwd_replace(data)

        return data

    @classmethod
    def recharge_parameterization(cls, data):
        """
        实现充值功能的参数化
        :param data:
        :return:
        """
        data = cls.not_existed_tel_replace(data)
        data = cls.invest_user_tel_pwd_replace(data)

        return data

    @classmethod
    def add_parameterization(cls, data):
        """
        实现加标功能的参数化
        :param data:
        :return:
        """
        data = cls.admin_user_tel_pwd_replace(data)
        data = cls.borrow_user_id_replace(data)

        return data

    @classmethod
    def invest_parameterization(cls, data):
        """
        实现投资功能的参数化
        :param data:
        :return:
        """
        data = cls.admin_user_tel_pwd_replace(data)  # 替换管理员的手机号和密码
        data = cls.borrow_user_id_replace(data)  # 替换借款用户的id
        data = cls.loan_id_replace(data)         # 替换标的id
        data = cls.invest_user_tel_pwd_replace(data)  # 替换投资用户的手机号和密码
        data = cls.invest_user_id_replace(data)   # 替换投资用户的id
        data = cls.not_existed_tel_replace(data)  # 替换未注册的手机号

        return data


do_context = HandleContext()

if __name__ == '__main__':
    target_str1 = '{"mobilephone": "${not_existed_tel}", "pwd":"123456"}'
    target_str2 = '{"mobilephone": "${invest_user_tel}", "pwd":"123456"}'
    target_str3 = '{"mobilephone": "${admin_user_tel}", "pwd":"123456"}'
    target_str4 = '{"memberId":"${invest_user_id}", "title":"买手机", "amount": 1000, "loanRate": 10.0, ' \
                  '"loanTerm":6, "loanDateType":0, "repaymemtWay":4, "biddingDays":7 }'
    target_str5 = '{"memberId":"${borrow_user_id}", "title":"买手机", "amount": 1000, "loanRate": 10.0, ' \
                  '"loanTerm":6, "loanDateType":0, "repaymemtWay":4, "biddingDays":7 }'
    do_context = HandleContext()
    HandleContext.loan_id = 3
    new_data1 = do_context.not_existed_tel_replace(target_str1)
    new_data2 = do_context.invest_user_tel_pwd_replace(target_str2)
    new_data3 = do_context.admin_user_tel_pwd_replace(target_str3)
    new_data4 = do_context.invest_user_id_replace(target_str4)
    new_data5 = do_context.add_parameterization(target_str5)
    pass