import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_vx():
    def setup(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()

    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        # with open("cookie.json","w") as f:
        #     json.dump(cookies, f)
        self.driver.get("https://work.weixin.qq.com/")
        with open("cookie.json","r") as f:
            cookies1 = json.load(f)
        for cookie in cookies1:
            self.driver.add_cookie(cookie)
        self.driver.find_element(By.XPATH, '//*[@class = "index_top_operation_loginBtn"]').click()

    def test_vxlogin(self):
        sleep(5)
        # self.driver.get("https://work.weixin.qq.com/")
        # self.driver.find_element(By.XPATH,'//*[@class = "index_top_operation_loginBtn"]').click()
        self.driver.find_element(By.XPATH,'//*[@id = "menu_contacts"]').click()
