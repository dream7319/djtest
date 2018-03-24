#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: special_demo.py
@time: 2018/3/24 16:16
'''
__author__ = 'lierl'

class Student(object):

    def __init__(self, name):
        self.name = name

        # 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？
    def __call__(self, *args, **kwargs):
        print("my name is %s." % self.name)

    def __str__(self):
        return "Student object (name: %s)" % self.name
    #直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的
    __repr__ = __str__

student1 = Student('lierl')
print(student1)
print(student1())#call __call__

#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环

class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1# 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b,self.a+self.b#计算下一个值
        if self.a > 10000:#退出循环
            raise StopIteration()
        return self.a#返回下一个值

    #Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
    #要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
    #与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a+b
        return a
    #正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错
    # 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')
    # 来尝试获得属性，这样，我们就有机会返回score的值：
    def __getattr__(self, item):
        if item == 'score':
            return 99
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)


print()
for n in Fib():
    print(n, end= " ")
f = Fib()
print(f[0])
print(f[1])
print(f[2])
print(f[3])

class Chain(object):

    def __init__(self, path = ''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

# print(Chain.status.user.timeline.list)