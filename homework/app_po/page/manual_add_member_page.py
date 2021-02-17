# 手动添加成员页面对象
from homework.app_po.page.basepage import BasePage


class ManualAddMemberPage(BasePage):
    def edit_name(self, name):
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        return self

    def edit_gender(self, gender):
        self.driver.find_element_by_xpath("//*[contains(@text,'性别')]/../android.widget.RelativeLayout").click()
        if gender == "男":
            self.driver.find_element_by_xpath("//*[@text='男']").click()
        else:
            self.driver.find_element_by_xpath("//*[@text='女']").click()
        return self

    def edit_email(self, email):
        self.driver.find_element_by_xpath("//*[contains(@text,'邮箱')]/../android.widget.EditText").send_keys(email)
        return self

    def click_save(self):
        from homework.app_po.page.add_member_page import AddMemberPage
        self.driver.find_element_by_xpath("//*[@text='保存']").click()
        return AddMemberPage(self.driver)

