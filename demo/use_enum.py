#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_enum.py
@time: 2018/3/24 17:31
'''
__author__ = 'lierl'

from enum import Enum, unique

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

for name, member in Month.__members__.items():
    print(name, '==>', member, ",", member.value)

@unique#@unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
day1 = Weekday.Mon
print(day1)

print(Weekday['Tue'])
print(Weekday.Tue.value)

for name, member in Weekday.__members__.items():
    print(name, "==>", member)

# 把Student的gender属性改造为枚举类型，可以避免使用字符串：

class Student(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

@unique
class Gender(Enum):
    Male = 0
    Female = 1

bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过')
else:
    print("测试失败")

# Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。