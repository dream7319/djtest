#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: do_login.py
@time: 2018/3/29 15:10
'''
__author__ = 'lierl'

'''
 1.输入用户名和密码
 2.认证成功后显示欢迎信息
 3.输错三次后锁定
Readme：
    （1）提示用户输入用户名；
    （2）用户名验证，验证是否已经锁定；
    （3）是否锁定：已锁定告诉用户，输入的用户名已经锁定，找管理员联系；未锁定就验证是否注册；
　　（4）是否注册：未注册就提示用户，这个用户名还没有注册，需要注册；注册就让用户输入密码；
　　（5）输入密码：输入正确就欢迎用户，输入不正常就三次机会，提示用户输入，三次之后将锁定
　　（6）锁定用户从登录用户文件中移除并添加到锁定用户文件。
'''

def isLocked(username):
    #验证输入的用户是否锁定,如果锁定则打印锁定信息
    try:
        with open('lock_user.txt', 'r') as f:
            users = []#定义一个空的列表，用于存储用户名
            lines = f.readlines()#读取所有行
            for line in lines:
                if line is not '':
                    users.append(line.strip().split(":")[0])#需要去掉最后的\n
        if username in users:
            print('输入的用户名已经锁定，找管理员联系')
            exit()
        else:
            #不存在则验证是否已经注册
            isRegister(username)
    except FileNotFoundError as e:
        print('锁定用户信息不存在, %s' % e)

#用户是否注册
def isRegister(username):
    try:
        with open('user_list.txt', 'r') as f:
            registers_users = []
            lines = f.readlines()
            for line in lines:
                registers_users.append(line.strip().split(":")[0])
        if username in registers_users:#当前用户已注册
            pass
        else:
            print("Sorry,%s还没有注册，请注册之后登录" % username)
            exit()
    except FileNotFoundError as e:
        print('用户列表不存在, %s' % e)

# username = input("请输入登录名:")
# password = input("请输入密码：")

#用户输入密码
def userpassword():
    password = input("请输入密码：")
    return password

#用户登录
def login():
    username = input("请输入登录名:")#用户首先需要输入用户名
    isLocked(username)#判断用户是否已经锁定

    with open('user_list.txt', 'r') as f:
        user_dic = {}
        lines = f.readlines()
        for user in lines:
            # 用户名,密码
            (user, user_password) = user.strip().split(":")
            user_dic[user] = user_password

    loginTimes = 1

    while loginTimes <= 3:
        # 用户有三次机会输入密码验证
        password = input("请输入密码:")
        if user_dic[username] == password:
            #登录成功
            print("welcome %s " % username)
            break
        else:
            #不成功提示用户有三次机会，如果三次都不成功，将锁定用户名
            if loginTimes == 3:#三次不成功
                print("对不起，你输入的次数过多，你的用户名已经被锁定，请联系管理员")
                addLock(username)
                # 输入次数过多，把用户名从文件user_list中删除，同时添加到锁定文件lock_user
                break
            else:
                print("对不起，你输入的密码不对，你还有%s次机会" % (3 - loginTimes))
                loginTimes += 1

def addLock(username):
    # 锁定输入密码次数过多用户名
    #把用户名从用户列表中删除，添加到lock中
    try:
        with open(file='user_list.txt',mode= 'r') as f:
            lines = f.readlines()
            users = []  # 保存用户名
            for line in lines:
                users.append(line.strip().split(":")[0])
            index = users.index(username)  # 获取到用户名所在位置

        # 把用户追加到lock中
        with open('lock_user.txt', 'a') as f:
            f.writelines("\n%s" % lines[index])

        with open('user_list.txt', 'w') as f:
            del lines[index]  # 删除
            f.writelines(lines)  # 把剩余用户写入文件
    except FileNotFoundError as e:
        raise e
login()

'''
上面代码运行需要创建两个文件在同级目录，lock_user和user_list，在里面使用了列表、字典等功能，list列表、字典功能最常用，要经常尝试使用空字典、空列表的功能，writelines()，readlines()。上面代码可以实现判断用户输入的用户名是否在锁定列表中，是否在登录的列表中，并且能够实现登录三次锁定的功能。
'''