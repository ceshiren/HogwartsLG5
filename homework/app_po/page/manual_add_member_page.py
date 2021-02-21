# 手动添加成员页面对象
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from homework.app_po.page.basepage import BasePage


class ManualAddMemberPage(BasePage):
    def edit_name(self, name):
        # self.driver.find_element(MobileBy.XPATH,
        #                          "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.find_and_send_text((MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../android.widget.EditText"),
                                name)
        return self

    def edit_gender(self, gender):
        # self.driver.find_element(MobileBy.XPATH,
        #                          "//*[contains(@text,'性别')]/../android.widget.RelativeLayout").click()
        self.find_and_click((MobileBy.XPATH,
                             "//*[contains(@text,'性别')]/../android.widget.RelativeLayout"))
        # 写一段显示等待的代码吧
        locator = (MobileBy.XPATH, "//*[@text='男']")
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        if gender == "男":
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
            self.find_and_click((MobileBy.XPATH, "//*[@text='男']"))
        else:
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
            self.find_and_click((MobileBy.XPATH, "//*[@text='女']"))
        return self

    def edit_email(self, email):
        self.find_and_send_text((MobileBy.XPATH,
                                 "//*[contains(@text,'邮箱')]/../android.widget.EditText"),
                                email)
        return self

    def click_save(self):
        from homework.app_po.page.add_member_page import AddMemberPage
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        self.find_and_click((MobileBy.XPATH, "//*[@text='保存']"))
        return AddMemberPage(self.driver)

