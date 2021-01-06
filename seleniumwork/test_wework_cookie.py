import json
from http import cookies
from time import sleep

from selenium import webdriver

class TestWeworkCookie():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_cookie(self):
        self.driver.get("https://work.weixin.qq.com/")
        # cookies = self.driver.get_cookies()
        with open("cookie.json","a") as i:
            # json.dump(cookies,i)
            cookies = json.load(i)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(1)
        self.driver.find_element_by_link_text("企业登录").click()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="menu_customer"]/span').click()
        sleep(2)
