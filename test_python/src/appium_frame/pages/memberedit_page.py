from appium.webdriver.common.mobileby import MobileBy

from test_python.src.appium_frame.pages.base_page import BasePage


class MemberEditPage(BasePage):
    def edit_name(self,name):
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        return MemberEditPage(self.driver)
    def edit_gender(self,gender):
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='性别']/..//*[@resource-id='com.tencent.wework:id/b8_']").click()
        if gender == "男":
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        return MemberEditPage(self.driver)

    def edit_phonenum(self,tel):
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fuy").send_keys(tel)
        return MemberEditPage(self.driver)

    def messageConfirm(self):
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ie7").click()
        from test_python.src.appium_frame.pages.addmember_page import AddMemberPage
        return AddMemberPage(self.driver)