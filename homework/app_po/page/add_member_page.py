# 添加成员页面对象
from appium.webdriver.common.mobileby import MobileBy
from homework.app_po.page.basepage import BasePage
from homework.app_po.page.manual_add_member_page import ManualAddMemberPage


class AddMemberPage(BasePage):
    def goto_manual_add_member_page(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.find_and_click((MobileBy.XPATH, "//*[@text='手动输入添加']"))
        return ManualAddMemberPage(self.driver)

    def get_toast(self):
        # ele = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        ele = self.find_and_get_text((MobileBy.XPATH, "//*[@class='android.widget.Toast']"))
        return ele
