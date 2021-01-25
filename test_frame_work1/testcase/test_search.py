import yaml
from test_frame_work1.base.app import App


class TestSearch:
    def setup(self):
        self.app = App()

    def teardown(self):
        self.app.stop()

    def test_search(self):
        result = self.app.start().goto_main().goto_market_page().goto_search().search()
        assert result

