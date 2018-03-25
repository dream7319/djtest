#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: do_fork.py
@time: 2018/3/25 14:51
'''
__author__ = 'lierl'

import os
from multiprocessing import Process

print("process (%s) start..." % os.getpid())

# pid = os.fork()#linux下没有问题,window会报错AttributeError: module 'os' has no attribute 'fork'
# print(pid)

#子进程要执行的代码
def run_proc(name):
    print("run child process %s(%s)..." % (name, os.getpid()))

'''
创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
'''
if __name__ == '__main__':
    print("parent process %s." % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print("child process will start")
    p.start()
    p.join()
    print("child process end.")









