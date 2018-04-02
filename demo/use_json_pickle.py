#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_json_pickle.py
@time: 2018/3/25 11:23
'''
import json

__author__ = 'lierl'

#pickle模块来实现序列化
import pickle
d = dict(name='bob', age=20, score=88)
print(pickle.dumps(d))#把任意对象序列化为一个bytes
pickle_data = b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00bobq\x02X\x05\x00\x00\x00scoreq\x03KXX\x03\x00\x00\x00ageq\x04K\x14u.'
pickle_loads = pickle.loads(pickle_data)
print(type(pickle_loads))
print(pickle_loads)

d = dict(name='bob', age=20, score=88)
with open("test.txt", mode='wb') as f:
    pickle.dump(d, f)#把序列化之后的bytes写入文件
    f.close()
f = open("test.txt", mode='rb')
content = pickle.load(f)
f.close()
print(content)
#Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容,因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系

#SON标准规定JSON编码是UTF-8
json1 = json.dumps(d)#dumps()方法返回一个str，内容就是标准的JSON
print("--"+json1)
#要把JSON反序列化为Python对象
json_str = '{"score": 88, "name": "bob", "age": 20}'
json_obj = json.loads(json_str)
print(type(json_obj))#<class 'dict'>'


#Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student(name='lierl', age=29, score=99)
# print(json.dumps(s))#TypeError: <__main__.Student object at 0x000002252A7ED828> is not JSON serializable

def student2dic(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
data = json.dumps(s, default=student2dic)
# print(json.dumps(s))
print("-->", type(data))
data = json.dumps(s, default=lambda obj:obj.__dict__)
print("-->", type(data))

json_str = '{"age": 29, "name": "lierl", "score": 99}'
def dic2student(d):
    return Student(d['name'], d['age'], d['score'])
data = json.loads(json_str, object_hook=dic2student)
print(type(data))#反序列化

stu = json.loads(json_str, object_hook=lambda d:Student(d['name'], d['age'], d['score']))
print(stu.name)

