from homework.app_po.page.app import App


class TestAddMember:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    def test_add_member(self):
        toast = self.main.goto_contact().goto_add_member().\
            goto_manual_add_member_page().edit_name("zhangsan2").edit_gender("男").\
            edit_email("zhangsan2@qq.com").click_save().get_toast()
        assert toast == "添加成功"