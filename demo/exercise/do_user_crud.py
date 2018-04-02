#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: do_user_crud.py
@time: 2018/4/2 20:54
'''
__author__ = 'lierl'

'''
作业要求

- 实现增删改查操作：
- 可进行模糊查询，语法至少支持下面3种:
    select name,age from staff_table where age > 22
    select from staff_table where dept = "IT"
    select from staff_table where enroll_date like "2013"
- 查到的信息，打印后，最后面还要显示查到的条数
- 可创建新员工纪录，以phone做唯一键，staff_id需自增
- 可删除指定员工信息纪录，输入员工id，即可删除
- 可修改员工信息，语法如下:
    UPDATE staff_table SET dept = "Market" WHERE where dept = "IT"
    staff_id  name      age   phone         dept    enroll_date
       1     Alex Li    22   13651054608     IT      2013-04-01
       2     Jack Wang  30   13304320533     HR      2015-05-03
       3     Rain Liu   25   1383235322     Sales    2016-04-22
       4     Mack Cao   40   1356145343      HR      2009-03-01
- 注意：以上需求，要充分使用函数，请尽你的最大限度来减少重复代码
'''

def search():
    print("search")

def add():
    print("add")

def modify():
    print("modify")

def delete():
    print("delete")

def main():
    info = '''
        1.模糊查询
        2.创建新员工
        3.修改员工信息
        4.删除员工信息
        5.退出
    '''
    while True:
        print(info)
        menu_dict={"1":search, '2':add, '3':modify, '4':delete}
        user_chosen = input("请输入您想要的操作和选项序号：")
        if user_chosen in menu_dict.keys():
            #执行相应函数
            menu_dict[user_chosen]()
        elif user_chosen == 'r':
            exit("下次再见")
        else:
            print("请输入正确的序号")
if __name__ == "__main__":
    main()