#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_spider_spring4all_main.py
@time: 2018/4/23 17:16
'''
import json

__author__ = 'lierl'

import requests

with open('spring4all.txt', 'w',encoding="utf-8") as f:
    for i in range(1,67):
        req = requests.get("http://www.spring4all.com/common/articles/"+str(i))

        datas = json.loads(req.text)
        print(type(datas))
        list_data = datas['data']['list']

        article_url_prefix="http://www.spring4all.com/article/"
        for data in list_data:
            f.writelines(data['title']+'#####'+article_url_prefix+str(data['id'])+"\n")
            # print(data['read'])
            # print(data['id'])
            # print(data['like'])
            # print(data['description'])
            # print(data['userId'])
            # print(data['category'])
            # print(data['categoryId'])
            # print(data['comment'])
            # print(data['nickname'])
            # print(data['recommended'])
            # print(data['type'])
            # print(data['avatar'])
