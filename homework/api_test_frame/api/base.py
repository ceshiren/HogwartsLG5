import requests


class Base:
    def __init__(self):
        # 获取token
        corpid = "wwa8c3f49624d81cd9"
        corpsecret = "NNdFue-cBIv0l5m60EvwcY22syS9Yv5ONHhhHjWo3hk"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url)
        self.token = r.json().get("access_token")
        # 声明一个Session
        self.session = requests.Session()
        # 把token放入到session中，每次参数都会有token
        self.session.params = {"access_token": self.token}

    def send(self, *args, **kwargs):
        # request使用session去发送，那么每次在发送url中就会带上session
        r = self.session.request(*args, **kwargs)
        return r.json()
