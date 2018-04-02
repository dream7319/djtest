#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: test.py
@time: 2018/3/30 13:48
'''
__author__ = 'lierl'
import demo.exercise.use_file
import os
import demo.clazz

ip_module = __import__('use_file')
print(dir(ip_module))

test_class = getattr(ip_module, "TestA")
cls_obj = test_class()

# methodname = getattr(cls_obj, 'aa')
# methodname('aa')
for attr in dir(cls_obj):
    if attr[0] != '_':
        class_attr_obj = getattr(cls_obj, attr)

        if hasattr(class_attr_obj, '__call__'):
            class_attr_obj('aa')
        else:
            print(attr, ' type:', type(class_attr_obj), ' value:', class_attr_obj)


import importlib
imp_module = 'use_file'
imp_class = 'TestA'

ip_module = importlib.import_module('.', imp_module)


ip_module_cls = getattr(ip_module, imp_class)
cls_obj = ip_module_cls()

methodname = getattr(cls_obj, 'aa')
methodname('aa')

ip_module = importlib.reload(ip_module)
ip_module_cls = getattr(ip_module, imp_class)
cls_obj = ip_module_cls()

methodname = getattr(cls_obj, 'aa')
methodname('aa')


clss = importlib.import_module('demo.web.other', '.')
clss_obj = getattr(clss, 'Other')
cls_obj = clss_obj()
methodname = getattr(cls_obj, 'bb')
methodname('bb')