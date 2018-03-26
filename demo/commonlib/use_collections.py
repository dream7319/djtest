#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_collections.py
@time: 2018/3/25 21:15
'''
__author__ = 'lierl'

from collections import namedtuple

#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
print(type(p))
print(isinstance(p, tuple))
print(p)

#使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈

from collections import deque
d = deque(['a', 'b', 'c'])
d.append('d')
d.append('e')
d.appendleft('m')
print(d)
print(d.popleft())#删除第一个
print(d.pop())#删除最后一个
print(d)
print(d.remove('b'))#删除指定值
print(d)

from collections import defaultdict

#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
#除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的
dd = defaultdict(lambda: 'N/A')#注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入
dd['aa'] = 'bb'
print(dd)
print(dd['aa'])
print(dd['cc'])#N/A

from collections import OrderedDict
#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序
#如果要保持Key的顺序，可以用OrderedDict
#OrderedDict的Key会按照插入的顺序排列,OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
od = OrderedDict([('b', 2), ('a', 1), ('c', 3)])
print(od)

class LastUpdatedOrderDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containKey = 1 if key in self else 0
        if len(self) - containKey >= self._capacity:
            last = self.popitem(last=False)
            print("remove:", last)
        if containKey:
            del self[key]
            print("set : ", (key, value))
        else:
            print("add:", (key, value))
        OrderedDict.__setitem__(self, key, value)


#Counter是一个简单的计数器，例如，统计字符出现的个数
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)