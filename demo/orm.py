#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: orm.py
@time: 2018/3/24 17:55
'''
__author__ = 'lierl'

#定义Field类，它负责保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

#在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, "varchar(100)")

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, "bigint")

#编写最复杂的ModelMetaclass
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print("Found model: %s" % name)

        mappings = dict()
        for k, v in attrs.items():
            print(k, '-->', v)
            if isinstance(v, Field):
                print("Found mapping: %s ==> %s" % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings#保存属性和列的映射关系
        attrs['__table__'] = name #假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)
#基类Model
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute %s" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self, k))
        sql = 'insert into %s (%s) VALUES (%s)' % (self.__table__, ','.join(fields),
                                                   ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    id = IntegerField('id')
    name = StringField("username")
    email = StringField("email")
    password = StringField("password")

u = User(id=1, name='lierl', email='lierlei0515@163.com', password='12345')
# u.save()