import pytest

def add_function(a,b):
    return a+b

# @pytest.mark.parametrize("参数名",列表数据)
# 参数名：作为测试用例的参数. 字符串格式，多个参数中间用逗号隔开。
# 列表数据：一组测试数据。list格式，多组数据用元组类型，
# list的每个元素都是一个元组，元组里的每个元素和按参数顺序一一对应。
# 可以添加ids参数指定用例说明(别名)。
@pytest.mark.parametrize("a,b,expected",[(3,3,6),(-1,-2,-3),(1000,1000,2000)],ids=["int","minus","bigint"])
def test_add(a,b,expected):
    assert add_function(a,b) == expected