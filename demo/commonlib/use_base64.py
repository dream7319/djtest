#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_base64.py
@time: 2018/3/26 15:18
'''
__author__ = 'lierl'

import base64

print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
#于标准的Base64编码后可能出现字符+和/ 在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))#b'abcd++//'
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode(b'abcd--__'))

print(base64.b64encode(b'abcd'))
