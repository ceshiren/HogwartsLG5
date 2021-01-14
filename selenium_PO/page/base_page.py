import json
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, base_driver=None):
        base_driver: WebDriver
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self._cookie_login()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(5)

    def test_get_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#customer/analysis")
        sleep(8)  # sleep 扫码
        # 获取  cookie
        cookies = self.driver.get_cookies()
        # 以文件流的形式打开文件
        cookie_path = os.path.dirname(__file__) + "./cookie.json"
        with open(cookie_path, "w") as f:
            # 存储 cookie 到 cookie.json
            json.dump(cookies, f)

    def _cookie_login(self):
        self.driver.get("https://work.weixin.qq.com/")
        # 以文件流的形式打开文件
        cookie_path = os.path.dirname(__file__) + "./cookie.json"
        with open(cookie_path, "r") as f:
            # 读取 cookies
            cookies = json.load(f)
        # 注入 cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#customer/analysis")
        sleep(3)
        # self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()

    def find(self, by, value):
        return self.driver.find_element(by=by, value=value)