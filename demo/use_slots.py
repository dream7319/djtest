#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_slots.py
@time: 2018/3/24 15:37
'''
__author__ = 'lierl'

#__slots__来限制实例的属性
class Student(object):
    __slots__ = ("name", "age")# 用tuple定义允许绑定的属性名称

class GraduateStudent(Student):
    pass

if __name__ == "__main__":
    s = Student()
    s.name = "lierl"
    s.age = 29
    try:
        s.score = 99
    except AttributeError as e:
        print("AttributeError:" , e)

    g = GraduateStudent()
    g.score = 89
    print("g.score = ", g.score)