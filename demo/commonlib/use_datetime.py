#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_datetime.py
@time: 2018/3/25 19:20
'''
__author__ = 'lierl'

from datetime import datetime

print(datetime.now())

#获取指定日期和时间
dt = datetime(year=2018, month=3, day=25, hour=19, minute=51, second=55, microsecond=234)
print(dt)

#datetime转换为timestamp
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
# 对应的北京时间是：timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00

tt = dt.timestamp()
#Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
print(type(tt))#float
print(tt)
#timestamp是一个浮点数，它没有时区的概念，而datetime是有时区
# timestamp转换为datetime
t = 1521978715.000234
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))#UTC时间

#datetime转换为str
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

#datetime加减

from datetime import timedelta

nowTime = datetime.now()
newTime = nowTime + timedelta(days=0, hours=8, minutes=0, milliseconds=0, microseconds=0)
print(newTime)

#本地时间转换为UTC时间

from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))#创建时区UTC+8:00
nowTime = datetime.now()
print(nowTime)

print(nowTime.replace(tzinfo=tz_utc_8))

#时区转换
## 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))





