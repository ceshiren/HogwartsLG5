from appium.webdriver.common.mobileby import MobileBy
from appium_work2.page.add_member_page import AddMemberPage
from appium_work2.page.base_page import BasePage


class MainPage(BasePage):

    def click_contact(self):
        contact_locator = (MobileBy.XPATH, '//*[contains(@resource-id, "com.tencent.wework:id/elq") and '
                                                 'contains(@text, "通讯录")]') # 使用组合定位，避免页面中其他带通讯录的元素干扰
        self.find(contact_locator).click()
        return AddMemberPage(self.driver)