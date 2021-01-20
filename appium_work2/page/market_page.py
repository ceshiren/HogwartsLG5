from appium_work2.page.base_page import BasePage
from appium_work2.page.search_page import SearchPage


class MarketPage(BasePage):
    _search_Loc = ('id','com.xueqiu.android:id/action_search')#搜索按钮

    def goto_search(self):
        self.click_new(self._search_Loc)
        return SearchPage(self._driver)
