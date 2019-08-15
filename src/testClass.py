#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

class Record:
    # 定义两个类变量
    item = '鼠标'
    date = '2016-06-16'
    def __init__(self):
        pass
    def info (self):
        print('info方法中: ', self.item)
        print('info方法中: ', self.date)
rc = Record()
print(rc.item) # '鼠标'
print(rc.date) # '2016-06-16'
rc.info()
rc.item='screen'
# 修改Record类的两个类变量
Record.item = '键盘'
Record.date = '2016-08-18'
# 调用info()方法
rc.info()
print('*'*100)
Record().info()