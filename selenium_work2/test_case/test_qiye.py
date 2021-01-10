from time import sleep

import pytest
from selenium_work2.page.main_page import MainPage

class TestAddMember:
    def setup_method(self):
        # self.base = MainPage(types='debug')#走debug模式
        # self.base.write_cookie_for_json('../datas/cookie.json')#debug模式下进行写入cookie
        self.main = MainPage(url='https://work.weixin.qq.com/wework_admin/frame')
        self.main.add_cookie('../datas/cookie.json')  # 浏览器读取cookies
        self.main.refresh()

    def teardown_method(self):
        self.main.quit()

    def test_add_department_success(self):
        res = self.main.goto_department().add_member_success('test1').get_list()
        assert 'test1' in res

    def test_add_department_fail(self):
        res = self.main.goto_department().add_member_fail('test1').get_toast()
        assert '该部门已存在' == res

if __name__ == '__main__':
    pytest.main(['test_qiye.py','-sq'])