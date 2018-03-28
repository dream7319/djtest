#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_itertools.py
@time: 2018/3/26 17:01
'''
__author__ = 'lierl'

#Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数

import itertools,time

natuals = itertools.count(2)#其实位置
#因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列
# for i in natuals:
#     print(i)
    # time.sleep(1)

#循环迭代  cycle()会把传入的一个序列无限重复下去
# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)

#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
rep = itertools.repeat('A', 3)

for r in rep:
    print(r)

#无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'CDE'):
    print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起：
print("----------------------------------------")
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, '-->', list(group))

print("----------------------------------------")
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
     print(key, list(group))

#利用Python提供的itertools模块，我们来计算这个序列的前N项和：

def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    step1 = itertools.count(start=1, step=2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    step2 = itertools.takewhile(lambda x: x <= 2*N - 1, step1)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    listStep2 = list(step2)
    step3 = [pow(-1, listStep2.index(i)) * (4/i) for i in listStep2]
    print(step3)
    # step 4: 求和:
    return sum(step3)

# l = [1, 2, 3]
# 0 -1 0 -1
# s = [pow(-1, l.index(i)) * (4/i) for i in l]
# print(s)
#
# print("--", sum(s))
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

#--------------第二种方法---------------------------

def pi1(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    step1 = itertools.count(start=1, step=2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    step2 = itertools.takewhile(lambda x: x <= 2*N - 1, step1)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    symbol_cycles = itertools.cycle([1,-1])#循环1 -1
    result = map(lambda x: next(symbol_cycles) * 4/x, step2)
    # step 4: 求和:
    return sum(result)
print(pi1(10))