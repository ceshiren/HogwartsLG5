from selenium.webdriver.common.by import By

from seleniumpo.page.base_page import BasePage


class ContactPage(BasePage):

    def get_department_list(self):
        add_depart_list = self.driver.find_elements(By.CSS_SELECTOR,".jstree-anchor")
        depart_list = []
        for depart in add_depart_list:
            depart_list.append(depart.text)
        return depart_list


