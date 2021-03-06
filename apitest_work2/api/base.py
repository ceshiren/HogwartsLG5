import requests


class Base:
    def __init__(self):
        # 获取token的接口,corpid 企业id，corpsecret，管理工具，通讯录工具，Secret
        data = {
            'corpid': 'ww8d98917c9b215d4f',
            'corpsecret': 'nT7v7PK2j_-dazQZ90v9N-44hEa9hzwBmGmpJbGeWno'
        }
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        r = requests.get(url, params=data).json()
        self.token = r['access_token']
        # 声明一个session
        self.request_session = requests.Session()
        # 把token放入到session中,每次参数都有token
        self.request_session.params = {'access_token': self.token}


    def send(self, *args, **kwargs):
        # 用 session
        r = self.request_session.request(*args, **kwargs)
        return r.json()