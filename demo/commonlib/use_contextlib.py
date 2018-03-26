#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_contextlib.py
@time: 2018/3/26 21:06
'''
__author__ = 'lierl'

with open('test.txt', 'r') as f:
    content = f.read()
    print(content)

#并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。实现上下文管理是通过__enter__和__exit__这两个方法实现的。例如，下面的class实现了这两个方法：

class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("begin")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("error")
        else:
            print("end")

    def query(self):
        print("query info about %s ..." % self.name)

with Query('bob') as q:
    q.query()

#编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：

class Query1(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print("query info about %s ..." % self.name)

from contextlib import contextmanager

@contextmanager
def create_query(name):
    print("begin")
    q = Query1(name)
    yield q
    print("end")

#@contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了：

with create_query('lierl') as q:
    q.query()

#很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。例如：

@contextmanager
def tag(name):
    print("<%s>" % name, end="")
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello", end=" ")
    print("world", end="")

'''
代码的执行顺序是：
1、with语句首先执行yield之前的语句，因此打印出<h1>；
2、yield调用会执行with语句内部的所有语句，因此打印出hello和world；
3、最后执行yield之后的语句，打印出</h1>。
因此，@contextmanager让我们通过编写generator来简化上下文管理。
'''

#果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()：

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)


# closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()


#作用就是把任意对象变为上下文对象，并支持with语句。@contextlib还有一些其他decorator，便于我们编写更简洁的代码。