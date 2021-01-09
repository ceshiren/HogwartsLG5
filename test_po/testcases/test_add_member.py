from test_po.page.main_page import MainPage


class TestAddMember():

    def setup_class(self):
        # 实例化 MainPage类
        self.main = MainPage()

    def test_add_member(self):
        #1. 首页跳转到添加成员页面 2. 添加成员 3. 获取成员信息
        result = self.main.goto_add_member().add_member("崔丝塔娜").get_list()
        assert "崔丝塔娜" in result

    def test_add_member_fail(self):
        # 1. 描述业务场景， 不是描述具体的行为操作
        result = self.main.goto_add_member().add_member_fail("崔丝塔娜").get_list()
        assert "崔丝塔娜" not in result
