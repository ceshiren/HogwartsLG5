import pytest


@pytest.mark.parametrize("a",[0,1,2])
@pytest.mark.parametrize("b",[2,3,4])
def test_foo(a,b):
    print("测试参数堆叠组合：a-->%s,b-->%s"%(a,b))