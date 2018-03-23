#Python内建了map()和reduce()函数。

#              f(x) = x * x
#
#                   │
#                   │
#   ┌───┬───┬───┬───┼───┬───┬───┬───┐
#   │   │   │   │   │   │   │   │   │
#   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼
#
# [ 1   2   3   4   5   6   7   8   9 ]
#
#   │   │   │   │   │   │   │   │   │
#   │   │   │   │   │   │   │   │   │
#   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼
#
# [ 1   4   9  16  25  36  49  64  81 ]
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x*x
r = map(f,[1,2,3,4,5])
#由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list
print(list(r))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x,y):
    return x+y
r = reduce(add,[1,2,3,4,5])
print(r)

def fn(x,y):
    return x*10+y
r = reduce(fn,[1,3,5,7,9])
print(r)

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
names = ['adam', 'LISA', 'barT']
def f(name):
    return name.title()
print(list(map(f,names)))

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
list1 = [1,2,3,4,5]
def prod(x,y):
    return x*y
print(reduce(prod,list1))

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}
def str2float(s):
    nums = map(lambda ch:CHAR_TO_FLOAT[ch], s)
    #[1, 2, 3, -1, 4, 5, 6]
    point = 0
    def to_float(f,n):
        #global 和 nonlocal关键字
        nonlocal point
        if n == -1:
            point=1
            return f
        if point == 0:
            return f*10+n
        else:
            point = point * 10
            return f + n/point
    return reduce(to_float,nums,0.0)
print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))

print(float('123.02'))
#--------------------------------filter()------------------------------------------
#和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
#在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd,[1,2,3,4,5])))

#把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['1','','2',None,'3',None])))

def _odd_iter():
    n=1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x: x % n > 0
def primes():
    yield 2
    it = _odd_iter()# 初始序列
    while True:
        n = next(it)# 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n, end=" ")
    else:
        break
print()
my_lambda = lambda x, y: x+y
print(my_lambda(1, 2))
#----------------------------sorted-------------------------------------------------------
#排序算法   默认情况下，对字符串排序，是按照ASCII的大小比较的
print(sorted([5,6,2,3,9]))
print(sorted([5,6,2,-3,9],key= abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

#忽略大小写的排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

#假设我们用一组tuple表示学生名字和成绩：

students = [('Bob', 75), ('Adam', 92), ('Bart', 66),('Bart', 76), ('Lisa', 88)]
print(sorted(students))
from operator import itemgetter
print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[0]))
print(sorted(students, key=itemgetter(1), reverse= True))
print(sorted(students, key=lambda t: t[1], reverse= True))
print(sorted(students, key=itemgetter(0, 1)))


def count():
    fs = []
    def f(n):
        def j():
            return n * n
        return j
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()

print(f1())#1
print(f2())#4
print(f3())#9

# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
