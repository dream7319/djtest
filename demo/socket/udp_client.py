#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: udp_client.py
@time: 2018/3/27 21:54
'''
__author__ = 'lierl'

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Lamba', b'Bond', b'alpha']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))

s.close()

