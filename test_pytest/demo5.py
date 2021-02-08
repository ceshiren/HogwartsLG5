import pytest
import yaml

def step1():
    print("打开浏览器")

def step2():
    print("登录账号")

def step3():
    print("关闭浏览器")

def read_steps(path):
    with open(path) as f:
        steps = yaml.safe_load(f)
    if "step1" in steps:
        step1()
    if "step2" in steps:
        step2()
    if "step3" in steps:
        step3()

def test_foo():
    read_steps("test_pytest/steps.yaml")