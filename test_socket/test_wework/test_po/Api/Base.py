import requests


class Base:
    def __init__(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww5d15687c2406f974&corpsecret=wZXvdAvDl2aRhvqKRIeF7bpApQ5v1iF3MsZNrw48xrk'
        r = requests.get(url)
        self.token = r.json()['access_token']
        # print(self.token)
        self.session = requests.Session()
        self.session.params={'access_token': self.token}

    def send(self,*wargs,**kwargs):
        r = self.session.request(*wargs,**kwargs)
        return r.json()
