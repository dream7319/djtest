#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_spider_spring4all.py
@time: 2018/4/23 16:12
'''
import json

from bs4 import BeautifulSoup

__author__ = 'lierl'

import requests
import re
#-----------------爬取spring4all整个网站
headers = {
    "Host":"www.spring4all.com",
    "Referer":"http://www.spring4all.com/",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
}

r = requests.get('http://www.spring4all.com/article/1035')

soup = BeautifulSoup(r.text, "html.parser")
resultSet = soup.findAll('script')
# resultSet = ResultSet()

tag = resultSet[17]
# print(tag)
# tag = Tag()

with open("test.txt", 'w') as f:
    f.write(tag.text.encode("gbk").decode('gbk','strict'))

with open("test.txt", 'r') as f:
    data = f.readlines()
    for d in data:
        if d.__contains__('article: '):
            final_data = d.strip().replace("article: ",'')[:-1]
            dic_data = json.loads(final_data)
            print(dic_data['userId'])
            print(dic_data['title'])
            print(dic_data['type'])
            print(dic_data['nickname'])
            print(dic_data['contentMd'])
            print(dic_data['avatar'])
            print(dic_data['description'])
            print(dic_data['tagSet'])
            print(dic_data['category'])
            print(dic_data['recommended'])
            print(dic_data['id'])
            print(dic_data['updateTime'])
            print(dic_data['createTime'])
            print(dic_data['read'])
            print(dic_data['tag'])
            print(dic_data['contentHtml'])
            print(dic_data['comment'])
            print(dic_data['categoryId'])
            print(dic_data['like'])
            break

