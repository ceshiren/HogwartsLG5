from add_department_page import AddDepartmentPage
from base_page_selenium import Base

class MainPage(Base):
    _contact_loc = ('css selector','.frame_nav a:nth-child(2)')#通讯录
    _add_loc = ('css selector','.member_colLeft_top_addBtn')#添加按钮
    _add_department_loc = ('css selector','.js_create_party')#添加部门入口

    def goto_department(self):
        '''添加部门'''
        self.clicks(self._contact_loc)#点击通讯录
        self.clicks(self._add_loc)  # 点击添加按钮
        self.clicks(self._add_department_loc)  # 点击添加部门
        return AddDepartmentPage(self._driver)

if __name__ == '__main__':
    contact = MainPage(url='https://work.weixin.qq.com/wework_admin/frame')
    contact.add_cookie('../datas/cookie.json')
    contact.refresh()
    contact.goto_contact()