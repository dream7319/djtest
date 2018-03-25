#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: re_demo.py
@time: 2018/3/25 18:47
'''
__author__ = 'lierl'

'''
\d 匹配一个数字
\w 匹配一个字母或数字
.  匹配任意字符
\s 匹配一个空格或tab空白字符
*  表示任意个字符(包括0个)
+  表示至少一个字符
?  表示0个或1个
{n} 表示n个字符
{n-m} 表示n-m个字符
[] 表示范围
[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'
^表示行的开头，^\d表示必须以数字开头
$表示行的结束，\d$表示必须以数字结束
'''

import re
#判断正则表达式是否匹配
print(re.match(r'^\d{3}-\d{3,8}$', '010-12345'))# 不匹配打印None
#切分字符串
print(re.split(r'[\s,;]+', 'a,b c   d;e'))
#分组 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
#group(0)永远是原始字符串
print(m.group(0))
print(m.group(1))
print(m.group(2))

t = '09:02:58'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

#贪婪匹配  需要特别指出的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
print(re.match('^(\d+)(0*)$', '102300').groups())#由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了

print(re.match('^(\d+?)(0*)$', '102300').groups())#必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：


#编译
'''
当我们在Python中使用正则表达式时，re模块内部会干两件事情：
1、编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
2、用编译后的正则表达式去匹配字符串
'''
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')#编译后生成Regular Expression对象
print(type(re_telephone))#<class '_sre.SRE_Pattern'>
print(re_telephone.match('010-123456').groups())

#请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
# someone@gmail.com
# bill.gates@microsoft.com

def is_valid_email(email):
    return re.compile(r"^\w+[.]?\w+@\w+.com$").match(email)

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
