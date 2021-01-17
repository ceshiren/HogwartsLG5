# -*- coding: utf-8 -*-
# @Author : feier
# @File : test_fixture.py
import pytest
# fixture 是 pytest 的一个外壳函数，可以模拟setup和teardown的操作
# yield 之前的操作相当于 setup，yield 之后的操作相当于teardown
# yield 相当于 return，如果需要返回数据的话，直接放在 yield 后面

# 创建一个登录的fixture方法
@pytest.fixture()
def login():
    print("登录操作")
    print("获取token")
    username = "tom"
    password = "123456"
    token = "token123456"
    yield [username, password, token]
    print("登出操作")

# 测试用例1：需要提前登录
def test_case1(login):
    print(f"login username and password:{login}")
    print("测试用例1")

# 测试用例2：不需要提前登录
def test_case2(connectDB):
    print("测试用例2")

# 测试用例3：需要提前登录
def test_case3():
    print("测试用例3")

# 测试用例4：需要提前登录
# @pytest.mark.usefixtures("login")
def test_case4():
    print("测试用例4")