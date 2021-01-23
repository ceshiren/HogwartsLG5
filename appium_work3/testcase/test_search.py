import pytest
from appium_work3.page.app import App

class TestAddMember:

    def setup(self):
        self.app = App().start()

    def teardown(self):
        self.app.stop()

    def test_add_member_success(self):
        res = self.app.main().goto_market().goto_search().search('alibaba')
        pytest.assume(res)

if __name__ == '__main__':
        pytest.main(['test_search.py','-sq'])