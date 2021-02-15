from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage
from test_appium.page.managecontact_page import ManageContactPage
from test_appium.page.memberinvite_page import MemberInvitePage
from test_appium.page.personalinfo_page import PersonalInfoPage


class AddressListPage(BasePage):

    # def __init__(self,driver):
    #     self.driver = driver

    #点击添加成员
    def add_member(self):
        self.scroll_and_find_and_click("添加成员")
        return MemberInvitePage(self.driver)

    def view_personal_information(self,name):
        #查看个人信息
        # self.find_and_click((MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/e0l' and @text='哈哈']"))
        self.find_and_click((MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/e0l']//*[@text='哈哈']"))
        return PersonalInfoPage(self.driver)

    def click_search(self):
        #点击搜索
        self.find_and_click((MobileBy.ID,"com.tencent.wework:id/igk"))
        return

    def manage_contact(self):
        #管理通讯录
        self.find_and_click((MobileBy.ID,"com.tencent.wework:id/igf"))
        return ManageContactPage(self.driver)