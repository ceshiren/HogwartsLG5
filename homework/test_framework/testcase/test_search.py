# -*- coding: utf-8 -*-
# @time     : 2021/1/19 22:34
# @Author   : Owen
# @File     : test_search.py
from homework.test_framework.app import App


class TestSearch:

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    def test_search(self):
        result = self.main.goto_search().get_text()
        assert result == "今日热点"