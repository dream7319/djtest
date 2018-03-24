#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: extenddemo.py
@time: 2018/3/24 14:52
'''
__author__ = 'lierl'

class Animal(object):

    def run(self):
        print("Animal is running...")

class Dog(Animal):

    def eat(self):
        print("dog is eating...")

    def run(self):
        print("dog is running ...")

class Cat(Animal):
    def run(self):
        print("cat is running ...")

    def eat(self):
        print("cat is eating ...")

if __name__ == '__main__':
    dog = Dog()
    dog.run()
    dog.eat()
    cat = Cat()
    cat.run()
    cat.eat()
    print(isinstance(dog, Dog))#判断dog是否是Dog类型
    print(isinstance(dog, Animal))