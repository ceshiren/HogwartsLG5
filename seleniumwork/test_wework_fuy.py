import json
from http import cookies
from time import sleep

from selenium import webdriver

class TestWeworkFuy():
    def setup(self):
        # self.driver = webdriver.Chrome()
        chromes= webdriver.ChromeOptions()         #浏览器复用
        chromes.debugger_address= "127.0.0.1:9222"
        self.driver= webdriver.Chrome(options=chromes)
        self.driver.implicitly_wait(5)
        # self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_wework(self):
        self.driver.get("https://work.weixin.qq.com/")
        sleep(1)
        self.driver.find_element_by_link_text("企业登录").click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu_customer"]/span').click()
        sleep(2)


