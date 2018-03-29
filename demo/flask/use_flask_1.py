#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_flask_1.py
@time: 2018/3/29 14:29
'''
__author__ = 'lierl'

from flask import Flask, g, request

app = Flask(__name__)

@app.before_request#在请求收到之前绑定一个函数做一些事情。
def before_request():
    print('before request started')

@app.after_request#每一个请求之后绑定一个函数，如果请求没有异常。
def after_request(response):
    print('after request finished')
    return response

@app.teardown_request#每一个请求之后绑定一个函数，即使遇到了异常。
def teardown_request(exception):
    print('teardown request')

@app.route('/')
def index():
    print("route")
    return 'Hello, world'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
