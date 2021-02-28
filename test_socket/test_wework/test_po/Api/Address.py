import requests

from test_socket.test_wework.test_po.Api.Base import Base


class Address(Base):

    def add_member(self, userid: str, name: str, mobile: int, department: list) -> object:
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}'
        body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = self.send(method="post",url=url, json=body)
        return r

    def query_member(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid=userid'
        r = self.send(method="get",url=url)
        return r

    def modify_member(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        body = {
            "userid": "userid",
            "name": "wg228",
            "mobile": "12312312324",
            "department": [6]
        }
        r = self.send(method="post",url=url, json=body)
        return r

    def delete_member(self,userid):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}'
        r = self.send(method='get',url=url)
        return r