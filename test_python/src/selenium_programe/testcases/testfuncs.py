import os
path = os.path.abspath(__file__).split("\\")
path2 = os.path.dirname(__file__).strip("testcase").__add__("data/cookie.json")
print(path)
print(path2)