import base64
import json
from hashlib import md5
from time import sleep

import requests
import urllib3

nas_cert = "/Users/pof/PycharmProjects/workfast/check_status/nas-client-cert.pem"
nas_key = "/Users/pof/PycharmProjects/workfast/check_status/nas-client-key.pem"
woop_cert = "/Users/pof/PycharmProjects/workfast/check_status/client.cert.pem"
woop_key = "/Users/pof/PycharmProjects/workfast/check_status/client.key.nopwd.pem"
nas = (nas_cert, nas_key)
woop = (woop_cert, woop_key)
urllib3.disable_warnings()


class basic_API:
    # nas后台登录
    def get_nas_token(self):
        url = "https://dev-nas.apiteamn.com/api/login"
        body = {"username": "admin",
                "password": "WP-nas2018"}
        r = requests.post(url=url, data=json.dumps(body), cert=nas)
        return r.json()['data']['token']

    # 生产站后台登录！！！！！！！注意
    def get_prod_token(self):
        url = "https://nas.apiteamn.com/api/login"
        body = {"username": "john",
                "password": "c2gU.yYZLh"}
        r = requests.post(url=url, data=json.dumps(body), cert=nas)
        return r.json()['data']['token']

    # 通过后台搜索，获取最新用户johnny*  的display_name
    def get_user_dispalyname(self, nas_token):
        url = "https://dev-nas.apiteamn.com/api/profile/search"
        body = {
            "condition": {
                "tags": [],
                "text": "johnny",
                "gender": 3,
                "min_age": None,
                "max_age": None,
                "status": 0
            },
            "page": 1
        }
        nas_token = "Bearer " + nas_token
        header = {"Authorization": nas_token}
        r = requests.post(url=url, data=json.dumps(body), headers=header, cert=nas)
        return r.json()['data']['profiles'][0]['display_name'][6:]

    # 上传image,获取image的url /api-getway/image
    def image(self, file):
        url = "https://dev.apiteamn.com/api-getway/image"
        with open("/Users/pof/PycharmProjects/HogwartsLG5/backend/" + file, 'rb')as f:
            pic = {"image": ("pic.jpeg", f.read(), "image/jpeg")}
        body = {}
        r = requests.post(url=url, data=body, files=pic, cert=woop)
        return r.json()['data']['url']

    # 注册接口，需要传递johnny * 名字和 图片的url
    # 图片url通过 image接口获取
    def sign_up(self, number, image_url):
        url = "https://dev.apiteamn.com/api-getway/signup"
        user_name = "johnny" + str(number)  # username 是 johnny+number：johnny515
        password = md5(("johnny" + "9BE72424-F231-477D-B4E4-0DEEE7E52606").encode()).hexdigest()
        body = {
            "platform_id": user_name + "@gmail.com",
            "platform": 0,
            "token": password,
            "device": {
                "device_id": "device_" + user_name,
                "device_type": 1,
                "os_version": "6.2.0",
                "device_token": "000000",
                "vpn_on": False,
                "machine": "iphone12.5",
                "language": "en-CN;q=1, zh-Hans-CN;q=0.9, ja-CN;q=0.8",
                "app_build": 60200
            },
            "basic": {
                "display_name": user_name,
                "gender": 1,
                "birthday": "1990-04-09",
                "store": 10,
                "time_zone": "CST",
                "gmt_offset": 28800
            },
            "avatar": {
                "image_name": image_url,
                "width": 1080,
                "height": 1080,
                "face_number": 1
            }
        }
        r = requests.post(url=url, data=json.dumps(body), cert=woop)
        return r.json()

    #  获取图片的实际url
    def get_pic_url(self, img_uri):
        encrypt_src_data = json.dumps({"bucket": "wooplus-stage-img", "key": img_uri})
        encrypt_data = str(encrypt_src_data).encode('utf-8')
        img_uri_encrypted = base64.b64encode(encrypt_data)
        portrait_url = 'https://image.apiteamn.com/' + img_uri_encrypted.decode('utf-8')
        return portrait_url

    # 获取用户状态
    def get_status(self, status, sta):
        list = ["normal", " ", " ", " ", "ban", "delete", "MP-Delete"]
        sta = list[status - 1]
        return sta

    # 获取关联账号
    def get_shared_account(self, ban_id):
        nas_token = basic_API.get_prod_token(self)
        url = "https://nas.apiteamn.com/api/profile/" + ban_id + "/shared_account"
        nas_token = "Bearer " + nas_token
        header = {"Authorization": nas_token}
        r = requests.get(url=url, headers=header, cert=nas)
        account = r.json()['data']['accounts']
        accounts = []
        # accounts.append(ban_id)
        print("关联账号有 " + str(len(account)) + " 个")
        for i in range(0, len(account)):
            if r.json()['data']['accounts'][i]['status'] == 5:
                accounts.append(account[i]['id'])
        print("关联被ban的以及本身" + str(len(accounts)) + " 个,将对接下来的账号进行恢复normal")
        return [len(account), len(accounts), accounts]

    # make_normal 将被ban的账号恢复normal
    def make_normal(self, accounts):
        nas_token = basic_API.get_prod_token(self)
        nas_token = "Bearer " + nas_token
        header = {"Authorization": nas_token}
        body = {
            'current_status': 5,
            'reason': None
        }
        for uid in accounts:
            url = "https://nas.apiteamn.com/api/user/" + str(uid) + "/1"
            r = requests.post(url=url, data=json.dumps(body), headers=header, cert=nas)
            print(r.json())

    # 创建视频id
    def create_video_id(self, token):
        url = "https://dev-nas.apiteamn.com/api-getway/user/create-auth-video"
        token = "Bearer " + token
        headers = {
            'App-Version': 60200,
            "Authorization": token
        }
        r = requests.post(url, headers=headers)
        return r.json()['data']['video_id']

    # upload视频
    def upload_video(self, video, video_id, token):
        url = "https://dev-nas.apiteamn.com/api-getway/user/upload-auth-video"
        token = "Bearer " + token
        headers = {
            'App-Version': 60200,
            "Authorization": token
        }
        body = {
            "video_id": video_id,
            "part_number": 1,
            "video_file": video
        }
        r = requests.post(url=url, data=json.dumps(body), files=video, headers=headers)
        return r.json()

    # 验证上传完成
    def complete_video(self, video_id, token):
        body = {
            "video_id": video_id,
            "part_info": [
                {
                    "part_number": 1,
                    "part_size": 1519868
                }
            ],
            "cover_at": 4000,
            "duration": 10,
            "action_confirm": False  # AI4
        }
        headers = {
            'App-Version': 60200,
            "Authorization": token
        }

    # 更改仅更换主图的用户状态
    def change_photostatus(self, user_id, auth, raw_url, action, recognition):
        url = "https://dev-nas.apiteamn.com/api/portrait_next/handle"
        picture_url = basic_API().get_pic_url(raw_url)
        auth_token = "Bearer " + auth
        header = {"Authorization": auth_token}
        body = {
            "user_id": user_id,
            "album": {
                "portrait_next": {
                    "ver": 0,
                    "src": 0,
                    "pic": None
                },
                "portrait": {
                    "url": picture_url,
                    "raw_url": raw_url,
                    "status": 1,
                    "face_number": 1,
                    "height": 1080,
                    "width": 1080,
                    "created_at": 1622367975000,
                    "handled_by": {
                        "admin": "admin"
                    }
                }
            },
            "action": action,  # action:0 approve ; 1: delete
            "recognition": recognition  # 2030: feel like scam
            # feel like scam(1,2030)   approve(0,null)   porn(1,2040)  no face(1,1010)
            # under age(1,1040)  wrong gender(1,1030)   multi face(1,1020)
            # contact(1,2050)
        }
        r = requests.post(url=url, headers=header, data=json.dumps(body), cert=nas)


# 批量获取用户id
def getuserid_many():
    url = "https://dev.apiteamn.com/api-getway/login"
    password = md5(("johnny" + "9BE72424-F231-477D-B4E4-0DEEE7E52606").encode()).hexdigest()
    user_names = []
    user_ids = []
    for i in range(300, 320):
        user_names.append('johnny' + str(i))
    for user_name in user_names:
        user_name = user_name + "@gmail.com"
        body = {
            "platform_id": user_name,
            "platform": 0,
            "token": password,
            "device": {
                "device_id": "johnny9999",
                "device_type": 3,
                "machine": "postman",
                "language": "en-CN;q=1, zh-Hans-CN;q=0.9, ja-CN;q=0.8",
                "os_version": "1.0.0",
                "device_token": "{{device_token}}",
                "vpn_on": True,
                "app_build": 60200
            }
        }
        r = requests.post(url, json.dumps(body), cert=woop)
        print(r.json())
        user_id = r.json()['data']['user']['user_id']
        user_ids.append(user_id)
    return user_ids


# 批量block
def block_many(user_ids):
    url = "https://dev.apiteamn.com/api-getway/user/block/add"
    auth_token = "Bearer " + "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjIjoxNjI1NjIyODQ2LCJleHAiOjE2MjYyMjc2NDYsImlkIjoiNjBjOTYyZmJlNTQyY2EyMThlMDY3NDUxIiwidiI6MX0.YSadl-HyGMIT5aLGgtCytL5oIx7DHG2vIDPIlkiAEIw"
    header = {"Authorization": auth_token}
    for user_id in user_ids:
        body = {
            "target_id": user_id
        }
        r = requests.post(url=url, headers=header, data=json.dumps(body), cert=woop)
        print(r.json())


# 注册+approve
def signup_approve():
    ba = basic_API()
    nas_token = ba.get_nas_token()  # nas 登录
    num = ba.get_user_dispalyname(nas_token)  # 搜索最新的name序号
    raw_url = ba.image("01.jpeg")  # 上传图片
    signup = ba.sign_up(int(num) + 1, raw_url)  # 注册
    uid = signup['data']['user']['user_id']  # 获取用户id
    ba.change_photostatus(uid, nas_token, raw_url, 0, None)  # approve


# 注册+强制认证
def signup_tbv():
    ba = basic_API()
    nas_token = ba.get_nas_token()  # nas 登录
    num = ba.get_user_dispalyname(nas_token)  # 搜索最新的name序号
    raw_url = ba.image("01.jpeg")  # 上传图片
    signup = ba.sign_up(int(num) + 1, raw_url)  # 注册
    uid = signup['data']['user']['user_id']  # 获取用户id
    ba.change_photostatus(uid, nas_token, raw_url, 1, 2030)  # tbv


# 批量注入视频
def authvideo():
    ba = basic_API()
    nas_token = ba.get_nas_token()  # nas 登录
    uids = getuserid_many()



if __name__ == "__main__":
    ba = basic_API()
    ban_id = "6002698378254500b9eb66d1"  # 6079336ad0845d2d5d603e2a johnnyR
    accounts = ba.get_shared_account(ban_id)
    print(accounts)
    ba.make_normal(accounts)

