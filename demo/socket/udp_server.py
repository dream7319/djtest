#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: udp_server.py
@time: 2018/3/27 21:54
'''
__author__ = 'lierl'

import socket
# 创建Socket时，socket.SOCK_DGRAM指定了这个Socket的类型是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999))
# 绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据
print('Bind UDP on 9999...')
# recvfrom()方法返回数据和客户端的地址与端口
# 服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端

while True:
    data, addr = s.recvfrom(1024)
    print(data, addr)
    print('Received from %s:%s' % addr)
    s.sendto(b'Hello, %s!' % data, addr)
