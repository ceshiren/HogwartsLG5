from base_page_selenium import Base


class ContactPage(Base):
    _all_depart_loc = ('xpath','//ul[@role="group" and @class="jstree-children"]//li')#所有部门的元素
    _fail_toeast_loc = ('id','js_tips')#添加部门失败toeast

    def get_list(self):
        eles = self.find_elements(self._all_depart_loc)
        depart_list = []#存放部门名称
        for depart_name in eles:
            depart_name = depart_name.text.strip()
            depart_list.append(depart_name)
        return depart_list

    def get_toast(self):
        return  self.get_text(self._fail_toeast_loc)#获取toeast信息

if __name__ == '__main__':
    contact = ContactPage(types='debug')
    print(contact.is_displayed(contact._fail_toeast_loc))
    print(contact.set_display(contact._fail_toeast_loc,'block'))