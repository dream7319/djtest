#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: tcp_server.py
@time: 2018/3/27 21:38
'''
__author__ = 'lierl'

import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')

def tcplink(sock, addr):
    print("Accept new connection from %s:%s.." % addr)
    sock.send(b'welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello, %s' % data.decode('utf-8')).encode('utf-8'))

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()





