import json
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_python.studypy.baseutil import WechatCom


class TestEnterpriseWeChat(WechatCom):


    # def test_cookie(self):
    #     self.driver.get("https://work.weixin.qq.com/")
        # self.driver.maximize_window()
        # self.driver.find_element_by_xpath('//*[@id=\"indexTop\"]/div[2]/aside/a[1]').click()
        # sleep(10)
        # cookies = self.driver.get_cookies()
        # with open("./cookie.json", "w") as f:
        #     json.dump(cookies, f)
        #
        # with open("./cookie.json", "r") as f:
        #     cookies = json.load(f)
        # print(cookies)
        # for cookie in cookies:
        #     self.driver.add_cookie(cookie)
        # self.driver.find_element_by_xpath('//*[@id=\"indexTop\"]/div[2]/aside/a[1]').click()
        # sleep(10)

    def test_crm(self):
        self.driver.find_element_by_xpath('//*[@id=\"indexTop\"]/div[2]/aside/a[1]').click()
        self.driver.find_element(By.ID, "menu_customer").click()
        sleep(5)


