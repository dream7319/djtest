#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_metaclass.py
@time: 2018/3/24 17:43
'''
__author__ = 'lierl'

#动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
#metaclass:当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。连接起来就是：先定义metaclass，就可以创建类，最后创建实例

#metaclass是类的模板,所以必须从type类型派生
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
# __new__()方法接收到的参数依次是：
# 1、当前准备创建的类的对象；
# 2、类的名字；
# 3、类继承的父类集合；
# 4、类的方法集合。

L = MyList()
L.add(1)
print(L)#[1]