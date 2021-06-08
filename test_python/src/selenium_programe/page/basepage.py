import json
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:
    path = os.path.dirname(__file__).strip("page").__add__("data/cookie.json")

    def __init__(self, base_drievr=None):
        base_drievr: webdriver
        if base_drievr == None:
            self.driver = webdriver.Chrome()
            self._loginByCookie()
        else:
            self.driver = base_drievr

    def _getCookies(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=chrome_args)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = driver.get_cookies()
        # 以文件流的形式打开文件
        with open(self.path, "w") as f:
            # 存储 cookie 到 cookie.json
            json.dump(cookies, f)
        f.close()

    def _loginByCookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 以文件流的形式打开文件
        with open(self.path, "r") as f:
            # 读取 cookies
            cookies = json.load(f)
        # 注入 cookies
        f.close()
        for cookie in cookies:
            # print(cookie["domain"])
            try:
                if cookie["expiry"] != "":
                    del cookie["expiry"]
            except:
                pass
            self.driver.add_cookie(cookies)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def finds(self, locator):
        return self.driver.find_elements(*locator)

    def findAndClick(self, locator):
        self.find(locator).click()

    def findAndSendkey(self, locator, key):
        self.find(locator).sendkeys(key)
