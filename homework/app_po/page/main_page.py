# 主页对象
from appium.webdriver.common.mobileby import MobileBy
from homework.app_po.page.basepage import BasePage
from homework.app_po.page.contact_page import ContactPage


class MainPage(BasePage):
    def goto_contact(self):
        self.find_and_click((MobileBy.XPATH, "//*[@text='通讯录']"))
        return ContactPage(self.driver)
