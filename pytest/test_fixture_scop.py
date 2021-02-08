import pytest

class TestDemo:
    def test_1(self,login):
        print('需登录，test1....')
        print(f'拿到fixture值：{login}')
        assert 1==1
        pass

    def test_2(self,login):
        print('无需登录，test2....')
        assert 1 == 1
        pass

class TestDemo2:
    def test_1(self,login):
        print('需登录，test1....')
        print(f'拿到fixture值：{login}')
        assert 1==1
        pass

    def test_2(self,login):
        print('无需登录，test2....')
        assert 1 == 1
        pass

if __name__ == '__main__':
    pytest.main(['test_fixture_scop.py','-sq'])