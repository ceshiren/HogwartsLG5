import requests

class Test_qyweixin_api:
    def get_token(self):
        data = {
            'corpid': 'ww8d98917c9b215d4f',
            'corpsecret': 'nT7v7PK2j_-dazQZ90v9N-44hEa9hzwBmGmpJbGeWno'
        }
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        r = requests.get(url, params=data)
        token = r.json()['access_token']
        return token

    def test_add_user(self):
        data = {'access_token': self.get_token()}
        body_json = {
            "userid": "test01",
            "name": "测试1号",
            "mobile": "+86 18100000001",
            "department": [1]
        }
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        r = requests.post(url, params=data, json=body_json)
        print(r.json())

    def test_get_user(self):
        data = {
            'access_token': self.get_token(),
            'userid': 'test01'
        }
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        r = requests.get(url, params=data)
        print(r.json())

    def test_update_user(self):
        data = {
            'access_token': self.get_token()}
        body_json = {
            "userid": "test01",
            "name": "测试1号修改",
            # "mobile": "+86 18100000001",
            # "department": [1]
        }
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        r = requests.post(url, params=data, json=body_json)
        print(r.json())

    def test_delete_user(self):
        data = {
            'access_token': self.get_token(),
            'userid': 'test01'
        }
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        r = requests.get(url, params=data)
        print(r.json())
