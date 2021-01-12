from base_page import BasePage
from add_member_choice import AddMemberChoice

class Contact(BasePage):
    _member_list_loc = ('xpath','//*[@resource-id="com.tencent.wework:id/ilb" ]//android.widget.TextView')
    def goto_add_member(self):
        '''点击添加成员'''
        self.steps('../page/contact_goto_add_member.yaml')
        return AddMemberChoice(self._driver)

    def get_member_list(self):
        '''获取成员名称'''
        eles = self.find_elements(self._member_list_loc)
        member_list = []
        for member in eles:
            member_list.append(member.text)
        return member_list