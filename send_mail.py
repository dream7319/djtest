#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: send_mail.py
@time: 2018/4/2 13:42
'''
__author__ = 'lierl'

import os
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djtest.settings")


subject = '来自xxx邮件'
text_content = "这是一封测试邮件,请忽略"
html_content = "<h1>这是一封测试邮件,请忽略</h1>"
from_email = 'lierlei0515@163.com'
to_email = ['643055803@qq.com']#可以是多个

#发一封普通邮件
send_mail(
        subject=subject,
        message=text_content,
        from_email=from_email,
        recipient_list=to_email
    )

#发一封带有附件的html邮件
msg = EmailMultiAlternatives(subject=subject, from_email=from_email, to=to_email)
msg.attach_alternative(html_content, 'text/html')
msg.attach_file("E:\\aa.xls")#添加附件
msg.send()

