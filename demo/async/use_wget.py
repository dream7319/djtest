#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_wget.py
@time: 2018/3/28 16:24
'''
__author__ = 'lierl'

import asyncio, threading

@asyncio.coroutine
def wget(host):
    print("wget %s ..." % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print("%s header > %s " % (host, line.decode('utf-8').rstrip()), threading.current_thread())
    writer.close()
#获取eventloop
loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
#执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


'''
asyncio提供了完善的异步IO支持
异步操作需要在coroutine中通过yield from完成
多个coroutine可以封装成一组Task然后并发执行
'''



