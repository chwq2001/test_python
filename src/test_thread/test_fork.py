#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os
'''
在实际编程中，程序可通过 fork() 方法来创建一个子进程
然后通过判断 fork() 方法的返回值来确定程序是否正在执行子进程，
也就是把需要并发执行的任务放在 if pid==0: 的条件执行体中，这样就可以启动多个子进程来执行并发任务。
'''
print('父进程（%s）开始执行' % os.getpid())
# 开始fork一个子进程
# 从这行代码开始，下面代码都会被两个进程执行
pid = os.fork()
print('进程进入：%s' % os.getpid())
# 如果pid为0，表明子进程
if pid == 0:
    print('子进程，其ID为 (%s)， 父进程ID为 (%s)' % (os.getpid(), os.getppid()))
else:
    print('我 (%s) 创建的子进程ID为 (%s).' % (os.getpid(), pid))
print('进程结束：%s' % os.getpid())
