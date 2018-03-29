#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_requests.py
@time: 2018/3/27 14:20
'''
__author__ = 'lierl'

import requests

r = requests.get('http://www.baidu.com', params={'aa': 'bb', 'cc': 'dd'})
print(r.status_code)
print(r.headers.items())
print(r.encoding)
print(r.text.encode('ISO-8859-1').decode('utf-8'))
print(r.url)
print(r.content)

r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')

print(r.text)
print(r.json())

# r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r.text)

#requests默认使用application/x-www-form-urlencoded对POST数据编码
r = requests.post('https://accounts.douban.com/exercise',data={'form_email': 'abc@example.com', 'form_password': '123456'})

#
# params = {'key': 'value'}
# r = requests.post(url, json=params) # 内部自动序列化为JSON

# 上传文件需要更复杂的编码格式，但是requests把它简化成files参数
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url='', files=upload_files)

# r.cookies['aa'] 获取cookie

# cs = {'token': '12345', 'status': 'working')
# r = requests.get(url, cookies=cs)

# r = requests.get(url, timeout=2.5)  # 2.5秒后超时







