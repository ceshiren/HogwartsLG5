import pytest

@pytest.fixture(scope="session")
def login():
    print("登录操作")
    print("获取token")
    username = "xiulanyue"
    password = "123456"
    token = "qdfdsfgg"
    yield [username,password,token]
    print("退出登录操作")

def test_login(login):
    print(f"username and password:{login}")
    print("我是第一条测试用例")

