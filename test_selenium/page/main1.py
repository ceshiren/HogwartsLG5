from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.registar import registar


class Main(BasePage):
    # _base_url = "https://work.weixin.qq.com/"
    def goto_registar(self):
        el = self.find(By.XPATH,'//*[@id="tmp"]/div[1]/a')
        el.click()
        return registar(self.driver)

    def goto_login(self):
        pass