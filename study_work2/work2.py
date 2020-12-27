class Demo():
    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    def divi(self,a,b):
        return a/b

if __name__ == '__main__':
    demo = Demo()
    res1 = demo.add(4, 2)
    res2 = demo.sub(4, 2)
    res3 = demo.mul(4, 2)
    res4 = demo.divi(4, 2)
    exp = 2
    assert res4 == exp