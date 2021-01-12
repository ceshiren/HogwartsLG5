from base_page import BasePage
from contact import Contact

class Main(BasePage):

    def goto_contact(self):
        '''点击通讯录'''
        self.steps('../page/main.yaml')
        return Contact(self._driver)
