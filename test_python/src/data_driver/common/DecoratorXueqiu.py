import os

import yaml


def black_list(fun):
    def inner(*args, **kwargs):
        instance = args[0]
        path = os.path.dirname(__file__).strip("common").__add__("datas/blacklist.yaml")
        with open(path, 'r', encoding="utf-8") as f:
            blacks = yaml.safe_load(f)
        # print("yaml 测试"+str(blacks))

        try:
            return fun(*args, **kwargs)
        except Exception as e:
            for black in blacks:
                eles = instance.driver.find_elements(*black)
                # 对黑名单元素进行处理
                if len(eles) > 0:
                    for ele in eles:
                        # 通过点击的方式，关闭弹窗
                        ele.click()
                        # 再次查找
                        try:
                            return fun(*args, **kwargs)
                        except:
                            pass
            raise e

    return inner
