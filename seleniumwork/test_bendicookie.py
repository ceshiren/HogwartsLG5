import json
from http import cookies
from time import sleep

from selenium import webdriver

class TestWeworkCookie():
    def setup_method(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address="127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def test_cookie(self):
        self.driver.get("https://work.weixin.qq.com/")
        with open("cookie.json","r") as i:
            cookies = json.load(i)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="menu_customer"]/span').click()

