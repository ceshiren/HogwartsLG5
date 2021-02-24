import pytest
from common.base import Api
import yaml,base64

class TestApi:


    def setup_class(self):
        corpid = "wwb341710801ade2f6"
        corpsecret = "6wJxVZUKmLrAJTBiD7p21twm2Fiy7NZWkAxI6HtDSV0"
        req_data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}",
            "headers": None,
            "json": None,
            "encoding": "base64"
        }
        self.token = Api().send(req_data).json()['access_token']#拿到token信息

    def test_query_member(self):
        userid = "ShenGang"
        req_data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}",
            "headers": None,
            "json": None,
            "encoding": "base64"
        }
        self.res = Api().send(req_data).json() # 拿到成员信息
        pytest.assume(self.res['mobile'] == '17365372296')

    def test_update_member(self):
        userid = "ShenGang"
        req_data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
            "headers": None,
            "json": {
                'userid' : userid,
                'name' : '沈刚（改）'
            },
            "encoding": "base64"
        }
        self.res = Api().send(req_data).json()  # 修改成员信息成员信息
        pytest.assume(self.res['errmsg'] == 'updated')

    def test_add_member(self):
        userid = "Shen2"
        req_data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
            "headers": None,
            "json": {
                "userid": userid,
                "name": "shenshenshen123",
                "mobile" : "12345678897",
                "department" : [1]
            },
            "encoding": "base64"
        }
        self.res = Api().send(req_data).json()  # 添加成员信息成员信息
        pytest.assume(self.res['errmsg'] == 'created')

    def test_del_member(self):
        userid = "Shen2"
        req_data = {
            "method": "get",
            "url": f"https://test/cgi-bin/user/delete?access_token={self.token}&userid={userid}",
            "headers": None,
            "json": {
                "userid": userid,
                "name": "shenshenshen123",
                "mobile": "12345678897",
                "department": "1"
            },
            "encoding": "base64"
        }
        self.res = Api().send(req_data).json()  # 删除成员信息成员信息
        pytest.assume(self.res['errmsg'] == 'deleted')


if __name__ == '__main__':
    pytest.main(['test_request.py','-sq'])