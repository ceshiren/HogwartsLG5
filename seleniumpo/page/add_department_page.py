from time import sleep

from selenium.webdriver.common.by import By

from seleniumpo.page.base_page import BasePage
from seleniumpo.page.contact_page import ContactPage


class AddMemberDepartmentPage(BasePage):

    _name = (By.NAME,"name")
    def add_department(self,name):
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click() #点击+号
        self.find(By.CSS_SELECTOR, ".js_create_party").click()    #选择添加部门
        self.find(*self._name).send_keys(name)     #输入部门名称
        self.find(By.CSS_SELECTOR,".js_toggle_party_list").click()  #点击所属部门
        self.find(By.CSS_SELECTOR,'.qui_dialog_body.ww_dialog_body [id="1688851257680761_anchor"]').click()   #选择部门归属
        self.find(By.XPATH, "//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]").click()    #点击确定
        sleep(3)
        self.driver.refresh()
        sleep(2)
        return ContactPage(self.driver)

    def add_department_null(self,name):
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()  # 点击+号
        self.find(By.CSS_SELECTOR, ".js_create_party").click()  # 选择添加部门
        self.find(*self._name).send_keys(name)  # 输入部门名称
        self.find(By.CSS_SELECTOR, ".js_toggle_party_list").click()  # 点击所属部门
        self.find(By.CSS_SELECTOR, '.qui_dialog_body.ww_dialog_body [id="1688851257680761_anchor"]').click()  # 选择部门归属
        self.find(By.XPATH, "//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]").click()  # 点击确定
        sleep(1)
        self.find(By.CSS_SELECTOR,'[d_ck="cancel"]').click()  #点击取消
        return ContactPage(self.driver)

    def add_department_repe(self,name):
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()  # 点击+号
        self.find(By.CSS_SELECTOR, ".js_create_party").click()  # 选择添加部门
        self.find(*self._name).send_keys(name)  # 输入部门名称
        self.find(By.CSS_SELECTOR, ".js_toggle_party_list").click()  # 点击所属部门
        self.find(By.CSS_SELECTOR, '.qui_dialog_body.ww_dialog_body [id="1688851257680761_anchor"]').click()  # 选择部门归属
        self.find(By.XPATH, "//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]").click()  # 点击确定
        sleep(1)
        return ContactPage(self.driver)