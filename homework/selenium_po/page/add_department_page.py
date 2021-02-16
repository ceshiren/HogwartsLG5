from selenium.webdriver.common.by import By

from homework.selenium_po.page.base_page import BasePage


class AddDepartmentPage(BasePage):
    def add_department(self):
        from homework.selenium_po.page.contact_page import ContactPage
        self.find(By.NAME, "name").send_keys("测试部")
        self.find(By.CSS_SELECTOR, '.js_toggle_party_list').click()
        # 选择“一部”为所属部门
        self.find(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688850462628028_anchor']").click()
        self.find(By.XPATH, '//*[@d_ck="submit"]').click()
        return ContactPage(self.driver)
