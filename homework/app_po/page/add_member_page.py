# 添加成员页面对象
from homework.app_po.page.basepage import BasePage
from homework.app_po.page.manual_add_member_page import ManualAddMemberPage


class AddMemberPage(BasePage):
    def goto_manual_add_member_page(self):
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        return ManualAddMemberPage(self.driver)

    def get_toast(self):
        ele = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        return ele
