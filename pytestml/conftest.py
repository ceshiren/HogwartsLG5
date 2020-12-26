import pytest


@pytest.fixture(scope="module")
def connectDB():
    print("连接数据库操作")
    yield
    print("断开数据库操作")