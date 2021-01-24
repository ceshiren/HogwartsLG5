import yaml


def handle_black(fun):
    def run(*args,**kwargs):
        instance = args[0]
        with open("../black_list.yml","r",encoding="utf-8") as f:
            #黑名单或弹窗列表
            black_lists = yaml.load(f)
        #捕获异常，元素没有找到
        try:
            return fun(*args,**kwargs)
        except Exception as e:
            #如果元素没有被找到，就会进行遍历黑名单
            for black in black_lists:
                #如果发现黑名单中的元素存在
                eles = instance.driver.find_elements(*black)
                #对黑名单元素进行处理
                if len(eles) > 0:
                    #通过点击的方式，关闭弹窗
                    eles[0].click()
                    #处理完成之后，就会再次进行查找
                    return fun(*args,**kwargs)
                raise e
    return run
