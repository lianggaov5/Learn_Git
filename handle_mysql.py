# -*- coding: utf-8 -*-
"""
********************************
@Time     :2019/9/10 17:35
@Author   :gaoliang
@Email    :337901080@qq.com
@File     :handle_mysql.py
@Software :PyCharm
********************************
"""
import random
import pymysql

from scripts.handle_config import do_config


class HandleMysql:
    """
    处理mysql
    """
    def __init__(self):
        self.conn = pymysql.connect(host=do_config("mysql", "host"),
                                    user=do_config("mysql", "user"),
                                    password=do_config("mysql", "password"),
                                    port=do_config("mysql", "port"),
                                    db=do_config("mysql", "db"),
                                    charset=do_config("mysql", "charset"),
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def __call__(self, sql, args=None, is_more=False):
        """

        :param sql:sql语句
        :param args:sql语句的类型，序列类型  元组或列表
        :param is_more:如果为True，获取多个值，如果为False,获取单个值， 默认为False
        :return:字典类型或者嵌套字典的列表
        """
        self.cursor.execute(sql, args)
        self.conn.commit()

        if is_more:
            result = self.cursor.fetchall()
        else:
            result = self.cursor.fetchone()
        return result

    def close(self):
        """
        先关闭游标，再关闭连接
        :return:
        """
        self.cursor.close()
        self.conn.close()

    @staticmethod
    def create_tel():
        """
        生成11位随机手机号
        思路：前三位：手机号段组成一个字符串列表，再随机取出其中一个，
            后八位：数字0-9组成一个8位的随机字符串，之后拼接
        :return:
        """
        start_num_list = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                          "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                          "186", "187", "188", "189"]
        start_num = random.choice(start_num_list)
        end_num_str = "0123456789"
        end_num = ''.join(random.sample(end_num_str, 8))

        return start_num+end_num

    def is_existed_tel(self, mobile):
        """
        判断给定的手机号在数据库中是否存在
        思路：条件判断手机号是否在数据库中，为真，返回True，为假，返回False
        :param mobile:
        :return:
        """
        sql = "SELECT MobilePhone FROM member WHERE MobilePhone=%s;"
        if self(sql, args=(mobile,)):
            return True
        else:
            return False

    def create_not_existed_tel(self):
        """
        创建不存在的手机号
        思路：使用循环判断，存在，继续循环，不存在，跳出循环
        :return:
        """
        while True:
            one_mobile = self.create_tel()
            if not self.is_existed_tel(one_mobile):
                break

        return one_mobile


do_mysql = HandleMysql()

if __name__ == '__main__':
    sql1 = "SELECT * FROM `member` LIMIT 0, 10"
    sql2 = "SELECT Id FROM `member` WHERE LeaveAmount > %s LIMIT 0, 10;"

    do_mysql = HandleMysql()
    # print(do_mysql(sql=sql1, is_more=True))
    # print(do_mysql(sql=sql2, args=(600, ), is_more=True))
    # print(do_mysql(sql=sql1)["LeaveAmount"])
    # do_mysql.close()
    print(do_mysql.create_not_existed_tel())

