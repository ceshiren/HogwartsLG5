from base_page import BasePage
from add_member import AddMember

class AddMemberChoice(BasePage):

    def manual_add_member(self):
        '''点击手动添加成员'''
        self.steps('../page/addmemberchoice_goto_add_member.yaml')
        return AddMember(self._driver)

    def back(self):
        '''点击返回'''
        self.steps('../page/addmemberchoice_back.yaml')
        pass