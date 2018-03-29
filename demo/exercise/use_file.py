#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_file.py
@time: 2018/3/29 22:03
'''
__author__ = 'lierl'

with open('aaa.txt', '+') as f:
    # print(f.readlines())
    f.write('bbb')