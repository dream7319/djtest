#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_property.py
@time: 2018/3/24 16:02
'''
__author__ = 'lierl'

#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return 786432

if __name__ == '__main__':
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')