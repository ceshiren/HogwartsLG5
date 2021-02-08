import pytest


def func(x):
    return x + 1

@pytest.mark.parametrize('a,b',[(1,2),(10,20),('a','a1'),(3,4),(5,6)])
def test_answer(a,b):
    assert func(a) == b

def test_answer1():
    assert func(3) == 4

@pytest.fixture()
def login():
    username = 'Jerry'
    return username

class TestDemo:
    def test_a(self,login):
        print(f'a  username = {login}')

    def test_b(self):
        print('b')

if __name__ == "__main__":
    pytest.main(['demo1.py'])