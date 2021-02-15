from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.addresslist_page import AddressListPage
from test_appium.page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
 #点击通讯录
    def click_addresslist(self):
        self.find_and_click((MobileBy.XPATH, "//*[@text='通讯录']"))
        return AddressListPage(self.driver)