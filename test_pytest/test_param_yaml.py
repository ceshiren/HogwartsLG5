import pytest
import yaml
def get_datas():
    # 打开文件
    with open("./data.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        # 获取文件中key为datas的数据
        add_datas = datas["datas"]
        # 获取文件中key为myids的数据
        add_ids = datas["myids"]
        return [add_datas,add_ids]

def add_function(a,b):
    return a+b
# @pytest.mark.parametrize("参数名",列表数据)
# 参数名：作为测试用例的参数. 字符串格式，多个参数中间用逗号隔开。
# 列表数据：一组测试数据。list格式，多组数据用元组类型，
# list的每个元素都是一个元组，元组里的每个元素和按参数顺序一一对应。
# 可以添加ids参数指定用例说明(别名)。
#get_datas()[0]取返回列表[add_datas,add_ids]的第一个元素
@pytest.mark.parametrize("a,b,expected",get_datas()[0],
                         ids=get_datas()[1])
def test_add(a,b,expected):
    assert add_function(a,b) == expected