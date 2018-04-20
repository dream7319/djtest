#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: do_spider.py
@time: 2018/4/18 16:37
'''
import time

__author__ = 'lierl'

import requests
import json

url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_551816010?csrf_token='

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Referer':'http://music.163.com/song?id=551816010',
    'Origin':'http://music.163.com',
    'Host':'music.163.com'
}

user_data = {
    'params':'Nn1b0vZ43P2CPn9V2sWtV3CuLf1lnh/RJCZQhB84F4ETiIdtQftxXHmrob55Dmiv0CNJ/Rxd87BNnfogqrJQ+iqcZKrHvHnWFR25oodsssAentevJGqsCQk5+K8p52fpG8iAcmTNTTri2VlcTSennFbA7KzQTu/qtVob7cdRKDw/Dc/v+BMRyfM6HBheDZ2e',
    'encSecKey':'0bb6d7d0ee0bd97b8a42d1aeb6811b8c4b0abf60ada71d59bacb8ceebde832d174180e64e46645f503457885d376980520f9654a151bd5ae2e4a8aa5f3d4aae7697560aa45e3ea79a0825984973230443604673ae6eb34e74ae61b7ce254b8a02941379fa3315c17ab9426f4b77aec9f1638ab03acf17aa8a23953059044ee5e'
}

#将时间戳规范为10位时间戳
def timestamp_to_timestamp10(time_stamp):
    time_stamp = int (time_stamp* (10 ** (10-len(str(time_stamp)))))
    return time_stamp

response = requests.post(url,headers=headers,data=user_data)

data = json.loads(response.text)
hotComments = []

for hotComment in data['hotComments']:
    item = {
        'nickname': hotComment['user']['nickname'],
        'avatarUrl': hotComment['user']['avatarUrl'],
        'likedCount': hotComment['likedCount'],
        'time': hotComment['time'],
        'content': hotComment['content']
    }
    hotComments.append(item)

content_list = [content for content in hotComments]

for content in content_list:
    print('用户：%s,头像：%s,点击数：%s,时间：%s, 内容：%s' % (content['nickname'], content['avatarUrl'],content['likedCount'],time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(timestamp_to_timestamp10(content['time']))),content['content']))



