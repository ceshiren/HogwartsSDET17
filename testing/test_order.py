#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.mark.second
def test_foo():
    assert True


@pytest.mark.first
def test_bar():
    assert True
