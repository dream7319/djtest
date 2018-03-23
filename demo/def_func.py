import math

def my_abs(x):
    if not isinstance(x,(int,float)):#对参数类型进行检查
        raise TypeError('bad operand type')

    if x >= 0:
        return x
    else:
        return -x

def move(x,y,step,angle=0):
    nx = x+step*math.cos(angle)
    ny = y-step*math.sin(angle)
    return nx,ny

n = my_abs(20)
print(n)

x,y = move(100,100,60,math.pi/6)
print(x,y)

# my_abs('123')#TypeError bad operand type-
#---------------------------------------------------------------------
def power(x):
    return x*x

print(power(5))
#---------------------------------------------------------------------
def power(x,n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5,4))
print(power(5))
#---------------------------------------------------------------------
#请计算a^2 + b^2 + c^2 + ……。
def calc(numbers):
    sum = 0
    for n in numbers:#1,4,9
        sum = sum + n*n
    return sum
print(calc([1,2,3]))#14
#---------------------------------------------------------------------
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1,2,3))#14
num = [1,2,3,4,5]
print("--",calc(*num))# *nums表示把nums这个list的所有元素作为可变参数传进去
#---------------------------------------------------------------------
def person(name,age,**kw):
    print("name:",name,",age:",age,",other:",kw)
person("miao",27)#name: miao ,age: 27 ,other: {}
person("lierl",29,city="bj")#name: lierl ,age: 29 ,other: {'city': 'bj'}
# person("test",22,"test")#报错

#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
#name: Jack ,age: 24 ,other: {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
#name: Jack ,age: 24 ,other: {'city': 'Beijing', 'job': 'Engineer'}
#---------------------------------------------------------------------
#命名关键字参数
#对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查
#以person()函数为例，我们希望检查是否有city和job参数：
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
#但是调用者仍可以传入不受限制的关键字参数：
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
person('Jack', 24, city='Beijing', job='Engineer')
#Jack 24 Beijing Engineer

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
#---------------------------------------------------------------------
#必选参数、默认参数、可变参数、关键字参数和命名关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
#a,b 必选参数
#c默认参数
#f2 d关键字参数
#*args 可变参数 args接收的是一个tuple
#**kw 关键字参数 kw接收的是一个dict
#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))
#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#---------------------------------------------------------------------
#函数内部
# 我们来计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
print(fact(10))#3628800
# print(fact(1000))#RecursionError: maximum recursion depth exceeded in comparison 栈溢出
#解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

#小结
# 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
# 针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
# Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题
#---------------------------------------------------------------------
# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')
#---------------------------------------------------------------------
#匿名函数
sum = lambda arg1, arg2: arg1 + arg2;
print(sum(10,20))
