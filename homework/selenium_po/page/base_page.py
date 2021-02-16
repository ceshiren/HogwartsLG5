import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, base_driver: WebDriver = None):
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self._cookie_login()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(3)

    def _cookie_login(self):
        # 先打开需要登录的网页（未登录的状态下）
        self.driver.get("https://work.weixin.qq.com/")
        # 读取cookie信息
        with open("cookies.json", "r") as f:
            cookies = json.load(f)
        # 通过add_cookie方法注入cookie，add_cookie方法在注入之前要打开需要注入的网页，就是第一行代码
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # 注入后，重新打开登录后的页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)

    def find(self, by, locator):
        return self.driver.find_element(by=by, value=locator)

    def find_elements(self, by, locator):
        return self.driver.find_elements(by=by, value=locator)