import os
import time
import selenium

# print(os.getcwd())
# print(time.time())
def func1(a):
    """
    函数func1的作用，给程序员看的
    :param a:
    :return:
    """
    print("这是一个函数")
    print("这是一个参数a",a)

def func2(a,b,c,d):
    print("参数a的值为：",a)

func3 = lambda x,y: x*2+y

#函数的调用
# func1('哈哈')
# func2(10,b=1,c=3,d=9)
print(func3(4,7))