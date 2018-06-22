#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_random.py
@time: 2018/4/24 9:58
'''
__author__ = 'lierl'

import random

#0,1之间时间生成的浮点数  float
print(random.random())

#随机生成1-3之间的整数
print(random.randint(1,3))

#随机生成1-5范围内的数字，range顾头不顾尾
print(random.randrange(1,5))

#随机选择任意一个
print(random.choice([1,'23',[4,5]]))

#随机选择任意两个
print(random.sample([1,'23',[4,5]],2))

def code_five1():
    code = ''
    for i in range(5):
        num = random.randint(0,9)
        alf = chr(random.randint(65, 90))
        add = random.choice([num, alf])
        code+=str(add)
    return code

def code_five2():
    num = [str(i) for i in range(10)]
    az = [chr(i) for i in range(65,91)]
    AZ = [chr(i) for i in range(97,123)]
    l = num + az + AZ
    data = random.sample(l,5)
    return ''.join(data)

# print(code_five1())
print(code_five2())

