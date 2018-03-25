#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: do_queue.py
@time: 2018/3/25 15:45
@desc: 进程间通信
'''
__author__ = 'lierl'

# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
# 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据

from multiprocessing import Queue, Process
import os, time, random

#写数据进程执行代码
def write(q):
    print("Process to write: %s" % os.getpid())
    for value in ['A', 'B', 'C']:
        print("put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random())

#读数据进程执行的代码
def read(q):
    print("process to read %s" % os.getpid())
    while True:
        value = q.get(True)
        print("get %s from queue" % value)

if __name__ == '__main__':
    ## 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    #启动子进程pw,写入
    pw.start()
    #启动子进程pr,读取
    pr.start()
    pw.join()#等待写入结束

    pr.terminate()#pr进程是死循环,无法等待其结束,强行终止




