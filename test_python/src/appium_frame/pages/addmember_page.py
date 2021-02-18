from appium.webdriver.common.mobileby import MobileBy

from test_python.src.appium_frame.pages.base_page import BasePage
from test_python.src.appium_frame.pages.memberedit_page import MemberEditPage


class AddMemberPage(BasePage):
    def add_member_manually(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return MemberEditPage(self.driver)

    def get_toast(self):
        toast = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "添加成功")]').text
        return toast
