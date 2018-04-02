#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: utils.py
@time: 2018/4/1 16:28
'''
__author__ = 'lierl'
import hashlib
from djtest import settings
from myapp.apps import MyappConfig

def get_md5(str, salt="myapp"):
    h1 = hashlib.sha256()
    str += salt
    h1.update(str.encode('utf-8'))
    return h1.hexdigest()

def send_email(email, code):
    from django.core.mail import send_mail
    from django.core.mail import EmailMultiAlternatives
    subject = '来自www.mmiao.club的注册确认邮件'
    text_content = '''感谢注册www.mmiao.club，这里是django实战教程如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''

    html_content = '''<p>感谢注册<a href="http://{}/{}/confirm?code={}" target=blank>www.mmiao.club</a>,这里是xxx的博客和教程站点，专注于Python和Django技术的分享！</p><p>请点击站点链接完成注册确认！</p><p>此链接有效期为{}天！</p>'''.format('127.0.0.1:8001', MyappConfig.name, code, settings.CONFIRM_DAYS)
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
