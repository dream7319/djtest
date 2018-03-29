#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_mysql.py
@time: 2018/3/28 9:29
'''
__author__ = 'lierl'

#mysql-connector-python\mysql-connector

import mysql.connector
conn = mysql.connector.connect(user='root', password='root', database='python', host='139.199.129.251', port=3306)

cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print(cursor.rowcount)
conn.commit()
cursor.close()

cursor = conn.cursor()#查询
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()

print(values)

cursor.close()
conn.close()