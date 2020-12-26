import pytest


@pytest.fixtrue(params=[1,2,3])
def login1(request):
    data = request.param
    print("获取测试数据")
    return data + 4

def test_case1(login1):
    print(login1)
    print("测试用例1")
