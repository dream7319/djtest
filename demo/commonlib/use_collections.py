#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_collections.py
@time: 2018/3/25 21:15
'''
__author__ = 'lierl'

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
print(type(p))
print(isinstance(p, tuple))


