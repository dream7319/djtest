#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: tcp_client.py
@time: 2018/3/27 21:44
'''
__author__ = 'lierl'

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8'))

for data in [b'Lamba', b'Bond', b'alpha']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()