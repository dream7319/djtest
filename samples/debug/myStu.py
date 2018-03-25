#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: myStu.py
@time: 2018/3/25 8:39
'''
__author__ = 'lierl'

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score > 100:
            raise ValueError("不能大于100")
        elif self.score >= 80:
            return 'A'
        elif self.score >= 60:
            return 'B'
        elif self.score > 0:
            return 'C'
        else:
            raise ValueError("不能小于0")