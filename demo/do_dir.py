#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: do_dir.py
@time: 2018/3/25 11:07
'''
__author__ = 'lierl'

import os, platform
print(os.name)
# print(os.uname())#os.uname()方法在window不可用，导致错误
print(platform.uname())
print(os.environ)
print(os.environ.get('PATH'))

print(os.path.abspath('.'))# 查看当前目录的绝对路径:
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('.', 'testDir'))

os.mkdir(os.path.join('.', 'testDir'))#创建目录
os.rmdir(os.path.join('.', 'testDir'))#删除目录

print(os.path.split('e:\\aa\\aa.txt'))
print(os.path.splitext('e:\\aa\\aa.txt'))

# os.rename('test.txt', 'test.py')#重命名
# os.remove('test.py')#删除文件

#shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。

import shutil
#列出当前目录下的所有目录，只需要一行代码
print([x for x in os.listdir(".") if os.path.isdir(x)])

#列出所有的.py文件
print([x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

#Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中