#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import pytest
import yaml

sys.path.append('..')
print(sys.path)
from pythoncode.Calculator import Calculator


def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    return (datas['add']['datas'], datas['add']['ids'])


# yaml json excel csv xml
# 测试类
class TestCalc:
    datas: list = get_datas()

    # 前置条件
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    # 后置条件
    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a, b, result", datas[0], ids=datas[1])
    def test_add(self, a, b, result):
        print(f"a={a} , b ={b} ,result={result}")
        assert result == self.calc.add(a, b)

    def test_add1(self):
        datas = [[1, 1, 2], [100, 400, 300], [1, 0, 1]]
        for data in datas:
            print(data)
            assert data[2] == self.calc.add(data[0], data[1])

    # TODO: 完善相加功能
    # TODO: 相除功能
    def test_div(self):
        pass
