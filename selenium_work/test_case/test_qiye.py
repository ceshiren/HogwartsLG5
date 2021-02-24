import pytest
from selenium_work.page.base_page_selenium import Base
from time import sleep
from selenium_work.page.index_page import *
class TestWeChat:

    def setup_class(self):
        # self.common = Base(types='debug')#走debug模式
        # self.common.write_cookie_for_json()#debug模式下进行写入cookie
        self.base = Base(url=url)#走非debug模式
        self.base.add_cookie()  # 浏览器读取cookies
        self.base.refresh()

    def teardown_class(self):
        sleep(3)
        self.base.quit()

    def test_wx(self):
        self.base.clicks(loc)#点击客户联系
if __name__ == '__main__':
    pytest.main(['test_qiye.py','-sq'])