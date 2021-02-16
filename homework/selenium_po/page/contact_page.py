from time import sleep
from selenium.webdriver.common.by import By
from homework.selenium_po.page.add_department_page import AddDepartmentPage
from homework.selenium_po.page.base_page import BasePage


class ContactPage(BasePage):
    def goto_add_department(self):
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        self.find(By.XPATH, '//*[text()="添加部门"]').click()
        return AddDepartmentPage(self.driver)

    def get_department_list(self):
        # 判断部门列表是否展开，未展开时进展展开
        expand_eles = self.find_elements(By.CSS_SELECTOR, ".jstree-node")
        for expan_ele in expand_eles:
            if expan_ele.get_attribute("aria-expanded") == "false":
                expan_ele.find_elements_by_xpath('./i').click()
        # 完全展开后再获取部门名称列表
        # 这里需要增加一个等待时间，等待新增加的部门信息可以获取正常
        sleep(3)
        department_list = list()
        elements = self.find_elements(By.CSS_SELECTOR, ".jstree-anchor")
        for ele in elements:
            department_list.append(ele.text)
        print("department_list:", department_list)
        return department_list
