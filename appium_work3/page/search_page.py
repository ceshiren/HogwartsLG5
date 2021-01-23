from appium_work3.page.base_page import BasePage


class SearchPage(BasePage):
    def search(self,content):
        self._params['value'] = content
        self.steps('search_page.yaml','search')
        return True