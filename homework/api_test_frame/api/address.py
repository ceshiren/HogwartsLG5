from homework.api_test_frame.api.base import Base


class Address(Base):
    def add_member(self, userid, username, mobile, department: list, **kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        json_data = {
            "userid": userid,
            "name": username,
            "mobile": mobile,
            "department": department
        }
        json_data.update(kwargs)
        return self.send("post", url, json=json_data)

    def get_member(self, userid):
        userid = userid
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        return self.send("get", url)

    def update_member(self, userid, username, mobile, department, **kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        json_data = {
            "userid": userid,
            "name": username,
            "department": department,
            "mobile": mobile
        }
        json_data.update(kwargs)
        return self.send("post", url, json=json_data)

    def delete_member(self, userid):
        userid = userid
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        return self.send("get", url)
