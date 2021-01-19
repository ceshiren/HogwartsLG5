# -*- coding: utf-8 -*-
# @time     : 2021/1/19 23:28
# @Author   : Owen
# @File     : black_element.py
from appium.webdriver.common.mobileby import MobileBy


def black_element(fun):
    def run(*args, **kwargs):
        _blacklist = [(MobileBy.ID, "iv_close")]
        instance = args[0]
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            for black in _blacklist:
                elements = instance.driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return fun(*args, **kwargs)
            raise e
    return run