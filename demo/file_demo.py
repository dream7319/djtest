#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: file_demo.py
@time: 2018/3/25 9:15
'''
__author__ = 'lierl'

try:
    f = open("test.txt", mode='r')
    content = f.read()#read()会一次性读取文件的全部内容
    print('read:', content)
    print(f.name)
finally:
    if f:
        f.close()
print("--------------------------------------------------------------------")
with open("test.txt", mode='r') as f:
    print(f.read())#read()会一次性读取文件的全部内容
print("--------------------------------------------------------------------")
with open("test.txt", mode='r') as f:
    print(f.readline())#读取一行，readline(2)  读取2个字符
print("--------------------------------------------------------------------")
with open("test.txt", mode='r') as f:
    for line in f.readlines():
        print(line.strip())
print("--------------------------------------------------------------------")
with open("test.txt", mode='rb') as f:#读取二进制文件，rb表示以二进制模式打开文件
    print(f.read())
print("--------------------------------------------------------------------")
with open("test.txt", mode='r', encoding="gbk", errors='ignore') as f:
    print(f.read())
print("--------------------------------------------------------------------")
#写
f = open("test.txt", mode='w')
f.write("write somethings")
f.close()
print("--------------------------------------------------------------------")
#当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险

print("--------------------------------------------------------------------")
with open("test.txt", mode='w') as f:
    f.write("hello world!!!")
print("--------------------------------------------------------------------")
#mode
'''
mode:
Character	Meaning
'r'	open for reading (default)
'w'	open for writing, truncating the file first
'x'	open for exclusive creation, failing if the file already exists
'a'	open for writing, appending to the end of the file if it exists
'b'	binary mode
't'	text mode (default)
'+'	open a disk file for updating (reading and writing)
'U'	universal newlines mode (deprecated)

errors:
'strict' to raise a ValueError exception if there is an encoding error. The default value of None has the same effect.
'ignore' ignores errors. Note that ignoring encoding errors can lead to data loss.
'replace' causes a replacement marker (such as '?') to be inserted where there is malformed data.
'surrogateescape' will represent any incorrect bytes as code points in the Unicode Private Use Area ranging from U+DC80 to U+DCFF. These private code points will then be turned back into the same bytes when the surrogateescape error handler is used when writing data. This is useful for processing files in an unknown encoding.
'xmlcharrefreplace' is only supported when writing to a file. Characters not supported by the encoding are replaced with the appropriate XML character reference &#nnn;.
'backslashreplace' replaces malformed data by Python’s backslashed escape sequences.
'namereplace' (also only supported when writing) replaces unsupported characters with \N{...} escape sequences.

'''
print("--------------------------------------------------------------------")

print("--------------------------------------------------------------------")

print("--------------------------------------------------------------------")

