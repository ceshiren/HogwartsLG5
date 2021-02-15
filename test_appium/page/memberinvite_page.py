from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage
from test_appium.page.contactedit_page import ContactEditPage


class MemberInvitePage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    #点击手动添加
    def addconect_menual(self):
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/cth").click()
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/cth"))
        return ContactEditPage(self.driver)