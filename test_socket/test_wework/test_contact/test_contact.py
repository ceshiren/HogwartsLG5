import pytest
import requests


class Test_Contact:
    def test_contact(self):
        url='https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww5d15687c2406f974&corpsecret=wZXvdAvDl2aRhvqKRIeF7bpApQ5v1iF3MsZNrw48xrk'
        r = requests.get(url)
        self.token = r.json()['access_token']
        print(self.token)

        url=f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}'
        body={
            "userid":"userid",
            "name":"wg228",
            "mobile":"12312312324",
            "department":[7]
        }
        r = requests.post(url,json=body)
        print(r.json())

        url=f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid=userid'
        r = requests.get(url)
        print(r.json())

        url=f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        body={
            "userid": "userid",
            "name": "wg228",
            "mobile": "12312312324",
            "department": [6]
        }
        r = requests.post(url,json=body)
        print(r.json())

        url=f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid=userid'
        r = requests.get(url)
        print(r.json())