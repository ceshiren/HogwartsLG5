from base_page import BasePage
from add_member_page import AddMember

class AddMemberChoice(BasePage):

    def manual_add_member(self):
        '''点击手动添加成员'''
        self.steps('../page/addmemberchoice_goto_add_member.yaml')
        return AddMember(self._driver)

    def add_member_toeast(self):
        '''返回toeast'''
        return self.steps('../page/add_member_toeast.yaml').text
