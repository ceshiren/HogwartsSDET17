#!/usr/bin/env python
# -*- coding: utf-8 -*-
# conftest.py 文件名字是固定的，不能改
import datetime

import pytest


@pytest.fixture(scope='session')
def login():
    print("登录操作>>>>>>")
    token = datetime.datetime.now()
    yield token  # yield 相当于return
    print("登出操作")
