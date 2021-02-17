# 主页对象
from homework.app_po.page.basepage import BasePage
from homework.app_po.page.contact_page import ContactPage


class MainPage(BasePage):
    def goto_contact(self):
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        return ContactPage(self.driver)
