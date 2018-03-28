#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_urllib.py
@time: 2018/3/27 9:39
'''
__author__ = 'lierl'

#urllib提供了一系列用于操作URL的功能

#urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应
from urllib import request


#对豆瓣的一个URL https://api.douban.com/v2/book/2129650进行抓取
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print("Status: ", f.status, f.reason)
    print(data.decode('utf-8'))
    print(type(f))#http.client.HTTPResponse
    for key, value in f.getheaders():
        print("%s: %s" % (key, value))

print("----------------------------------------------------------------------------")
#如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req) as f:
    print("Status: ", f.status, f.reason)
    for key, value in f.getheaders():
        print("%s: %s" % (key, value))
    print(data.decode('utf-8'))
print("----------------------------------------------------------------------------")
#如果要以POST发送一个请求，只需要把参数data以bytes形式传入
#模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入
from urllib import request, parse
print("Login to webo.cn...")
email = input("email:")
passwd = input("password:")
login_data = parse.urlencode([
    ('email', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('parser', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

print("----------------------------------------------------------------------------")

import json
def fetch_data(url):
    with request.urlopen(url) as f:
        return json.loads(f.read().decode('utf-8'), encoding='utf-8')

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')






