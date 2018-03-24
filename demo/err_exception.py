#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: err_exception.py
@time: 2018/3/24 22:13
'''
__author__ = 'lierl'

from functools import reduce
import logging

def str2num(s):
    if '.' in s:
        return float(s)
    else:
        return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 = ', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 = ', r)

main()