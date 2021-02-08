import pytest
def setup_module():
    print('***********模块级别')
def teardown_module():
    print('***********模块级别')

def setup_function():
    print('waimian用例前执行')


def teardown_function():
    print('waimian用例结束后执行')

def test3():
    print('执行test3.......')

def test4():
    print('执行test4.......')

class TestClass:
    def setup_class(self):
        print('用例前执行')

    def teardown_class(self):
        print('用例结束后执行')

    def setup_method(self):
        print('每个用例前执行')

    def teardown_method(self):
        print('每个用例结束后执行')

    def test1(self):
        print('执行test1.......')

    def test2(self):
        print('执行test2.......')

if __name__ == '__main__':
    pytest.main(['test_py.py','-sq'])