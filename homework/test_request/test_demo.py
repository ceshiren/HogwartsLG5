import requests

class TestApi:
    def setup_class(self):
        corpid = "wwa8c3f49624d81cd9"
        corpsecret = "NNdFue-cBIv0l5m60EvwcY22syS9Yv5ONHhhHjWo3hk"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url)
        self.token = r.json()["access_token"]

    def test_add_member(self):
        # 通讯录增加成员
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        json_data = {
            "userid": "wangwu01",
            "name": "王五01",
            "alias": "wangwu01",
            "mobile": "+86 13800000000",
            "department": [1, 2]
        }
        r = requests.post(url, json=json_data)
        print(r.json())

    def test_query_member(self):
        # 查询成员信息
        userid = "wangwu01"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}"
        r = requests.get(url)
        print(r.json())

    def test_update_member(self):
        # 更新成员信息
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        json_data = {
            "userid": "wangwu01",
            "name": "张五",
            "department": [1],
            "mobile": "13800000001"
        }
        r = requests.post(url, json=json_data)
        print(r.json())

    def test_delete_member(self):
        # 删除成员信息
        userid = "wangwu01"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
        r = requests.get(url)
        print(r.json())
