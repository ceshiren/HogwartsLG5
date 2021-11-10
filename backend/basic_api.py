import base64
import json
import os
from hashlib import md5
from time import sleep
import redis
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

    # 通过后台搜索，获取最新用户johnny*  的display_name数
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
    def login(self, uname, password):
        url = "https://dev-nas.apiteamn.com/api-getway/login"
        body = {
            "platform_id": uname + '@gmail.com',
            "platform": 0,
            "token": password,
            "device": {
                "device_id": "device_"+str(uname),
                "device_type": 3,
                "machine": "iphone7",
                "language": "en-CN;q=1, zh-Hans-CN;q=0.9, ja-CN;q=0.8",
                "os_version": "1.0.0",
                "device_token": "000000",
                "vpn_on": False,
                "app_build": 60200
            }
        }
        r = requests.post(url, json.dumps(body), cert=woop)

    """
        desc: 批量创建会话
        params: uid:被会话的人的id
                number：需要建立会话的条数。通过读取token文档，选取auto_test进行建立
                type: 会话建立类型 2-Say Hi会话；4-Vip会话
        use: create_chat('6124704ae5d21dbf9a5e49cf'，50)
        return： null
    """
    def create_chat(self, uid, number, chat_type):
        basic_API().refresh_token(number)
        with open('./user_data/user_token.txt', 'r') as f:
            tokens = f.readlines()
        url = "https://dev.apiteamn.com/api-getway/conversation/create"
        for i in range(0, number):
            auth_token = tokens[i].replace("\n", "")
            header = {"Authorization": auth_token}
            body = {
                "target_id": uid,
                "type": chat_type,  # 2-Say Hi  4-VIP会话
            }
            r = requests.post(url=url, headers=header, data=json.dumps(body), cert=woop)
            print(r.json())
            # sleep(1)

    """
        desc: 批量like
        params: token：需要进行like一堆人的用户token
        use: like_many(eyJhbGciOiJIUzI1NiIsInR5cCI6... ，50)
        return： null
    """
    def like_many(self, token, number):
        basic_API().refresh_token(number)
        url = "https://dev.apiteamn.com/api-getway/cards/slide"
        auth_token = "Bearer " + token
        header = {"Authorization": auth_token}
        with open('./user_data/user_id.txt', 'r') as f:
            ids = f.readlines()
        for i in range(0, number):
            user_id = ids[i].replace("\n", "")
            body = {
                    'match_type': 0,
                    "liked": [user_id],
            }
            r = requests.post(url=url, headers=header, data=json.dumps(body), cert=woop)
            # print(r.json())

    """
        desc: 批量block
        params: token：需要进行block一堆人的用户token
        use: block_many(eyJhbGciOiJIUzI1NiIsInR5cCI6... ，50)
        return： null
    """
    def block_many(self, token, number):
        basic_API().refresh_token(number)
        url = "https://dev.apiteamn.com/api-getway/user/block/add"
        auth_token = "Bearer " + token
        header = {"Authorization": auth_token}
        with open('./user_data/user_id.txt', 'r') as f:
            ids = f.readlines()
        for i in range(0, number):
            user_id = ids[i].replace("\n", "")
            body = {
                "target_id": user_id
            }
            r = requests.post(url=url, headers=header, data=json.dumps(body), cert=woop)
            # print(r.json())

    """
        desc: 被批量like
        params: userid：被批量like的一群人
                number：需要被like的数量
        use:beliked_many(6124704fe5d21dbf9a5e49d3，50)
        return： null
    """
    def beliked_many(self, userid, number):
        basic_API().refresh_token(number)
        with open('./user_data/user_token.txt', 'r') as f:
            tokens = f.readlines()
        # with open('./user_data/user_name.txt', 'r') as f2:
        #     names = f2.readlines()
        url = "https://dev.apiteamn.com/api-getway/cards/slide"
        for i in range(0, number):
            auth_token = tokens[i].replace("\n", "")
            # name = names[i].replace('\n', '')
            header = {"Authorization": auth_token}
            bodys = {
                        'match_type': 0,
                        "liked": [userid],
                     }
            r = requests.post(url=url, headers=header, data=json.dumps(bodys),
                              cert=woop)
            # print(r.json())
            # print(f"ok!{name} liked you!")
            # sleep(1)

    """
        desc: 批量点赞moment
        params: number：需要被like的数量
                moment_id，media_id：当前moment则相同，点赞他人评论，则media_id为评论的id
                target_author：作者的id，名字，性别
        use:  ba.moment_like(100, "611f27bf20c513ef91a91b17", "611f27bf20c513ef91a91b17",
                    ["611e1b53935e8dded0b6b2e5", "Ashley2045", 2])
        return： null
    """
    def moment_like(self, number, moment_id, media_id, target_author):
        basic_API().refresh_token(number)
        with open('./user_data/user_token.txt', 'r') as f:
            tokens = f.readlines()
        url = "https://dev.apiteamn.com/api-getway/moment/like"
        body = {
                "moment_id": moment_id,
                "media_id": media_id,
                "target_author": {
                    "id": target_author[0],
                    "name": target_author[1],
                    "gender": target_author[2]
                }
        }
        for i in range(0, number):
            auth_token = tokens[i].replace("\n", "")
            header = {"Authorization": auth_token}
            r = requests.post(url=url, headers=header, data=json.dumps(body), cert=woop)
            print(r.json())

        """
            desc: 评论moment
            params: number：需要被like的数量
                    moment_id，media_id：当前moment则相同，点赞他人评论，则media_id为评论的id
                    target_author：作者的id，名字，性别
            use:  ba.moment_like(100, "611f27bf20c513ef91a91b17", "611f27bf20c513ef91a91b17",
                        ["611e1b53935e8dded0b6b2e5", "Ashley2045", 2])
            return： null
        """
    def comment_moment(self, number, moment_id, media_id, target_author):
        basic_API().refresh_token(number)
        with open('./user_data/user_token.txt', 'r') as f:
            tokens = f.readlines()
        url = "https://dev.apiteamn.com/api-getway/moment/comment"
        body = {
                "moment_id": moment_id,
                "media_id": media_id,  # 一级评论id
                # "content": "😭nancy,我好艰难啊",
                "content": "👿我，秦始皇，打钱╭(╯ε╰)╮",
                "target_author": {
                    "id": target_author[0],
                    "name": target_author[1],
                    "gender": target_author[2],
                    "avatar": None,
                    "deep_link": None
                }
                # "reference": {  # 要at的评论的作者
                #     "author": {
                #         "id": target_author[0],
                #         "name": target_author[1],
                #         "gender": target_author[2]
                #     },
                #     "id": target_author[0],  # 要at的评论id
                #     "content": "好耶"  # 要at的评论内容
                # }
        }
        for i in range(0, number):
            auth_token = tokens[i].replace("\n", "")
            header = {"Authorization": auth_token}
            r = requests.post(url=url, headers=header, data=json.dumps(body), cert=woop)
            print(r.json())

    """
        desc: 发送moment
        params: number：需要发送的数量
        use:  send_moment(10)
        return： null
    """
    def send_moment(self, number):
        url = "https://dev.apiteamn.com/api-getway/moment/"
        body = {
            "kind": 100,
            "topic_id": "5e17e49be39d588c891e6459",
            "photos": [{
                "url": "2021/09/10/613b1740b8fe285af4cfa4d2",
                "width": 1365,
                "height": 1024
            }],
            "location": {
                "lat": 30.5971505,
                "lon": 104.0608851
            },
            "address": "Chengdu Shi, Sichuan Sheng, China"
        }
        with open('./user_data/user_token.txt', 'r') as f:
            tokens = f.readlines()
        for i in range(0, number):
            token = tokens[i].replace("\n", "")
            header = {"Authorization": token}
            r = requests.post(url=url, headers=header, data=json.dumps(body), cert=woop)
            print(r.json())

    # 更新token
    def refresh_token(self, num):
        url = "https://dev.apiteamn.com/api-getway/login"
        password = md5(("johnny" + "9BE72424-F231-477D-B4E4-0DEEE7E52606").encode()).hexdigest()
        user_names = []
        with open("./user_data/user_token.txt", 'w') as clear_f:
            clear_f.write("")
        for i in range(0, num):
            user_names.append('johnny_autotets' + str(i))
        for user_name in user_names:
            user_name = user_name + "@gmail.com"
            body = {
                "platform_id": user_name,
                "platform": 0,
                "token": password,
                "device": {
                    "device_id": "device_" + user_name,
                    "device_type": 3,
                    "machine": "postman",
                    "language": "en-CN;q=1, zh-Hans-CN;q=0.9, ja-CN;q=0.8",
                    "os_version": "1.0.0",
                    "device_token": "{{device_token}}",
                    "vpn_on": True,
                    "app_build": 60400
                }
            }
            r = requests.post(url, json.dumps(body), cert=woop)
            # print(r.json())
            token = r.json()['data']['token']
            auth_token = "Bearer " + token
            with open("./user_data/user_token.txt", 'a') as f3:
                f3.write(auth_token + '\n')

    # 连接redis
    def connect_redis(self):
        r = redis.StrictRedis(host='stage.z1p6ym.ng.0001.ape1.cache.amazonaws.com', port=6379, db=0)

     #清空redis的ly数据，用于创造free trail
    def delete_ly_data(self):
        pass




if __name__ == "__main__":
    ba = basic_API()
    # ban_id = "6002698378254500b9eb66d1"  # 6079336ad0845d2d5d603e2a johnnyR
    # accounts = ba.get_shared_account(ban_id)
    # print(accounts)
    # ba.make_normal(accounts)

    ba.connect_redis()

