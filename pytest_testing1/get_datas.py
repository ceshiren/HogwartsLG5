# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 16:35
# @Author  : Yan
# @Email   : 13433183608@163.com
# @File    : get_datas.py

import yaml

def get_datas():

    with open("./datas/calc_data.yaml") as f:
        datas = yaml.safe_load(f)

        return datas
        # print(datas)


if __name__ == '__main__':
    get_datas()