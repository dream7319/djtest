#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: do_subprocess.py
@time: 2018/3/25 15:32
'''
__author__ = 'lierl'

#subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出
import subprocess

print("$ nslookup www.python.org")
r = subprocess.call(['nslookup', 'www.python.org'])
print("exit code:", r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
