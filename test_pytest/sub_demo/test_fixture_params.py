
import pytest

@pytest.fixture(params=[1,2,3])
def login(request):
    print(request.param)
    print("获取测试数据")

def test_login(login):
    print("执行测试用例1")