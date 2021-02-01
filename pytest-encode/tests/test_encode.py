#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parametrize('name', ['哈利', '赫敏'])
def test_encode(name):
    print(name)
