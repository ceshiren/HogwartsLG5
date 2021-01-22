from time import sleep

from selenium.webdriver.common.by import By

from test_python.src.selenium_programe.page.basepage import BasePage


class AddDepartmentPage(BasePage):
    def insertName(self,name):
        self.driver.find_element(By.NAME, 'name')
        self.driver.find_element(By.NAME, 'name').send_keys(name)
        return AddDepartmentPage(self.driver)
    def chooseBaseDept(self):
        self.findAndClick((By.CLASS_NAME, 'js_toggle_party_list'))
        # self.driver.find_element(By.XPATH, "//div[@class='js_party_list_container']/div/ul/li/div").click()
        ele=self.finds((By.XPATH, "//*[contains(@id,'_anchor')]"))
        ele_length = len(ele)
        ele[int(ele_length/2)].click()
        return AddDepartmentPage(self.driver)

    def confirmDept(self):
        self.findAndClick((By.XPATH, "//*[@d_ck='submit']"))
        sleep(1)
        from test_python.src.selenium_programe.page.contact_page import ContactPage
        return ContactPage(self.driver)