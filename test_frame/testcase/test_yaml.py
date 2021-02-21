from test_frame.page.market_page import MarketPage


def test_yaml():
    market_page = MarketPage()
    market_page.goto_search()
