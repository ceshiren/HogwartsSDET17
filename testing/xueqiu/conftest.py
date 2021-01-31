#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

import pytest


@pytest.fixture(scope='session')
def login():
    print("登录操作>>>>>>")
    name = "哈利波特"
    yield name  # yield 相当于return
    print("登出操作")
