from test_python.src.appium_frame.app_page import AppPage


class TestContact:
    def setup(self):
        self.app = AppPage()

    def teardown(self):
        self.app.stop()

    def test_blacker(self):
        result = self.app.start().goto_main().goto_market().goto_search().input_keyword().search_stocks()

        assert result

