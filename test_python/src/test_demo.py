import pytest
import selenium
from selenium import webdriver

drive = webdriver.Chrome()
drive.get("http://www.baidu.com")
# def add(a,b):
#     return a+b
#
# class TestDemo:
#     @pytest.mark.one
#     def test_mark(self):
#         assert  add(1,2) == 3