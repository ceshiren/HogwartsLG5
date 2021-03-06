from apitest_work2.api.base import Base


class Address(Base):

    def add_member(self, userid, name: str, mobile: str, department: list, **kwargs):
        # 创建成员
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        body.update(kwargs)
        return self.send("post", url, json=body)

    def get_member(self, userid):
        # 获取成员
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        return self.send("get", url)

    def update_member(self, userid, name: str, **kwargs):
        # 更新成员信息
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        body = {
            "userid": userid,
            "name": name
        }
        header = {"cpntent-type": "application/json"}
        body.update(kwargs)
        return self.send("post", data=body, headers=header)

    def delete_member(self, userid: str):
        # 删除成员
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        return self.send("get", url)