import pytest
@pytest.fixture()
def login():
    print('登录成功***')
    user = 'shen'
    pawd = 'gang'
    yield [user,pawd]
    print('退出登录')

class TestDemo:
    def test_1(self,login):
        print('需登录，test1....')
        print(f'拿到fixture值：{login[0]}')
        assert 1==1
        pass

    @pytest.mark.usefixtures('login')
    def test_2(self):
        print('无需登录，test2....')
        print(f'拿到fixture值：{login}')
        assert 1 == 1
        pass

    def test_4(self):
        print('无需登录，test4....')
        assert 1 == 1
        pass

if __name__ == '__main__':
    pytest.main(['test_fixture.py','-sq'])