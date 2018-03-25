#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: do_multi_thread.py
@time: 2018/3/25 16:07
'''
__author__ = 'lierl'

'''
Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
'''

import time, threading

#新线程执行代码
def loop():
    print("thread %s is running " % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print("thread %s >>> %s " % (threading.current_thread().name, n))
        time.sleep(1)
    print("thread %s ended " % threading.current_thread().name)

print("thread %s is running..." % threading.current_thread().name)

t = threading.Thread(target=loop, name='LoopThread')
# t = threading.Thread(target=loop(), name='LoopThread')#MainThread
t.start()
t.join()
print("thread %s ended." % threading.current_thread().name)



