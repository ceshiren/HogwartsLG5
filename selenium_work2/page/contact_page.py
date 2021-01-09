from time import sleep

from add_department_page import AddDepartmentPage
from base_page_selenium import Base


class ContactPage(Base):
    _add_loc = ('css selector','.member_colLeft_top_addBtn')#添加按钮
    _add_department_loc = ('css selector','.js_create_party')#添加部门入口
    _all_depart_loc = ('xpath','//ul[@role="group" and @class="jstree-children"]//li')#所有部门的元素
    _fail_toeast_loc = ('id','js_tips')#添加部门失败toeast


    def goto_department(self):
        '''添加部门'''
        self.clicks(self._add_loc)#点击添加按钮
        self.clicks(self._add_department_loc)#点击添加部门
        return AddDepartmentPage(self._driver)

    def get_list(self):
        eles = self.find_elements(self._all_depart_loc)
        depart_list = []#存放部门名称
        for depart_name in eles:
            depart_list.append(depart_name.text)
        return depart_list

    def get_toeast(self):
        sleep(1)
        return  self.get_text(self._fail_toeast_loc)#获取toeast信息

if __name__ == '__main__':
    contact = ContactPage(types='debug')
    print(contact.get_list())
