#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import pytest
import yaml

sys.path.append('..')
print(sys.path)
from pythoncode.Calculator import Calculator


def get_datas(name, type='int'):
    with open("./datas/calc.yml") as f:
        all_datas = yaml.safe_load(f)
    datas = all_datas[name][type]['datas']
    ids = all_datas[name][type]['ids']
    return (datas, ids)


# yaml json excel csv xml
# 测试类
class TestCalc:
    # datas: list = get_datas()
    add_int_data = get_datas('add', 'int')
    div_int_data = get_datas('div', 'int_error')

    # 前置条件
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    # 后置条件
    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a, b, result", add_int_data[0], ids=add_int_data[1])
    def test_add(self, a, b, result):
        print(f"a={a} , b ={b} ,result={result}")
        assert result == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,result", [
        [0.1, 0.1, 0.2],
        [0.1, 0.2, 0.3]
    ])
    def test_add_float(self, a, b, result):
        assert result == round(self.calc.add(a, b), 2)

    # TODO: 完善相加功能
    # TODO: 相除功能
    @pytest.mark.parametrize("a, b, result", div_int_data[0], ids=div_int_data[1])
    def test_div_0(self, a, b, result):
        with pytest.raises(ZeroDivisionError, TypeError):
            result = a / b
