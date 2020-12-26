import pytest
import yaml
def add_function(a,b):
    return a+b

#参数化:需要传递两个参数,第一个参数传递需要传输的值的格式（方法定义的参数）；第二个传递一个list，然后其中参数以list或者元祖进行传递；ids=：别名的设置
# @pytest.mark.parametrize("a,b,expected",[[1,1,2],[-1,-2,-3],[1000,1000,2000]],ids=['int','minus','bigint'])
# def test_add(a,b,expected):
#     assert add_function(a,b) == expected
#
#参数化堆叠使用

# @pytest.mark.parametrize("a",[0,1],ids=['OA','OB'])
# @pytest.mark.parametrize("b",[2,3],ids=['TE','TA'])
# def test_foo(a,b):
#     print(f'测试参数堆叠组合：a-->{a},b-->{b}')


#参数化:通过读文件的方式进行参数化
#方式一：
# @pytest.mark.parametrize("a,b,expected",yaml.safe_load(open('data.yml'))['datas'],ids=yaml.safe_load(open('data.yml'))['myids'])
# def test_add(a,b,expected):
#     assert add_function(a,b) == expected
#
#方式二：
def get_data():
    with open('data.yml') as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_data = datas['datas']
        add_ids = datas['myids']
    return [add_ids,add_data]

@pytest.mark.parametrize("a,b,expected",get_data()[1],ids=get_data()[0])
def test_add(a,b,expected):
    assert add_function(a,b) == expected