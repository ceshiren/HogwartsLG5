def inc(x):
    return x + 1

def test_answer():
    print('这是我的第一个用例！')
    assert inc(3) == 4

def test_demo():
    print('这是我的第一个用例！')
    assert inc(3) == 4

def test_foo():
    print('这是我的第一个用例！')
    assert inc(3) == 4


#命名不对，不运行
def check_ansewer():
    assert inc(3) ==  4