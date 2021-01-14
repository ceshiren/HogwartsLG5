from time import sleep

from selenium.webdriver.common.by import By
from selenium_PO.page.base_page import BasePage


class contact_page(BasePage):
    def add_department_successful(self, name):
        self.find(By.CSS_SELECTOR, '.member_colLeft_top_addBtnWrap').click()
        self.find(By.CSS_SELECTOR, '.js_create_party').click()
        self.find(By.NAME, 'name').send_keys(name)
        self.find(By.CSS_SELECTOR, '.js_toggle_party_list').click()
        self.find(By.CSS_SELECTOR, '.qui_dialog_body.ww_dialog_body [id="1688850514012490_anchor"]').click()
        self.find(By.CSS_SELECTOR, '[d_ck="submit"]').click()
        self.driver.refresh()
        return self

    def add_department_cancel(self, name):
        self.find(By.CSS_SELECTOR, '.member_colLeft_top_addBtnWrap').click()
        self.find(By.CSS_SELECTOR, '.js_create_party').click()
        self.find(By.NAME, 'name').send_keys(name)
        self.find(By.CSS_SELECTOR, '.js_toggle_party_list').click()
        self.find(By.CSS_SELECTOR, '.qui_dialog_body.ww_dialog_body [id="1688850514012490_anchor"]').click()
        self.find(By.CSS_SELECTOR, '[d_ck="cancel"]').click()
        self.driver.refresh()
        return self

    def add_department_fail(self, name):
        self.find(By.CSS_SELECTOR, '.member_colLeft_top_addBtnWrap').click()
        self.find(By.CSS_SELECTOR, '.js_create_party').click()
        self.find(By.NAME, 'name').send_keys(name)
        self.find(By.CSS_SELECTOR, '.js_toggle_party_list').click()
        self.find(By.CSS_SELECTOR, '.qui_dialog_body.ww_dialog_body [id="1688850514012490_anchor"]').click()
        self.find(By.CSS_SELECTOR, '[d_ck="submit"]').click()
        result = self.find(By.ID, 'js_tips')
        return result.text

    def get_deparment_list(self):
        """
        返回通讯录页面的部门
        """
        sleep(2)
        elements = self.driver.find_elements(By.XPATH, '//*[@class="jstree-anchor"]')
        department_list = []
        for element in elements:
            department_list.append(element.text)
        return department_list