#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: do_io.py
@time: 2018/3/25 11:00
'''
__author__ = 'lierl'

from io import StringIO
#在内存中读写 StringIO操作的只能是str
f = StringIO()
f.write("hello")
f.write(' ')
f.write('world!')
print(f.getvalue())#获取写入后的字符串
f.close()
f = StringIO("hello\nhi\ngoodbye")
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
f.close()

#如果要操作二进制数据，就需要使用BytesIO

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
f.close()

#StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。