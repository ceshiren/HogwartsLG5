# -*- coding: utf-8 -*-
# @time     : 2021/1/24 10:32
# @Author   : Owen
# @File     : test_search.py
from homework.test_framework_yaml.app import App


class TestSearch:

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    def test_search(self):
        self.main.goto_search().search()


