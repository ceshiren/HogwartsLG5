import pytest

from test_socket.test_wework.test_po.Api.Address import Address
class Test_Contact:
    def setup(self):
        self.address = Address()

    @pytest.mark.parametrize("userid,name,mobile,depart",[("wg122801","wg122801",12312312326,[7])])
    def test_add_member(self,userid,name,mobile,depart):
        # "userid": "userid",
        # "name": "wg228",
        # "mobile": "12312312324",
        # "department": [7]
        r = Address.add_member(self.address,userid,name,mobile,depart)
        assert r["errcode"] == 0
        Address.delete_member(self.address,userid)
        assert r["errcode"] == 0
