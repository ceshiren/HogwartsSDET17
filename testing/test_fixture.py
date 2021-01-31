#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture()
def login():
    print("登录操作")


@pytest.fixture()
def get_username():
    name = "赫敏"
    print(name)
    return name


def test_search():
    print("搜索")


@pytest.mark.usefixtures("login")
def test_cart():
    print("购物")


@pytest.mark.usefixtures("get_username")
@pytest.mark.usefixtures("login")
def test_order():
    print("下单")
