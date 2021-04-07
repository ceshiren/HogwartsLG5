#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_threading2.py 
@Time   :   2021/4/2 16:55   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   threading.Thread
"""
import datetime
import threading
import time


class test_threading2(threading.Thread):
    def __init__(self, n):
        super(test_threading2, self).__init__()  # 重构run函数必须写
        self.n = n

    def run(self):
        print('task', self.n, datetime.datetime.now())
        time.sleep(int(self.n))
        print(int(self.n), self.n, datetime.datetime.now())
        time.sleep(1)


if __name__ == '__main__':
    # print(dir(test_threading2))# 查看线程有哪些方法
    '''
    1.t2 设为守护进程，守护进程不一定执行到结束，主进程结束则立刻结束，主进程会等所有非守护进程的子进程结束。
    2.使用jion()可以使主进程等待守护进程
    '''
    t1 = test_threading2('1')
    t2 = test_threading2('5')
    # t3 = test_threading2('t3')
    t2.setDaemon(True)
    t1.start()
    t2.start()
    t2.join()
    print("end", datetime.datetime.now())
    # t3.start()
