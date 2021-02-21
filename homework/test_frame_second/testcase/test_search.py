from homework.test_frame_second.app import App


class TestDemo:

    def test_search(self):
        app = App()
        app.start().goto_main().goto_market_page().goto_search().search()
