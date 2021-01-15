import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By



class BasePage:
    def __init__(self, base_driver=None):

        if base_driver is None:
            self.driver = webdriver.Chrome()
            self._cookie_login()
        else:
            self.driver= base_driver

        # self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def quit(self):
        self.driver.quit()

    def _cookie_login(self):
        self.driver.get("https://work.weixin.qq.com/")
        with open("E:\pycharm\Project\HogwartsLG5\seleniumpo\case\cookie.json", "r") as i:
            cookies = json.load(i)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="menu_customer"]/span').click()

    def find(self,by,value):
        return self.driver.find_element(by=by,value=value)