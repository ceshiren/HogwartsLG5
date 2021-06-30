def b(fun_123455):
    def run_1244215(*args, **kwargs):
        print("before a")
        fun_123455(*args, **kwargs)
        print("after a")
    return run_1244215

@b
def a():
    print('a')


def test_demo():
    a()
