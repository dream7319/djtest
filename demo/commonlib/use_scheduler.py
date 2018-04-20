#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_scheduler.py
@time: 2018/4/19 18:50
'''
import datetime

__author__ = 'lierl'

from apscheduler.schedulers.blocking import BlockingScheduler

def job1():
    print("job 1")

def job2(name):
    print("hello %s" %name)

schedule = BlockingScheduler()

#每秒执行一次 有参数
schedule.add_job(func=job2, args=('lierl',), trigger='interval', seconds=1)
#每秒执行一次 无参数
schedule.add_job(func=job1,trigger='interval', seconds=1)
schedule.start()









#关于触发器（trigger）,它有三种参数可选：date / interval / cron.
#date：一次性任务，即只执行一次任务。
# 延时五秒后执行一次
'''
date：一次性任务，即只执行一次任务。
参数如下：
next_run_time (datetime|str) – the date/time to run the job at
timezone (datetime.tzinfo|str) – time zone for run_date if it doesn’t have one already
'''
schedule.add_job(func=job2, args=('lierl',), trigger='date', next_run_time=datetime.datetime.now()+datetime.timedelta(seconds=5))


#interval：循环任务，即按照时间间隔执行任务。
'''
参数如下：
weeks (int) – number of weeks to wait
days (int) – number of days to wait
hours (int) – number of hours to wait
minutes (int) – number of minutes to wait
seconds (int) – number of seconds to wait
start_date (datetime|str) – starting point for the interval calculation
end_date (datetime|str) – latest possible date/time to trigger on
timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations
'''
## 每个1秒运行一次函数
#不带参数和和带有参数的函数
#schedule.add_job(func=job2, args=('lierl',), trigger='interval', seconds=1)
#schedule.add_job(func=job1,trigger='interval', seconds=1)

'''
cron：定时任务，即在每个时间段执行任务。

参数如下：

second (int|str) – 秒 (0-59)
minute (int|str) – 分钟 (0-59)
hour (int|str) – 小时 (0-23)
day_of_week (int|str) – 一周中的第几天 (0-6 or mon,tue,wed,thu,fri,sat,sun)
day (int|str) – 日 (1-31)
week (int|str) – 一年中的第几周 (1-53)
month (int|str) – 月 (1-12)
year (int|str) – 年(四位数)
start_date (datetime|str) – 最早开始时间
end_date (datetime|str) – 最晚结束时间
timezone (datetime.tzinfo|str) – 时区

'''
#在1月,3月,5月,7-9月，每天的下午2点，每一分钟执行一次任务
schedule.add_job(func=job1, trigger='cron', month='1,3,5,7-9', day='*', hour='14', minute='*')



# schedule.start()
