#!/usr/bin/env python
# -*- coding: utf-8 -*-
# conftest.py 文件名字是固定的，不能改
import datetime
from typing import List

import pytest


@pytest.fixture(scope='session')
def login():
    print("登录操作>>>>>>")
    token = datetime.datetime.now()
    yield token  # yield 相当于return
    print("登出操作")


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        if 'add' in item._nodeid:
            item.add_marker(pytest.mark.add)

    items.reverse()
