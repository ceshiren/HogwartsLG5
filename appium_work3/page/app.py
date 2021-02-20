#coding:utf-8
import os
from appium import webdriver
from appium_work3.page.main_page import MainPage
from appium_work3.page.base_page import BasePage
import multiprocessing
import subprocess
import socket

class App(BasePage):
    res_yaml = BasePage().open_yaml('../config/app.yaml')
    def start(self,ip=res_yaml['ip'],udid=res_yaml['udid'][0],port=res_yaml['port'][0]):
        '''判断driver是否有值，有则加载报名，无则启动driver，返回对象本身'''
        if self.start_port(ip,port):
            try:
                capability_conf = {}
                capability_conf['platformName'] = self.res_yaml['platformName']
                capability_conf['deviceName'] = self.res_yaml['deviceName']
                capability_conf['appPackage'] = self.res_yaml['appPackage']
                capability_conf['appActivity'] = self.res_yaml['appActivity']
                capability_conf['noReset'] = self.res_yaml['noReset']
                capability_conf['unicodeKeyboard'] = self.res_yaml['unicodeKeyboard']
                capability_conf['resetKeyboard'] = self.res_yaml['resetKeyboard']
                capability_conf['chromedriverExecutableDir'] = self.res_yaml['chromedriverExecutableDir']
                capability_conf['udid'] = udid
                capability_conf['settings[waitForIdleTimeout]'] = self.res_yaml['settings[waitForIdleTimeout]']
                # capability_conf['dontStopAppOnself.reset'] = self.res['dontStopAppOnself.reset']#调试模式，quit会失效
                self._driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", capability_conf)
                # self._driver = webdriver.Remote(f"http://localhost:{port}/wd/hub", capability_conf)
                print(f'当前连接的设备信息为：{capability_conf}')
                self._driver.implicitly_wait(10)
            except Exception as e:
                raise e
        else:
            self.stop_port(port)
            self.start(ip,udid,port)
        return self

    def stop(self):
        '''关闭APP'''
        self._driver.quit()
        return self

    def restart(self):
        '''重启APP'''
        self._driver.quit()
        self._driver.launch_app()
        return self

    def start_sync(self):
        '''多进程启动多个模拟器'''
        desired_process_list =  []
        for des in range(len(self.res_yaml['udid'])):
            port = 4723 + 2*des
            desired = multiprocessing.Process(target=self.start,args=
            (self.res_yaml['ip'],self.res_yaml['udid'][des],port))#target执行方法，args传参
            desired_process_list.append(desired)
        for run in desired_process_list:
            run.start()
        for run in desired_process_list:
            run.join()
        return self

    def start_port_sync(self):
        '''后台启动两个appium服务端口'''
        desired_process_list = []
        for i in range(len(self.res_yaml['udid'])):
            port = 4723 + 2*i
            desired = multiprocessing.Process(target=self.start_port, args=(self.res_yaml['ip'], port))  # target执行方法，args传参
            desired_process_list.append(desired)
        for run in desired_process_list:
            run.start()
        for run in desired_process_list:
            run.join()


    def start_port(self,host,port):
        '''后台创建appium服务，else未占用进行创建'''
        if self.check_port(host,port):
            return False
        else:
            bootstart_port = port+1
            cmd = 'start /b appium -a '+ host + ' -p ' + str(port) + ' -bp ' + str(bootstart_port)#/b是隐藏cmdUI界面后台运行
            subprocess.Popen(cmd,shell=True,stdout=open('./appium_log'+str(port)+'.log','a'),stderr=subprocess.STDOUT)
            return True


    def stop_port(self,  port):
        '''杀死监听的端口'''
        cmd_find = f'netstat -ano | findstr {port}'
        res = os.popen(cmd_find).read()
        if port and 'LISTENING' in res:
            i = res.index('LISTENING')
            start = i+len('LISTENING')+7
            end = res.index('\n')
            res = res[start:end]
            cmd_kill = f'taskkill /pid {res} -t -f'
            os.popen(cmd_kill)
        else:
            return False
        # res = subprocess.Popen(cmd_find,shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE, encoding='utf-8')
        # res_text:str = res.communicate()[0]#拿到cmd查到的信息
        # res_port = res_text.split('\n')
        # for i in res_port:
        #     if str(port) and 'LISTENING' in i:
        #         res = i.split()[-1].strip()
        #         cmd_kill = f'taskkill /pid {res} -t -f'
        #         subprocess.Popen(cmd_kill, shell=True, stderr=subprocess.STDOUT)
        #         # print(f'杀死{res}进程成功。。。')
        #         break
        #     print('未找到进程。。。')

    def check_port(self,host,port):
        '''检查接口是否被占用,true被占用'''
        so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            so.connect((host,port))
            so.shutdown(2)#关闭连接
        except OSError as msg:
            return False
        else:
            return True


    def main(self)->MainPage:
        return MainPage(self._driver)

if __name__ == '__main__':
    pass
    # App().stop_port(4725)
    # App().stop_port(4723)
    App().start_port_sync()