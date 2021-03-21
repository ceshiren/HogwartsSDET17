"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""
import json

from mitmproxy import ctx, http


class AD:


    def request(self, flow: http.HTTPFlow):
        """
        使用request事件实现map local
        :param flow:
        :return:
        """
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            with open("/Users/lixu/project/hogwarts/HogwartsSDET17/test_mock/xueqiu.json", encoding="utf-8") as f:
                # 给flow.response属性进行赋值，
                # 赋值调用mitmproxy 响应对象的 make方法
                # 响应体在make函数里面所需要的数据为str
                flow.response = http.HTTPResponse.make(200,  # (optional) status code

                    f.read(),  # (optional) content
                    {"Content-Type": "text/html"}  # (optional) headers
                )

    def response(self, flow: http.HTTPFlow):
        pass


# addons 是mitmproxy 的强制要求的规范
# 一定要使用此变量名存放类的实例
addons = [
    AD()
]