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

#假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
import re
def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz_r = re.match(r'^UTC([+|-]\d{1,2}):00$', tz_str)#获取时区信息
    print(tz_r.groups())
    tz = timezone(timedelta(hours=int(tz_r.group(1))))
    dt = dt.replace(tzinfo=tz)
    return dt.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0
#
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0
#
month = datetime.now().month

print(str('10').rjust(2,'0'))
