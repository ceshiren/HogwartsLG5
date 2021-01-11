import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


from test_selenium.base import Base

#网页
class Test_selenium(Base):
    def test_click(self):
        # self.driver.get("https://ceshiren.com/")
        # ele_js = self.driver.execute_script("return document.getElementById('')")
        # ele_js.click()
        # ele_js1 = self.driver.execute_script("return document.scrollTop=10000")#向上滑动10000像素

        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script("a=document.getElementById('train_data');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_data').value='2021-12-31'")
        time.sleep(10)
        self.driver.implicitly_wait(5)
        # self.driver.implicitly_wait(5)
        # ele_cl = self.driver.find_element_by_xpath('//*[@id="ember109"]/td[1]/div/a/span[2]/span')
        # action = ActionChains(self.driver)
        # action.click(ele_cl)
        # self.driver.implicitly_wait(5)
        # action.perform()
        # self.driver.implicitly_wait(5)


if __name__ == '__main__':
    pytest.main()