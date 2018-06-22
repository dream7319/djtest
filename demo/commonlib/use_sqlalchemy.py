#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_sqlalchemy.py
@time: 2018/4/20 14:55
'''

__author__ = 'lierl'

from sqlalchemy import Column,create_engine
from sqlalchemy.types import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建对象的基类:
BaseModel = declarative_base()

#定义对象
class User(BaseModel):
    #表名
    __tablename__='user'
    id = Column('id',Integer,primary_key=True,autoincrement=True)
    name = Column("user_name",String(20))#数据库中的字段名称为：user_name
    age = Column('age', Integer)

    role_id = Column('role_id',Integer)
    #方便输出，我们打印user时调用此方法
    def __repr__(self):
        return "id:%d,name:%s,age:%d" % (self.id, self.name, self.age)
# 为了方便输出
# def print_user(user):
#     return "id:%d,name:%s,age:%d" % (user.id, user.name, user.age)

class Role(BaseModel):
    # 表名
    __tablename__ = 'role'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column("role_name", String(20))

    def __repr__(self):
        return self.name

sql_connect = "mysql://root:root@139.199.129.251/blogdb?charset=utf8"
#创建连接数据库引擎
engine = create_engine(sql_connect, echo=True)#echo参数设为true，是为了输出sql语句以及打印日志信息

#初始化数据库
def init_db():
    BaseModel.metadata.create_all(engine)


#删除数据库表
def drop_db():
    BaseModel.metadata.drop_all(engine)

# init_db()
# drop_db()

DBsession = sessionmaker(bind=engine)
#添加数据
def addUser():
    # 创建session对象,相当于MySQLdb里面的游标
    session = DBsession()
    # 创建新User对象:
    new_user1 = User(name='zhangsan', age=18, role_id=1)
    new_user2 = User(name='lisi', age=12,role_id=1)
    new_user3 = User(name="zhaoliu", age=24,role_id=2)
    # 添加到session:
    session.add(new_user1)
    session.add(new_user2)
    session.add(new_user3)

    role1 = Role(name="超级管理员")
    role2 = Role(name="一般管理员")
    session.add(role1)
    session.add(role2)
    # 提交即保存到数据库
    session.commit()
    # 关闭session
    session.close()
# addUser()


def queryAll():
    # 调用all()则返回所有行:
    session = DBsession()
    users = session.query(User).all()
    print([user for user in users])
    session.close()

# queryAll()

#使用filter()则必须用 对象.属性==值；如果使用filter_by()，则使用"="即可
def queryFilter():
    session = DBsession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行
    # user = session.query(User).filter(User.id==1).one()
    user = session.query(User).filter_by(id=1).one()
    print(user)
    session.close()
# queryFilter()

#更新数据
def update_method1():
    session = DBsession()
    user = session.query(User).filter(User.id == '1')
    user.update({User.age: 10, User.name:'aaaa'})
    session.commit()
    # 关闭session
    session.close()

# update_method1()


def update_method2():
    session = DBsession()
    user = session.query(User).filter_by(id='2').one()
    user.age = 10
    user.name='bbb'
    session.commit()
    # 关闭session
    session.close()

# update_method2()

def delete():
    session = DBsession()
    user = session.query(User).filter(User.id == '1').one()
    session.delete(user)
    session.commit()
    # 关闭session
    session.close()
# delete()

def execute():
    session = DBsession()
    user = session.execute("SELECT id,user_name as name,age FROM user WHERE id=:param",{"param":2}).fetchone()
    print(user)
    session.commit()
    # 关闭session
    session.close()
# execute()


def use_in():
    session = DBsession()
    users = session.query(User).filter(User.name.in_(['zhangsan','lisi'])).all()
    print([user for user in users])

# use_in()

def use_count():
    session = DBsession()
    count = session.query(User).filter().count()
    print(count)

# use_count()

from sqlalchemy import func

def use_group():
    session = DBsession()
    users = session.query(User.age,func.count(User.age)).group_by(User.age).all()
    print([user for user in users])

# use_group()



def use_relation_query():
    session = DBsession()
    user_role_datas = session.query(User,Role).filter(User.role_id == Role.id).all()
    print([user_role_data for user_role_data in user_role_datas])

use_relation_query()



