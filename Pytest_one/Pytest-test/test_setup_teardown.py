import pytest
#模块级别
def setup_module():
    print('\nsetup_module:整个test_setup_teardown.py模块开始前执行一次！')
def teardown_module():
    print('\nteardown_module:整个test_setup_teardown.py模块结束后执行一次！')

#函数级别（不包含在类中的用例）
def setup_function():
    print('\n setup_function:不在类中的用例执行前')
def teardown_function():
    print('\n teardown_function:不在类中的用例执行后！')

def test_three():
    print('正在执行test three！')

def test_four():
    print('正在执行test four！')

class TestClass():
    def setup_class(self):
        print('\nsetup_class:所有用例执行前，执行！')
    def teardown_class(self):
        print('\nteardown_class:所有用例结束后，执行！')

    def setup_method(self):
        print('\nsetup_method:每个用例开始前执行')
    def teardown_method(self):
        print('\nteardown_method:每个用例结束后执行！')
    def test_one(self):
        print('正在执行test_one')

    def test_two(self):
        print('正在执行test_two')

