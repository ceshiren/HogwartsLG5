import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWorkWechat:
    def setup_class(self):
        # self.driver.maximize_window()
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"  #传入本地的chrome调试端口
        # self.driver = webdriver.Chrome(options=chrome_args) #浏览器复用时使用
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_get_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#customer/analysis")
        sleep(8)  # sleep 扫码
        # 获取  cookie
        cookies = self.driver.get_cookies()
        # 以文件流的形式打开文件
        with open("cookie.json", "w") as f:
            # 存储 cookie 到 cookie.json
            json.dump(cookies, f)

    def test_customer(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#customer/analysis")
        self.driver.find_element_by_id('menu_customer').click()
        sleep(3)

    def test_customer_cookie(self):
        self.driver.get("https://work.weixin.qq.com/")
        # 以文件流的形式打开文件
        with open("cookie.json", "r") as f:
            # 读取 cookies
            cookies = json.load(f)
        # 注入 cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.test_customer()