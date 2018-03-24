import time
import datetime
import functools

#假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
#本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("call %s():" % func.__name__)
        return func(*args, **kwargs)
    return wrapper

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本

def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("%s %s():"%(text,func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator

#装饰器根据先后依次执行
@log #相当于执行了 now = log(now)
@log1("execute")##相当于执行了 now = log(‘execute’)(now)
def now():
    print(time.time())
    #不加参数时，默认就是输出当前的时间
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    print(datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S"))
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

f = now
f()
# print(type(f))#<class 'function'>
# h = now()
# print(type(h))#<class 'NoneType'>
print(f.__name__)#装饰前为now,添加装饰后：wrapper,需要添加 @functools.wraps(func)才能返回now
#now函数虽然添加了两个装饰器，但是now函数只会执行一次

#-------------------------------偏函数---------------------------------------
#二进制转十进制
int2 = functools.partial(int, base=2)
print(int2('1000000'))#64

