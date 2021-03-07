import pytest
from homework.api_test_frame.api.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()

    @pytest.mark.parametrize("userid, username, mobile, department",
                             [["jingdong", "京东", "12800000001", [1, 2]]])
    def test_add_member(self, userid, username, mobile, department: list):
        # pre_test:删除成员
        self.address.delete_member(userid)
        # test:添加成员
        add_result = self.address.add_member(userid, username, mobile, department)
        assert add_result.get("errcode") == 0
        # post_test:查询成员信息
        get_result = self.address.get_member(userid)
        assert get_result.get("userid", "添加成员失败") == "jingdong"