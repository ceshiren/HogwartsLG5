from appium_frame.app import App


def test_search():
    app = App()
    result = app.start().goto_main().goto_market_page().goto_search().search()
    assert result == True