from time import sleep

import pytest
from selenium import webdriver
import json
from selenium.webdriver.common.by import By

class TestWork():
    def setup_method(self):
        # chrome --remote-debugging-port=9222，打开前关闭所有的Google浏览器
        #使用cookie和复用浏览器
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)

        self.driver = webdriver.Chrome()
    def teardown_method(self):
        self.driver.quit()

    def test_cookie(self):
        # 获取  cookie
        cookies = self.driver.get_cookies()
        # 以文件流的形式打开文件
        with open("cookie.json", "w") as f:
        # 存储 cookie 到 cookie.json
            json.dump(cookies, f)

        self.driver.get("https://work.weixin.qq.com/")
        sleep(3)
        # 以文件流的形式打开文件
        with open("cookie.json", "r") as f:
            # 读取 cookies
            cookies = json.load(f)
        # 注入 cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(10)
        self.driver.find_element(By.XPATH, '//*[@id="menu_customer"]/span').click()
        sleep(2)

