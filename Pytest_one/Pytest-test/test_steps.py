import yaml


def step1():
    print('\n打开浏览器')
def step2():
    print('输入账号/密码')
def step3():
    print('登录！')

def steps(path):
    with open(path) as f:
        steps = yaml.safe_load(f)
    if "step1" in steps:
        step1()
    if "step2" in steps:
        step2()
    if "step3" in steps:
        step3()
def test_foo():
    steps('steps.yml')