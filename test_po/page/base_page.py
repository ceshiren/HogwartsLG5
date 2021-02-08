import json
import time

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self,base_driver=None):
        base_driver :WebDriver
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self._cookie_login()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(5)

    def _cookie_login(self):
        # 读取kookie文件
        self.driver.get("https://work.weixin.qq.com/")
        with open('cookie.json', 'r') as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(5)

    def find(self,by,value):
        return self.driver.find_element(by=by,value=value)

    def finds(self,by,value):
        return self.driver.find_elements(by=by,value=value)