from homework.test_frame.app import App


class TestDemo:

    def test_search(self):
        app = App()
        app.start().goto_main().goto_market_page().goto_search().search()
