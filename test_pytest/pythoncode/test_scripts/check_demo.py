def inc(x):
    return x + 1

# 修改ini文件,让check开头的也能识别
def check_answer():
    print("这是我得第一条测试用例")
    assert inc(3) == 4

def test_foo():
    print("这是我得第二条测试用例")
    assert inc(3) == 4