#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_retrying.py
@time: 2018/4/18 16:43
'''
import sys
from time import time

__author__ = 'lierl'

from retrying import retry
#pip install retrying

#retry装饰器,被注释的方法出现异常的话会一直被调用

def stop_func(attempts, delay):
    print(" stop_func %d--->%d" % (attempts,delay))

@retry(stop_max_delay=10, stop_func=stop_func)
def test_stop_func():
    print("test_stop_func")
    raise Exception

test_stop_func()





