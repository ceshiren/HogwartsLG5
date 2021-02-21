# 通讯录页面对象
from appium.webdriver.common.mobileby import MobileBy
from homework.app_po.page.add_member_page import AddMemberPage
from homework.app_po.page.basepage import BasePage


class ContactPage(BasePage):
    def goto_add_member(self):
        self.scroll_find_click("添加成员")
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().'
        #                          'scrollable(true).instance(0)).'
        #                          'scrollIntoView(new UiSelector().'
        #                          'text("添加成员").instance(0));').click()
        return AddMemberPage(self.driver)
