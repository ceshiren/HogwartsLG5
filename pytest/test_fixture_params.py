import pytest
@pytest.fixture(scope='class',params=[1,2,3],ids=['a','b','c'])
def login1(request):
    data = request.param
    print(f'获取params数据:{data}')
    return data
class TestDemo:
    def test_1(self,login1):
        print(f'打印{login1}')
        assert 1==1
        pass


if __name__ == '__main__':
    pytest.main(['test_fixture_params.py','-sv'])