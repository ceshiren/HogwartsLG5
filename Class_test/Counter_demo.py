#定义一个计算器的类
class Counter:
    #实例初始化a、b的值
    # def __init__(self,a=1,b=1):
    #     self.a = a
    #     self.b = b

    #计算器的加法运算
    def add(self,a,b):
        return a + b

    #计算器的减法运算
    def minus(self,a,b):
        return a - b

    #计算器的成份运算
    def multiply(self,a,b):
        return a * b

    #计算器的除法运算
    def divide(self,a,b):
        if b == 0:
            return False
        return a / b

#测试
if __name__ == '__main__':
    t = Counter()
    print(t.add(2,1))
    print(t.minus(2,3))
    print(t.multiply(2,1))
    print(t.divide(2,0))
