#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: test.py
@time: 2018/3/30 13:48
'''
__author__ = 'lierl'

while True:
    num = input("请输入内容")
    num = num.strip()
    print(num.isdigit())
    print(num == '')