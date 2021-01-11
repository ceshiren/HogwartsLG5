# -*- coding: utf-8 -*-
# @time     : 2021/1/10 10:25
# @Author   : Owen
# @File     : mainpage.py
from selenium.webdriver.common.by import By

from homework.weixin.core.base import Base
from homework.weixin.core.contact import Contact
'''
企业微信首页
'''

class MainPage(Base):
    #跳转到联系人页面
    def goto_contact(self):
        self.find(By.CSS_SELECTOR, '#menu_contacts').click()
        return Contact(self.driver)