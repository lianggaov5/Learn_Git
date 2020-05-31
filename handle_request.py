# -*- coding: utf-8 -*-
"""
********************************
@Time     :2019/9/9 18:59
@Author   :gaoliang
@Email    :337901080@qq.com
@File     :handle_request.py
@Software :PyCharm
********************************
"""
import json
import requests

from scripts.handle_log import do_log
from scripts.handle_config import HandleConfig
from scripts.constants import CONFIGS_FILE_PATH


class HandleRequest:
    """
    封装处理请求的类
    """
    def __init__(self):
        # 创建一个对象属性one_session，返回一个Session对象
        self.one_session = requests.Session()

    def __call__(self, method, url, data=None, is_json=False, **kwargs):

        method = method.lower()
        if isinstance(data, str):
            try:
                data = json.loads(data)      # 考虑到'{"name": null}'和'{"name": None}'
            except Exception as e:
                do_log.error(e)
                data = eval(data)

        if method == "get":
            res = self.one_session.request(method=method, url=url, params=data, **kwargs)
        elif method == "post":
            if is_json:  # 如果是json格式数据
                res = self.one_session.request(method=method, url=url, json=data, **kwargs)
            else:
                res = self.one_session.request(method=method, url=url, data=data, **kwargs)
        else:
            do_log.error("不支持的请求方法")
            return None
        return res

    def close(self):
        self.one_session.close()    # 只是做了资源回收，并没有中断回话


send_request = HandleRequest()


if __name__ == '__main__':
    # 1.构造url
    do_config = HandleConfig(CONFIGS_FILE_PATH)
    # register_url = "http://192.168.65.128:8080/futureloan/mvc/api/member/register"
    register_url = do_config("api", "url")+"/member/register"
    login_url = "http://test.lemonban.com:8080/futureloan/mvc/api/member/login"
    recharge_url = "http://test.lemonban.com:8080/futureloan/mvc/api/member/recharge"

    # 2.创建请求参数
    register_params = {
        "mobilephone": "13652168740",
        "pwd": "123456"
    }

    login_params = {
        "mobilephone": "13652168740",
        "pwd": "123456"
    }

    recharge_params = {
        "mobilephone": "13652168740",
        "amount": 1000
    }
    do_request = HandleRequest()
    response = do_request(method="post", url=register_url, data=register_params)
    print(response.text)
    # do_request(method="post", url=login_url, data=login_params)
    # do_request(method="post", url=recharge_url, data=recharge_params)
    do_request.close()
    pass


