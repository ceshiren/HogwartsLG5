import json
import yaml

import requests
import base64
"""
·需要二次封装requests，对请求j进行定制化
·将请求结构体url从一个写死ip替换成动态域名
·使用env配置文件，存放环境配置信息
·将请求结构中的url替换未env配置文件中的url
·将env配置文件使用yaml进行管理
"""
class Api:

    corpid = "wwb341710801ade2f6"
    corpsecret = "6wJxVZUKmLrAJTBiD7p21twm2Fiy7NZWkAxI6HtDSV0"
    req_data = {
        "method": "get",
        "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}",
        "headers": None,
        "json": None,
        "encoding": "base64"
    }

    with open('../common/env.yaml','r')as f:
        env = yaml.safe_load(f)

    def __init__(self):
        self.token = requests.get(self.req_data['url']).json()['access_token']  # 拿到token信息
        self.req_session = requests.Session()
        self.req_session.params = {'access_token': self.token}

    def send(self,data:dict):
        data['url'] = str(data['url']).replace('test',self.env['test_studio'][self.env['defult']])
        res = self.req_session.request(method=data['method'],url=data['url'],headers=data['headers'],json=data['json'])
        return res.json()