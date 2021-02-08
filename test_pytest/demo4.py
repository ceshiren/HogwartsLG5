import selenium
from selenium import webdriver

def test_demo():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")