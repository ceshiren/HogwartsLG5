import pytest
from apitest_work2.api.address import Address


class TestAddress:

    def setup(self):
        self.address = Address()

    @pytest.mark.parametrize("name,userid,mobile", [("测试1号", "test01", "+86 18100000001"),
                                               ("测试2号", "test02", "+86 18100000002"),
                                               ("测试3号", "test03", "+86 18100000003")],
                             ids=["add_account1", "add_account2", "add_account3"])
    def test_add_member(self, name, userid, mobile):
        department = [1]
        r = self.address.add_member(userid=userid, name=name, mobile=mobile, department=department)
        assert r.get("errcode") == 0
        assert r.get("errmsg") == "created"
        r = self.address.get_member(userid)
        print(r)
        assert r.get("name", "userid 添加失败") == name
        d = self.address.delete_member(userid) #删除添加的数据
        assert d.get("errcode") == 0