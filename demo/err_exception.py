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
logging.basicConfig(level=logging.INFO)

def str2num(s):
    a = s.strip().replace(".", '', 1)
    if a.isdigit():
        if "." in s.strip():
            return float(s.strip())
        else:
            return int(s.strip())
    else:
        raise ValueError("is not digit")

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    try:
        r = calc('100 + 200 + 345')
        print('100 + 200 + 345 = ', r)
        r = calc('99 + 88 + 7.6')
        print('99 + 88 + 7.6 = ', r)
    except ValueError as e:
        logging.exception(e)

main()

print("3.2".is_integer())