# -*- coding: utf-8 -*-
# @Author : feier
# @File : test_demo1.py
import pytest


@pytest.fixture()
def connectDB():
    print("test_demo1 下的 connectDB")

def test_a(connectDB):
    print("sub_demo test_a")

class TestB:
    def test_b(self):
        print("sub_demo test_b")