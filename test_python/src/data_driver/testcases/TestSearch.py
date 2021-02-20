from test_python.src.appium_frame.app_page import AppPage


class TestContact:
    def setup(self):
        self.app = AppPage()

    def teardown(self):
        self.app.stop()

    def test_blacker(self):
        toast = self.app.start().goto_main().goto_market()
        assert toast

