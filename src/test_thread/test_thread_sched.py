#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import sched, time
import threading
# 定义线程调度器
s = sched.scheduler()
# 定义被调度的函数
def print_time(name='default'):
    print("%s 的时间: %s" % (name, time.ctime()))
# print('主线程：', time.ctime())
# # 指定10秒之后执行print_time函数
# s.enter(10, 1, print_time)
# # 指定5秒之后执行print_time函数，优先级为2
# s.enter(5, 5, print_time, argument=('位置参数',))
# # 指定5秒之后执行print_time函数，优先级为1
# s.enter(5, 1, print_time, kwargs={'name': '关键字参数'})
# print('主线程,before run: ', time.ctime())
# # 执行调度的任务
# s.run(blocking=True)
# print('主线程,after run：', time.ctime())


s = sched.scheduler(time.time)
ts = time.struct_time((2019, 8, 3, 12, 49, 00, 5, 215, 0))
print('主线程：', time.ctime())
#   enterabs 的第一个参数time得兼容scheduler的第一个参数timefunc
s.enterabs(time.mktime(ts), 1, print_time, kwargs={'name': '指定时间'})
# 指定10秒之后执行print_time函数
s.enter(5, 1, print_time,('位置参数',))
print('主线程,before run: ', time.ctime())
# 执行调度的任务
s.run(blocking=True)
print('主线程,after run：', time.ctime())
