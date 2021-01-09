from contact_page import ContactPage
from base_page_selenium import Base

class MainPage(Base):
    _contact_loc = ('css selector','.frame_nav a:nth-child(2)')#通讯录
    def goto_contact(self):
        '''跳转通讯录'''
        self.clicks(self._contact_loc)#点击通讯录
        return ContactPage(self._driver)

if __name__ == '__main__':
    contact = MainPage(url='https://work.weixin.qq.com/wework_admin/frame')
    contact.add_cookie('../datas/cookie.json')
    contact.refresh()
    contact.goto_contact()