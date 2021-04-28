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
import _thread

from cffi.cparser import lock

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

str1 = "wg"

g = "global"
number_n = 0
def test_run(n):
    global g
    lock.acquire()
    g = g+n
    print('task', n, datetime.datetime.now(),g)
    time.sleep(0.1)
    lock.release()
    time.sleep(1)
def test_lock(lock):
    global number_n
    global str1
    lock.acquire()
    number_n += 1
    str1=str1+str(number_n)
    time.sleep(0.1)
    print(str1)
    lock.release()

if __name__ == '__main__':

    #test_run不加（）
    # t1 = threading.Thread(target=test_run, args=('t1',))  # target是要执行的函数名（不是函数），args是函数对应的参数，以元组的形式存在
    # t2 = threading.Thread(target=test_run, args=('t2',))
    # t1.setDaemon(True)
    # t1.start()
    # t2.start()

    """
    互斥锁：lock
    lock=threading.Lock()
    l = []
    for i in range(100):
        p = threading.Thread(target=test_run,args=("t%s"%(i),))
        l.append(p)
        p.start()
    print("end")
    for i in l:
        i.join()
    """
    """
    递归锁（Rlock）：支持嵌套，多个锁没有释放的时候一般会使用递归锁
    lock=threading.RLock()
    for i in range(10):
        p = threading.Thread(target=test_lock,args=(lock,))
        p.start()
    """
    """
    信号量：互斥锁只允许一个线程更改数据，Semaphore允许一定数量的线程更改数据
        semaphore=threading.BoundedSemaphore(3)#最多三个线程可以同时进行
    l = []
    for i in range(100):
        p = threading.Thread(target=test_lock,args=(semaphore,))
        l.append(p)
        p.start()
    print("end")
    for i in l:
        i.join()
        >>>
        wg123456789101112131415
        wg123456789101112131415
        wg123456789101112131415
        wg123456789101112131415161718
        wg123456789101112131415161718
        wg1234567891011121314151617181920
        wg123456789101112131415161718192021
        wg123456789101112131415161718192021
        wg123456789101112131415161718192021
    """
    """
    python 线程的事件：
        事件用于主线程控制其他现场的执行，时间是一个简单的线程同步对象，主要提供以下几个方法：
    clear：设置flag为F
    set：设置flag为T
    is_set：判断是否设置了flag
    wait：监听flag，如果没有检测到就一直处于阻塞状态
        事件处理的机制：
    全局定义一个flag，当flag为T时，event.wait就可以运行，为F时就会阻塞
       event = threading.Event()


    def lighter():
        count = 0
        event.set()  # 初始者为绿灯
        while True:
            if 5 < count <= 10:
                event.clear()  # 红灯，清除标志位
                print("\33[41;lmred light is on...\033[0m]")
            elif count > 10:
                event.set()  # 绿灯，设置标志位
                count = 0
            else:
                print('\33[42;lmgreen light is on...\033[0m')

            time.sleep(1)
            count += 1


    def car(name):
        while True:
            if event.is_set():  # 判断是否设置了标志位
                print('[%s] running.....' % name)
                time.sleep(1)
            else:
                print('[%s] sees red light,waiting...' % name)
                event.wait()
                print('[%s] green light is on,start going...' % name)


    # startTime = time.time()
    light = threading.Thread(target=lighter, )
    light.start()

    car = threading.Thread(target=car, args=('MINT',))
    car.start()
    endTime = time.time()
    # print('用时：',endTime-startTime)
    """

