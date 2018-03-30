#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: do_three_level.py
@time: 2018/3/30 9:33
'''
import os

__author__ = 'lierl'

'''
（1）三级菜单
（2）可以次选择进入各子菜单
（3）所需新知识点：列表、字典
要求：输入back返回上一层，输入quit退出整个程序
思路：
    （1）首先定义好三级菜单字典；
　　（2）提取第一级省的编号，打印包含哪些省份，让用户输入省份的编号，能够显示对应的省，这个过程需要创建一个字典，用于存放省原有的名称和编号，以便用户输入之后进去匹配；
    （3）进入第二级菜单，市的提取，市也存放在一个字典中，以便用户输入对应的编号的时候能够到字典中查找，并返回对应的市；
　　（4）根据上面输入，得到县/区的列表，遍历列表，并使用enumerate()给县/区添加编号，对应的索引只需减一即可，因为不可能让用户看到从0开始，而列表默认是从0开始的；
'''
from demo.exercise.province_city import dict_db

# 显示省
def show_province():
    while True:
        print("欢迎来到全国省市区查询系统...")
        print("+---------------------------------------------------------------+")
        #获取到所有的省
        province_dict = {}
        province_nos = []
        for index, province in enumerate(dict_db.keys(), start=1):
            print('省的编号:%s          省的名称：%s' % (index, province))
            province_dict[index] = province
            province_nos.append(index)
        print("+---------------------------------------------------------------+")
        province_no = input('请输入你要查询的省的编号(输入quit退出)：')
        province_no = province_no.strip()
        if province_no == 'quit':
            exit()
        elif province_no.isdigit():
            province_num = int(province_no)
            if province_num not in province_nos:
                print("您输入的数字不存在,请重新输入")
                show_province()

            province_name = province_dict[province_num]
            print(province_name)
            show_city(province_name)
        else:
            print("您输入的不是数字,请输入的对应的数字")
            show_province()

# 显示市
def show_city(province_name):
    while True:
        print('+---------------------------------------------------------------+')
        city_dict = {}
        cities = {}
        cities_nos = []
        for index, city_all in enumerate(dict_db[province_name], start=1):
            cities_nos.append(index)
            cities[index] = city_all
            for city in city_all.keys():
                print('市的编号：%s        市的名称：%s' % (index, city))
                city_dict[index] = city
        print('+---------------------------------------------------------------+')
        city_no = input("请输入你要查询的市的编号(输入quit退出,输入back返回上一层)：")
        city_no = city_no.strip()
        if city_no == 'quit':
            exit()
        elif city_no == 'back':
            break
        elif city_no.isdigit():
            city_num = int(city_no)
            if city_num not in cities_nos:
                print("您输入的数字不存在,请重新输入")
                show_city(province_name)

            city_name = city_dict[city_num]
            print('%s    %s' % (province_name, city_name))
            show_county(province_name, city_name, cities, city_num)
        else:
            print("您输入的不是数字,请输入的对应的数字")
            show_city(province_name)

# 显示县
def show_county(province_name, city_name, cities, city_num):
    while True:
        print('+---------------------------------------------------------------+')
        country_dict = {}
        country_nos = []
        for country_all in cities[city_num].values():
            for index, country in enumerate(country_all, start=1):
                country_dict[index] = country
                country_nos.append(index)
                print('县/区编号：%s        县/区名称：%s' % (index, country))
        print('+---------------------------------------------------------------+')
        country_no = input('请输入你要查询的县/区的编号(输入quit退出,输入back返回上一层)：')
        country_no = country_no.strip()
        if country_no == 'quit':
            exit()
            show_county(province_name, city_name, cities, city_num)
        elif country_no == 'back':
            break
        elif country_no.isdigit():
            country_num = int(country_no)
            if country_num not in country_nos:
                print("您输入的数字不存在,请重新输入")
                show_county(province_name, city_name, cities, city_num)

            print('%s    %s    %s' % (province_name, city_name, country_dict[country_num]))
            exit()
        else:
            print("您输入的不是数字,请输入的对应的数字")
            show_county(province_name, city_name, cities, city_num)

if __name__ == '__main__':
    show_province()




