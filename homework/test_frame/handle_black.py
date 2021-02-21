import yaml
from appium.webdriver.common.mobileby import MobileBy


def handle_black(fun):
    def run(*args, **kwargs):
        # black_list = [(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
        # 从yaml文件中读取black list
        with open("../black_list.yaml", "r", encoding="utf-8") as f:
            black_list = yaml.safe_load(f)
        param_1 = args[0]
        param_2 = args[1]
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            # 循环遍历黑名单列表，如果存在，那么对黑名单元素进行处理：点击关闭弹窗
            for black in black_list:
                eles = param_1.driver.find_elements(*black)
                if len(eles) > 0:
                    eles[0].click()
                # 处理黑名单后再次查找
                # return self.find(locator)
                # return fun(*args, **kwargs)
                return param_1.find(param_2)
            raise e
    return run
