from selenium.webdriver.common.by import By
from test_po.page.base_page import BasePage
from test_po.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    _username = (By.ID, "username")

    def add_member(self ,name):
        # 输入成员信息，点击保存
        self.find(self.username).send_keys(name)
        self.find(By.ID, "memberAdd_acctid").send_keys("13145212")
        self.find(By.ID, "memberAdd_phone").send_keys("13866668887")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)

    def add_member_fail(self , name):
        # 输入成员信息，点击保存
        # *代表解元祖，相当于self.find(By.ID, "username")
        self.find(*self.username).send_keys(name)
        self.find(By.ID, "memberAdd_acctid").send_keys("13145212")
        self.find(By.ID, "memberAdd_phone").send_keys("13866668888")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        self.find(By.CSS_SELECTOR, ".js_btn_cancel").click()
        return ContactPage(self.driver)



