#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_template.py
@time: 2018/3/28 15:46
'''
__author__ = 'lierl'

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template(template_name_or_list='form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html', username = username)
    return render_template('form.html', message='bad username or password', username = username)

if __name__ == '__main__':
    # 若不配置host和port，则默认是localhost，端口为5000
    # 若配置，如写作app.run("",8000)，就是localhost，端口8000
    app.run("", 8080)




