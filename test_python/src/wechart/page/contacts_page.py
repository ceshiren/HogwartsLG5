from selenium.webdriver.common.by import By

from test_python.src.wechart.page.base_page import BasePage


class Contacts(BasePage):
    def goto_add_dep(self):
        self.click_element_by(By.CLASS_NAME, "member_colLeft_top_addBtn")
        self.click_element_by(By.CSS_SELECTOR, "#js_contacts47 > div > div.member_colLeft > ul > li:nth-child(1) > a")
        return AddDepartment(self.driver)

    def is_add_dep_success(self):
        self.is_ele_exit(By.XPATH, "//ul[@class='jstree-children']")


class AddDepartment(BasePage):
    def add_dep(self):
        self.send_keys_by(By.XPATH, "//form//input[1]", "技术部门")
        self.click_element_by(By.CLASS_NAME, "js_toggle_party_list")
        self.click_element_by(By.CLASS_NAME, "js_party_list_container")
        self.click_element_by(By.PARTIAL_LINK_TEXT, "确定")
        return Contacts(self.driver)

