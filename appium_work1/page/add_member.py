from base_page import BasePage

class AddMember(BasePage):

    def add_member(self,name,phone):
        '''添加成员成功'''
        self._params['{name}'] = name
        self._params['{phone}'] = phone
        self.steps('../page/add_member.yaml')
        print('添加成功')
        return True

