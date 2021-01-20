from selenium.webdriver.common.by import By

from test_po.page.base_page import BasePage


class ContactPage(BasePage):
    def goto_add_member(self):
        pass

    def add_department(self):
        pass

    def get_list(self):
        """
        返回通讯录页面的人员信息
        :return:
        """
        name_webelement_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        name_list = []
        for webelement in name_webelement_list:
            name_list.append(webelement.text)

        return name_list