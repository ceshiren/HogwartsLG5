class TestDemo:
    def test_demo(self):
        s = {'a', 'b', 'c'}
        s2 = {'a', 'c', 'd'}
        print(s - s2)  # 差集  在s里 不在s2里
        print(s | s2)  # 并集
        print(s & s2)  # 交集
        print(s ^ s2)  # s和s2不同时存在的元素

        res = 1.233333
        print(type(res))
        if isinstance(res, float):
            res = round(res, 2)
        print(res)

        str = '[1,2]'
        print(type(eval(str)))
