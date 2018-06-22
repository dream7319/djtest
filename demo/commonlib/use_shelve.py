#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_shelve.py
@time: 2018/4/24 11:09
'''
__author__ = 'lierl'

import shelve

f = shelve.open("test.txt")

print(type(f))
# print(f.get("aa"))
