import json
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import *

POLL_FREQUENCY = 0.5
TIMEOUT = 30
class BasePage:
    _params = {}#sendkeys动态传入
    _black_list = [('id','image_cancle')]#弹窗黑名单
    _error_count = 0#初始计数
    _max_count = 10#最大计数
    _driver = WebDriver
    def __init__(self,driver:WebDriver=None):
        self._driver = driver

    def quit(self):
        '''退出浏览器'''
        self._driver.quit()

    def refresh(self):
        '''刷新浏览器'''
        self._driver.refresh()

    def get(self,url=''):
        '''打开浏览器'''
        if url != '':
            print('传了url')
            self._driver.get(url)
        else:pass

    def write_cookie_for_json(self,path='cookie.json'):
        '''拿到cookies写入指定的JSON文件'''
        try:
            cookies = self._driver.get_cookies()
            with open(path,'w',encoding='utf-8')as f:
                json.dump(cookies,f)#写入JSON
        except Exception as e:
            print('cookies 写入JSON失败，请检查路径...')
            raise e

    def add_cookie(self,path='cookie.json'):
        '''从指定JSON读取cookies，并写入打开的浏览器页面cookie'''
        try:
            with open(path,'r',encoding='utf-8') as f:
                cookies = json.load(f)
            for cookie in cookies:
                self._driver.add_cookie(cookie)
        except Exception as e:
            print('添加cookie失败...')
            raise e

    def find_element_by_ui(self,key,value):
        '''
        判断元素存在返回元素对象,通过android_uiautomator
        :param locator: 元素
        :return: 元素对象/false
        '''
        elem = WebDriverWait(self._driver,timeout=TIMEOUT,poll_frequency=POLL_FREQUENCY).until(lambda x : x\
                .find_element_by_android_uiautomator('new UiSelector().'+key+'("'+value+'")'))
        return elem

    def scroll_find_element(self,text):
        '''app滚动查找元素'''
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector().'
                   'scrollable(true).instance(0)).'
                   'scrollIntoView(new UiSelector().'
                   f'text("{text}").instance(0));')
        self.find_and_click(element)

    def find_element(self,locator):
        '''
        定位一个元素
        :param locator: 传的元素，元祖类型，key定位类型，value元素值
        :return:返回元素对象/False
        '''
        try:
            ele = WebDriverWait(self._driver,timeout=TIMEOUT,poll_frequency=POLL_FREQUENCY).\
                until(EC.presence_of_element_located(locator))
            return ele
        except:
            print('未找到元素》》》》》》》》》》》》》》》》》》，返回None')
            return False

    def find_elements(self,locator):
        '''
        定位一组元素
        :param locator: 传的元素，元祖类型，key定位类型，value元素值
        :return:返回元素对象/None
        '''
        try:
            eles = WebDriverWait(self._driver,timeout=TIMEOUT,poll_frequency=POLL_FREQUENCY).\
                until(lambda x: x.find_elements(*locator))
            return eles
        except:
            print('未找到元素》》》》》》》》》》》》》》》》》》，返回None')
            return False

    def find(self,locator):
        '''屏蔽黑名单弹窗封装'''
        try:
            ele = self.find_element(locator)
            self._error_count = 0
            return ele
        except Exception as e:
            self._error_count+=1
            if self._error_count >= self._max_count:
                raise e
            for black in self._black_list:
                eles = self.find_elements(black)
                if len(eles) > 0:
                    eles[0].click()
                    return self.find(locator)
            return e

    def send(self,locator,value):
        '''输入内容，如果存在弹窗关闭弹窗'''
        try:
            self.find(locator).send_keys(value)
            self._error_count = 0
        except Exception as e:
            self._error_count+=1
            if self._error_count >= self._max_count:
                raise e
            for black in self._black_list:
                eles = self.find_elements(black)
                if len(eles) > 0:
                    eles[0].click()
                    return self.send(locator,value)
            return e

    def click_new(self,locator):
        '''输入内容，如果存在弹窗关闭弹窗'''
        try:
            self.find(locator).click()
            self._error_count = 0
        except Exception as e:
            self._error_count+=1
            if self._error_count >= self._max_count:
                raise e
            for black in self._black_list:
                eles = self.find_elements(black)
                if len(eles) > 0:
                    eles[0].click()
                    return self.click_new(locator)
            return e

    def open_yaml(self,path):
        with open(path, encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    def steps(self,path='../page/main.yaml'):
        '''封装数据驱动，通过关键字驱动操作'''
        with open(path, encoding='utf-8') as f:
            step_yaml:list[dict] = yaml.load(f, Loader=yaml.FullLoader)
            print(f'yaml数据：{step_yaml}')
            for step in step_yaml:
                if 'by' in step.keys():
                    locator = (step['by'],step['locator'])
                if 'action' in step.keys():
                    if 'click' == step['action']:
                        self.click_new(locator)
                    if 'send' == step['action']:
                        content:str = step['value']
                        for param in self._params:
                            content = content.replace(f'{param}',self._params[param])
                        self.send(locator,content)
                else:
                    print('不存在操作，返回元素对象本身')
                    return  self.find(locator)

    def get_attribute(self,locator,value='value'):
        '''拿到元素的value'''
        try:
            elem_value = self.find_element(locator).get_attribute(value)#试着找到元素的value
            return elem_value#有值返回具体内容
        except:
            print('没有attribute值')
            return None#没值返回None

    def get_text(self, locator):
        '''获取元素的文本'''
        try:
            elem_text = self.find_element(locator).text
            return elem_text  # 有值返回具体内容
        except:
            print('没有text值')
            return None  # 没值返回None

    def get_loaction(self, locator):
        '''获取元素的坐标'''
        try:
            elem_location = self.find_element(locator).location
            return elem_location  # 有值返回具体内容
        except:
            print('没有location值')
            return None  # 没值返回None

    def get_size(self, locator):
        '''获取元素的尺寸'''
        try:
            elem_size = self.find_element(locator).size
            return elem_size  # 有值返回具体内容
        except:
            print('没有size值')
            return None  # 没值返回None

    def sendkeys(self,locator,text):
        '''输入内容'''
        try:
            ele = self.find_element(locator)
            ele.send_keys(text)
        except Exception as e:
            print('未找到输入元素')
            raise e

    def clicks(self,locator):
        '''点击元素'''
        try:
            ele = self.find_element(locator)
            ele.click()
        except Exception as e:
            print('未找到点击元素')
            raise e


    def clear(self,locator):
        '''清空内容'''
        ele = self.find_element(locator)
        elem_value = self.get_element_value(locator)
        if elem_value != None:
            ele.clear()
        else:
            return False

    def is_selected(self,locator):
        '''判断元素是否被选中,返回bool'''
        ele = self.find_element(locator)
        if ele:
            return ele.is_selected()
        else:
            return False

    def is_displayed(self,locator):
        '''判断元素是否可见,返回bool'''
        ele = self.find_element(locator)
        if ele:
            return ele.is_displayed()
        else:
            return False

    def is_enabled(self,locator):
        '''判断元素是否可用,返回bool'''
        ele = self.find_element(locator)
        if ele:
            return ele.is_enabled()
        else:
            return False

    def is_element_exist(self,locator):
        '''判断一个元素是否存在,返回对象或False'''
        if self.find_element(locator):
            return True
        else:
            return False

    def is_elements_exist(self,locator):
        '''判断一组元素是否存在，返回 一个/多个对象，else False'''
        ele = self.find_elements(locator)
        if len(ele)==1:
            return True
        elif len(ele)>1:
            print(f'定位到多个元素：{ele}')
            return True
        else:
            return False

    def title_is(self,title):
        '''判断预期标题和实际标题是否一致，bool返回值'''
        try:
            res = WebDriverWait(self._driver,timeout=TIMEOUT,poll_frequency=POLL_FREQUENCY).\
                until(EC.title_is(title))
            return res
        except:
            return False

    def title_contains(self, title):
        '''判断预期标题是否包含实际标题，bool返回值'''
        try:
            res = WebDriverWait(self._driver,timeout=TIMEOUT,poll_frequency=POLL_FREQUENCY).\
                until(EC.title_contains(title))
            return res
        except:
            return False

    def text_in_element(self,locator, text):
        '''判断元素是否存在text，bool返回值'''
        try:
            res = WebDriverWait(self._driver,timeout=TIMEOUT,poll_frequency=POLL_FREQUENCY).\
                until(EC.text_to_be_present_in_element(locator,text))
            return res
        except:
            return False

    def is_visibility_of_element_located(self,locator):
        '''
        判断元素是否可见，可见返回元素对象，不可见返回false
        :param locator: 元素
        :return: 元素对象/false
        '''
        try:
            result = WebDriverWait(self._driver,timeout=TIMEOUT,poll_frequency=POLL_FREQUENCY).until\
                (EC.visibility_of_any_elements_located(locator))
            return result
        except:
            return False

    def is_invisibility_of_element_located(self,locator):
        '''
        判断元素是否隐藏，找得到返回False，找不到或隐藏返回true
        :param locator: 元素
        :return: true/false
        '''
        try:
            result = WebDriverWait(self._driver,timeout=TIMEOUT,poll_frequency=POLL_FREQUENCY).until\
                (EC.invisibility_of_element_located(locator))
            return result
        except:
            return False

    def is_text_to_be_present_in_element(self,locator,_text):
        '''
        判断元素的text是否包含字符串
        :param locator: 元素
        :param _text: 预期字符串
        :return: true/false
        '''
        try:
            result = WebDriverWait(self._driver,timeout=TIMEOUT,poll_frequency=POLL_FREQUENCY).until\
                (EC.text_to_be_present_in_element(locator,_text))
            return result
        except:
            return False

    def is_text_to_be_present_in_element_value(self,locator,_text):
        '''
        判断元素的value是否包含字符串
        :param locator: 元素
        :param _text: 预期字符串
        :return: true/false
        '''
        try:
            result = WebDriverWait(self._driver,timeout=TIMEOUT,poll_frequency=POLL_FREQUENCY).until\
                (EC.text_to_be_present_in_element_value(locator,_text))
            return result
        except:
            return False

    def is_element_to_be_clickable(self,locator):
        '''
        判断元素是否可被点击，可以点击返回元素对象，需要元素可见且可被调用
        :param locator:元素
        :return:元素对象/false
        '''
        try:
            result = WebDriverWait(self._driver,timeout=TIMEOUT,poll_frequency=POLL_FREQUENCY).until\
                (EC.element_to_be_clickable(locator))
            return result
        except:
            return False

    def is_frame_to_be_available_and_switch_to_it(self,locator):
        '''
        判断frame是否switch进去，能被切入返回ture
        :param locator:元素
        :return:true且switch进去/false
        '''
        try:
            result = WebDriverWait(self._driver,timeout=TIMEOUT,poll_frequency=POLL_FREQUENCY).until\
                (EC.frame_to_be_available_and_switch_to_it(locator))
            return result
        except TimeoutException:
            return "元素找不到"
        except NoSuchFrameException:
            return "元素切不过去"

    def is_staleness_of(self,locator):
        '''
        判断元素是否被移除,没有移除返回False，移除了返回true
        :param locator:元素
        :return:True/false
        '''
        try:
            result = self.findElement(locator).is_enabled()
            return False
        except:
            if TimeoutException:
                return "元素找不到了，已经不在当前页面"
            elif StaleElementReferenceException:
                return "元素不在当前页面"
            else:
                return True

    def is_alert_is_present(self):
        '''
        判断alert是否存在，存在返回alert.text，不存在返回false
        :return:alert.text/false
        '''
        try:
            result = WebDriverWait(self._driver,timeout=TIMEOUT,poll_frequency=POLL_FREQUENCY).until\
                (self._driver.switch_to.alert.text)
            return result
        except:
            return False

    def get_window_rect(self):
        '''
        获取窗口的比例和位置
        rect{'width': 720, 'height': 1280, 'x': 0, 'y': 0}
        :return:
        '''
        res = self._driver.get_window_rect()
        width = res['width']
        height = res['height']
        return width,height

    def swipe(self,locator,start_x,start_y,end_x,end_y,duration):
        '''
        滑动屏幕
        :param start_x: 第一点x轴
        :param start_y: 第一点y轴
        :param end_x: 第二个点x轴
        :param end_y:  第二个点y轴
        :param duration: 滑动时间
        :return:
        '''
        if self.find_element(locator):
            print('找到元素，开始滑动')
            return  self._driver.swipe(start_x, start_y, end_x, end_y, duration)
        else:
            print('元素未出现，无法进行滑动')
            return False

if __name__ == '__main__':
    pass