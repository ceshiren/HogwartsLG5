from base_page_selenium import Base


class AddDepartmentPage(Base):
    _depart_name_loc = ('css selector','.member_tag_dialog_inputDlg div:nth-child(1) input')#部门名称
    _click_depart_loc = ('css selector','.js_parent_party_name')#部门下拉
    _depart_loc = ('xpath', '//form[@class="form"]//a[@tabindex="-1" and @id="1688850024412370_anchor"]')# 所属部门
    _ensure_loc = ('css selector','.ww_dialog_foot a:nth-child(1)')#确定

    def add_member_success(self,depart_name):
        '''添加部门成功'''
        self.sendkeys(self._depart_name_loc,depart_name)#输入部门姓名
        self.clicks(self._click_depart_loc)  # 点击选择部门
        self.clicks(self._depart_loc)#选择具体部门
        self.clicks(self._ensure_loc)# 点确定
        from contact_page import ContactPage
        return ContactPage(self._driver)

    def add_member_fail(self,depart_name):
        '''添加部门失败'''
        self.sendkeys(self._depart_name_loc,depart_name)#输入部门姓名
        self.clicks(self._click_depart_loc)  # 点击选择部门
        self.clicks(self._depart_loc)#选择具体部门
        self.clicks(self._ensure_loc)# 点确定
        from contact_page import ContactPage
        return ContactPage(self._driver)

if __name__ == '__main__':
    contact = AddDepartmentPage(url='https://work.weixin.qq.com/wework_admin/frame#contacts',types='debug')
    print(contact.get_list())