#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
 test module
'''
__author__ = 'lierl'

class Student(object):

    def __init__(self, name, score):
        self.__name = name#外部不能访问两个属性
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    #为什么要定义一个方法大费周折？因为在方法中，可以对参数做检查，避免传入无效的参数：
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

class Person(object):
    def __init__(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('bad gender')

if __name__ == '__main__':
    bart = Person('male')
    if bart.get_gender() != 'male':
        print("测试失败")
    else:
        bart.set_gender('female')
        if bart.get_gender() != 'female':
            print("测试失败")
        else:
            print("测试成功")

    bart = Student('Bart Simpson', 59)
    print('bart.get_name() =', bart.get_name())
    bart.set_score(60)
    print('bart.get_score() =', bart.get_score())

    print('DO NOT use bart._Student__name:', bart._Student__name)