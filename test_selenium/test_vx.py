import pytest

from test_selenium.page.base_page import BasePage
from test_selenium.page.main1 import Main


class Test_vx():
    def setup(self):
        print("开始")



    def test_registar(self):
        self.Main = Main()
        self.Main.goto_registar()


if __name__ == '__main__':
    pytest.main()