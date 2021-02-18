import os

import pytest
import yaml

from test_python.src.appium_frame.pages.app_page import AppPage
from test_python.src.appium_frame.common.Common_Funcs import Common_Funcs
class TestContact:
    def setup(self):
        self.app = AppPage()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name,gender,phonenum",Common_Funcs().get_data()[0],ids=Common_Funcs().get_data()[1])
    def test_add_contact(self,name,gender,phonenum):
        # name = "zhangsi2"
        # gender = '男'
        # phonenum = '13300000002'
        toast = self.main

