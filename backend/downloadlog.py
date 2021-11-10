import os
import sys

import boto3

def download(args):
    s3 = boto3.resource('s3')
    # print("输入时间（空格）用户id，例如：2021-02-20 57ea449d7748abb7428b456a")
    # t_u = args.args[0]
    print(args)
    download_path = '/Users/pof/PycharmProjects/HogwartsLG5/'  # 修改为自己的保存路径
    log = 'wooplus-prod-client-log'
    t = '/' + args[0]
    user_id = '/' + args[1]
    Prefix = 'logs' + t + user_id
    my_bucket = s3.Bucket(log)
    lists = []
    dir = ""
    for obj in my_bucket.objects.filter(Prefix=Prefix):
        dir = download_path + obj.key[:len('logs/2021-02-20/')]
        if not os.path.exists(dir):
            os.makedirs(dir)
            os.makedirs(dir + args[1] + "_sql")
        if obj.key not in lists and obj.key[-3:] != "txt":
            lists.append(obj.key)
    lists.reverse()
    list_download = []   # 存要下载的文件名
    list_after = []   # 存后缀用于去重
    for i in lists:   # 进行去重，去重后的文件名加入到要下载的数组中
        if i[-2:] not in list_after:
            list_after.append(i[-2:])
            list_download.append(i)
    if len(list_download) == 0:
        print("未获取到日志，可能日志上传失败，重新输入新的日期和id")
        return 0

    if len(list_download) >= 20:
        print("日志大于20条，联系John修改代码")
        return 0

    for i in list_download:
        s3.Bucket("wooplus-prod-client-log").download_file(i, download_path + i)

    # 将大于10的日志处理为 90，91...
    if len(list_download) >= 10:
        print("日志大于10条，稍等.....")
        for i in range(0, len(list_download)):
            if list_download[i][-2] == '1':
                ls = list(list_download[i])
                ls[-2] = '9'
                x = ''.join(ls)
                os.system("mv " + download_path + list_download[i] + " " + download_path + x)
    # 大于20还未处理，遇到再进行处理 :insert 9
    zip_name = download_path + list_download[0][:-2]
    zip_path = dir
    os.system("cat " + zip_name + ".* > " + zip_name)
    zip_commend = "unzip -o " + zip_name + " -d " + zip_path + args[1] + "_sql"
    os.system(zip_commend)
    os.system("rm -f " + zip_name + ".*")
    # os.system("rm -f " + zip_name)
    # return zip_path + args[1] + "_sql"
    return zip_name

if __name__ == "__main__":
    args = sys.argv
    download(args)


