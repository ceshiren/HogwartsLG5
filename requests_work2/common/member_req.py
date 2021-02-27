from requests_work2.common.base import Api


class Member(Api):
    def get_member(self,userid):
        req_data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}",
            "headers": None,
            "json": None,
            "encoding": "base64"
        }
        return self.send(req_data)

    def add_member(self,userid,name,phone,depid:list):
        req_data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "headers": None,
            "json": {
                "userid": userid,
                "name": name,
                "mobile": phone,
                "department": depid
            },
            "encoding": "base64"
        }
        return self.send(req_data)

    def update_member(self,userid,name):
        req_data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "headers": None,
            "json": {
                'userid': userid,
                'name': name
            },
            "encoding": "base64"
        }
        return self.send(req_data)

    def del_member(self,userid):
        req_data = {
            "method": "get",
            "url": f"https://test/cgi-bin/user/delete?userid={userid}",
            "headers": None,
            "json": None,
            "encoding": "base64"
        }
        return self.send(req_data)