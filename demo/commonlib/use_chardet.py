#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_chardet.py
@time: 2018/3/27 16:39
'''
__author__ = 'lierl'

import chardet

print(chardet.detect(b'Hello, world!'))#检测出的编码是ascii，注意到还有个confidence字段，表示检测的概率是1.0（即100%）

data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))

data = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data))

#用chardet检测编码，使用简单。获取到编码后，再转换为str，就可以方便后续处理。

