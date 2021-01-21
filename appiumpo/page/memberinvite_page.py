
#点击手动添加人员
from appium.webdriver.common.mobileby import MobileBy



#邀请成员页面
from appiumpo.page.base_page import BasePage
from appiumpo.page.contactedit_page import ContactEditPage


class MemberinvitePage(BasePage):
    def addconect_menual(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.find_and_click((MobileBy.XPATH, "//*[@text='手动输入添加']"))
        return ContactEditPage(self.driver)

    #判断是否添加成功
    def get_toast(self):
        # result = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"添加成功")]').text
        result = self.find_and_get_text((MobileBy.XPATH, '//*[contains(@text,"添加成功")]'))
        return result