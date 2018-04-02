#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: utils.py
@time: 2018/4/1 16:28
'''
__author__ = 'lierl'
import hashlib

class MD5:
    def get_md5(str, salt="myapp"):
        h1 = hashlib.sha256()
        str += salt
        h1.update(str.encode('utf-8'))
        return h1.hexdigest()

