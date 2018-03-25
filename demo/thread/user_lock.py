#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: user_lock.py
@time: 2018/3/25 16:20
'''
__author__ = 'lierl'

import time, threading, multiprocessing

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        #获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()#释放锁

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

print(multiprocessing.cpu_count())#cpu数量