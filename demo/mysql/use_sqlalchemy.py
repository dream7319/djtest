#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_sqlalchemy.py
@time: 2018/3/28 9:41
'''
__author__ = 'lierl'

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建对象的基类
Base = declarative_base()

#定义user对象
class User(Base):
    __tablename__ = 'user'
    #表结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:      '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:root@139.199.129.251:3306/python')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
# session.close()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id == '5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()


'''
例如，如果一个User拥有多个Book，就可以定义一对多关系如下：

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))
当我们查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list。
'''


