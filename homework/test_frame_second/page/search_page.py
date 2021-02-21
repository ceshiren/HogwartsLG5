from homework.test_frame_second.basepage import BasePage


class SearchPage(BasePage):
    def search(self):
        self.run_steps("../yaml/search_page.yaml", "search")
        # self.find_and_send_text((MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']"), "alibaba")