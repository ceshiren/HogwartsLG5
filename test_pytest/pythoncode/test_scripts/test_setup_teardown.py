import pytest
'''
* 模块级的（setup_module、teardown_module）全局的，在模块执行前运行一遍，在模块执行后运行一遍
* 函数级的（setup_function、teardown_function）只对函数用例生效，而且不在类中使用
* 类级的（setup_class、teardown_class）在类中使用，类执行之前运行一次，类执行之后运行一次
* 类中方法级的（setup_method、teardown_method）在每一个方法之前执行一次，在每一个方法之后执行一次
* 单独使用（setup、teardown）其作用和setup_function、teardown_function/setup_method、teardown_method 一样

'''

def setup_module():
    print("\nsetup_module:整个test_setup_teardown.py模块开始前只执行一次")
def teardown_module():
    print("\nteardown_module:整个test_setup_teardown.py模块结束后只执行一次")

def setup_function():
    print("\nsetup_function:不在类中的用例执行前")

def teardown_function():
    print("\nteardown_function:不在类中的用例执行后")

def test_three():
    print("正在执行test three")

def test_four():
    print("正在执行test four")

class TestClass():

    def setup_class(self):
        print("\nsetup_class:所有用例执行前")
    def teardown_class(self):
        print("\nteardown_class:所有用例结束执行")

    def setup_method(self):
        print("\nsetup_method:每个用例开始前执行")
    def teardown_method(self):
        print("\nteardown_method:每个用例结束执行")

    def test_one(self):
        print("正在执行test one")
    def test_two(self):
        print("正在执行test two")