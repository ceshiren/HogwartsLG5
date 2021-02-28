from test_python.src.data_driver.base_page import BasePage


class SearchPage(BasePage):
    def input_keyword(self):
        self.run_steps("../pages/search_page.yaml", "input_keyword")
        return self

    def search_stocks(self):
        self.run_steps("../pages/search_page.yaml", "search_stocks")
        return True
