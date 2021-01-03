#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/3 15:05
import pytest

def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')