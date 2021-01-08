import json
from http import cookies
from time import sleep

from selenium import webdriver

class TestWeworkCookie():
    def setup_method(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address="127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)

    def test_cookie(self):
        cookies = self.driver.get_cookies()
        with open("cookie.json","r") as i:
            cookies = json.load(i)

    def test_weixin(self):
        self.driver.get("https://work.weixin.qq.com/")
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu_customer"]/span').click()

