#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_threading.py
@Time   :   2021/4/2 14:21
@Contact    :
@Author     :   WG
@Version    :   v 0.1
@Desc   :   threading
"""
'''
    使用多线程编程具有如下几个优点：
    进程之间不能共享内存，但线程之间共享内存非常容易。
    操作系统在创建进程时，需要为该进程重新分配系统资源，但创建线程的代价则小得多。因此使用多线程来实现多任务并发执行比使用多进程的效率高
    python语言内置了多线程功能支持，而不是单纯地作为底层操作系统的调度方式，从而简化了python的多线程编程。
'''

import threading
import datetime
from threading import Lock, Thread
import time, os


def test_run(n):
    print('task', n, datetime.datetime.now())
    time.sleep(1)
    print('1s', n, datetime.datetime.now())
    time.sleep(1)


if __name__ == '__main__':
    #test_run不加（）
    t1 = threading.Thread(target=test_run, args=('t1',))  # target是要执行的函数名（不是函数），args是函数对应的参数，以元组的形式存在
    # t2 = threading.Thread(target=test_run, args=('t2',))
    t1.setDaemon(True)
    t1.start()
    print("end")
    # t2.start()
