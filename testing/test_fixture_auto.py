#!/usr/bin/env python
# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

import pytest


@pytest.fixture()
def login():
    print("登录操作")
    token = datetime.datetime.now()
    yield token  # yield 相当于return
    print("登出操作")


@pytest.fixture()
def get_username(login):
    print(login)
    name = "赫敏"
    print(name)
    return name


def test_search(get_username):
    print("搜索")


def test_cart():
    print("购物")


def test_order():
    print("下单")
