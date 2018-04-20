#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_config_parser.py
@time: 2018/4/19 14:48
'''
__author__ = 'lierl'

#使用ConfigPaser模块可以对配置文件进行操作。
import configparser
import os
cf = configparser.ConfigParser()
#读取test.ini文件
cf.read(filenames="test.ini")
sections = cf.sections()#得到两个section名称,即 one two
for section in sections:
    options = cf.options(section)#获取key one_key  two_key1
    print(options) #['one_key'],['two_key']
kvs = cf.items('one')
print(kvs)#[('one_key', 'one key content')]

#读取指定节和键的值
one_content_str = cf.get('one', 'one_key')
print(one_content_str)
print(type(one_content_str))

two_content_int = cf.getint('two', 'two_key')
print(two_content_int)
print(type(two_content_int))

# 更新指定节和键的值
values = cf.values()
for value in values:
    print(value)