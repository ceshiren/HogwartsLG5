from selenium.webdriver.common.by import By
from selenium_PO.page.base_page import BasePage
from selenium_PO.page.contact_page import contact_page

'''
企业微信首页
'''


class home_page(BasePage):
    def click_contacts(self):
        self.find(By.ID, 'menu_contacts').click()
        return contact_page(self.driver)
