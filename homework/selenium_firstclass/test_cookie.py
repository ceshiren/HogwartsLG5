import json
from time import sleep
from selenium import webdriver


class TestLogin:
    def setup_method(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)

    def test_getcookies(self):
        # 使用浏览器调试网页登录后，直接获取网页的cookie信息
        cookies = self.driver.get_cookies()
        # 将获取到的cookie信息写入到cookies.json文件中
        with open("cookies.json", "w") as f:
            json.dump(cookies, f)

    def test_login(self):
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
        self.driver.find_element_by_id("menu_customer").click()
        sleep(3)
