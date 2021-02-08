import time

from selenium.webdriver.common.by import By

from test_po.page.base_page import BasePage


class AddDepartmentPage(BasePage):

    def add_department(self,name):
        #  输入部门 qui_inputText ww_inputText
        #  点击所属部门 qui_btn ww_btn ww_btn_Dropdown js_toggle_party_list
        # 选择部门  id=1688850950829607_anchor
        # 点击保存  //*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]      css = .ww_btn_Blue
        time.sleep(3)
        self.find(By.CSS_SELECTOR,'[name=name]').send_keys(name)
        #点击所属部门，选择第一个
        self.find(By.CSS_SELECTOR,".js_toggle_party_list").click()
        self.find(By.CSS_SELECTOR,".qui_dialog_body.ww_dialog_body [id='1688850950829607_anchor']").click()
        #点击确定
        time.sleep(2)
        self.find(By.XPATH,"//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]").click()