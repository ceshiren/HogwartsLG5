from test_python.src.wechart.page.contacts_page import Contacts
from test_python.src.wechart.page.index_page import IndexPage


class TestContact:
    def setup(self):
        print("测试通讯录")
        self.index = IndexPage()

    def test_add_dep(self):
        assert self.index.goto_contacts().goto_add_dep().add_dep().is_add_dep_success()

    def teardown(self):
        self.index.close()
