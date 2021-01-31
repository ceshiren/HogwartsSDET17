#!/usr/bin/env python
# -*- coding: utf-8 -*-
def test_search(login):
    print("搜索")


def test_cart(login):
    print(login)
    print("购物")


# @pytest.mark.usefixtures('login')
def test_order(login):
    print(login)
    print("下单")
