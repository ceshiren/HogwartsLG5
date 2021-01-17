# -*- coding: utf-8 -*-
# @Author : feier
# @File : test_assume.py
import pytest


def test_a():
    # assert 1 == 2
    # assert False == True
    # assert 100 == 200
    pytest.assume(1 == 2)
    pytest.assume(True == True)
    pytest.assume(100 == 200)