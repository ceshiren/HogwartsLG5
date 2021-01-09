import yaml


def step1():
    print("打开浏览器")
def step2():
    print("注册新账号")
def step3():
    print("登录")

# 使用steps函数集中处理步骤,对读出的文件内容,不同的步骤调用不同的函数
def steps(path):
    with open(path) as f:
        steps = yaml.safe_load(f)
        print(steps)
    if "step1" in steps:
        step1()
    if "step2" in steps:
        step2()
    if "step3" in steps:
        step3()

def test_foo():
    # 当步骤变化的时候,只用修改steps.yml文件
    steps("./steps.yml")