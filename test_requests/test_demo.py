import requests


def test_demo():
    # 获取 token
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwe653983e4c732493&corpsecret=T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc"
    r = requests.get(url)
    token = r.json()['access_token']
    # 读取成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=sataudays123"
    r = requests.get(url)
    # print(r.json())

    # 更新成员信息
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
    body = {
        "userid": "sataudays123",
        "name": "今天是星期六"}
    r = requests.post(url, json=body)
    # print(r.json())

    # 创建成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    body = {
            "userid": "kenan0012345",
            "name": "柯南0012345",
            "mobile": "+86 13800000900",
            "department": [1],
    }
    r = requests.post(url, json=body)
    # print(r.json())
    # 删除成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=kenan0012345"
    r = requests.get(url)
    print(r.json())
