# 装饰器demo

# 原始的a函数
# def a():
#     print("a")

# 我想对a函数进行扩展，原始想法就是直接去修改a函数，比如修改后的如下
# 如果经常扩展，那么a就会无限膨胀（可以把a理解为一个py文件，对一个py文件进行扩展后会膨胀）
# 那么就需要解决方案，把扩展的内容移出来，这种解决方案就可以使用装饰器，避免a进行扩展
def a1():
    print("before a")
    print("a")
    print("after a")

# 装饰器解决方案步骤
# 第一步：声明一个新的函数b
# 第二步：把多余的扩展移出来放到函数b，然后在函数b里面调函数a
# 如下：但此时a还是原来的a，运行b才可以将扩展的功能实现，b实际是a的增强
# 如果我还是想调a来实现扩展的功能，但不想感知到b的存在，那么就会用到装饰器，
# 此时，b函数改写一些语法，此时改写成b1
def b():
    print("before a")
    a()
    print("after a")

# 在定义b1时的参数是传入一个函数
def b1(fun):
    # 在内部定义一个run函数，run可以改成其他名称，参数按下面的参数写
    def run(*args, **kwargs):
        # 扩展代码
        print("before a")
        # 调用fun函数，再传参
        fun(*args, **kwargs)
        # 扩展代码
        print("after a")
    # 最后一定要return run函数
    return run
# b1函数按照上面的语法写成后，就是一个装饰器，此时只需要在a函数上面增加@b1，那么a函数就可以调用b1扩展代码
# b1函数要写在a函数前面，上面的a函数被注释掉了
#
@b1
def a():
    print("a")


def test_demo():
    a()
