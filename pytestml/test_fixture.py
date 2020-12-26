import pytest


#创建一个登录的fixture方法
@pytest.fixture()
def login():
    print("登录操作")
    print("获取token")
    username = 'tom'
    password = '123456'
    token = "token123456"
    yield [username,password,token]
    print("登出操作")

#测试用例1：需要提前登录
def test_case1(login):
    print(f"login userneme ")