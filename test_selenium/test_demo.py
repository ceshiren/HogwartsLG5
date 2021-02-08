import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDemo():
    def setup(self):
        # chrome_args = webdriver.ChromeOptions()
        # chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        self.driver.get("https://work.weixin.qq.com/")
        # self.driver.find_element(By.XPATH, "//*[@class='index_top_operation_loginBtn']").click()
        # time.sleep(15)
        # cookies = self.driver.get_cookies()
        # with open("cookie.json",'w') as f:
        #     json.dump(cookies,f)
        #读取kookie文件
        with open('cookie.json','r') as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='menu_customer']").click()   #点击客户联系
        time.sleep(3)

    @pytest.mark.skip
    def test_weixin(self):
        self.driver.get("https://work.weixin.qq.com/")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='menu_index']").click()  #点击首页
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='menu_contacts']").click()  #点击通讯录
        time.sleep(3)
