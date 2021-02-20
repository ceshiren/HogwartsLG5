import os

import pytest
import yaml

from test_python.src.appium_frame.pages.app_page import AppPage
from test_python.src.appium_frame.common.Common_Funcs import Common_Funcs
class TestContact:
    def setup(self):
        self.app = AppPage()

    def teardown(self):
        self.app.stop()

    def test_blacker(self):
        toast = self.app.start().goto_main().goto_market()
        assert toast

