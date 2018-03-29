#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_async.py
@time: 2018/3/28 16:16
'''
__author__ = 'lierl'

'''
asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO
'''
import asyncio, threading

@asyncio.coroutine  #把一个generator标记为coroutine类型
def hello():
    print("hello world %s " % threading.current_thread())
    #异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print('hello again %s ' % threading.current_thread())

#获取eventloop
loop = asyncio.get_event_loop()
task = [hello(), hello()]
#执行coroutine
loop.run_until_complete(asyncio.wait(task))
loop.close()













