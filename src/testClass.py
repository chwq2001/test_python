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

    def __gt__(self, other):
        print("__gt__")
        if other is None or other.item is None:
            return False
        return self.item > other.item

    def __lt__(self, other):
        print("__lt__")
        if other is None or other.item is None:
            return False
        return self.item < other.item

    def __ge__(self, other):
        print("__ge__")
        if not super().__ge__(other):
            return False

        if other is None or other.item is None:
            return False
        return self.item >= other.item

    def __le__(self, other):
        print("__le__")
        if other is None or other.item is None:
            return False
        return self.item <= other.item

    def __eq__(self, other):
        print("__eq__")
        if other is None or other.item is None:
            return False
        return self.item == other.item
# rc = Record()
# print(rc.item) # '鼠标'
# print(rc.date) # '2016-06-16'
# rc.info()
# rc.item='screen'
# print(Record.item)
# # 修改Record类的两个类变量
# Record.item = '键盘'
# Record.date = '2016-08-18'
# # 调用info()方法
# rc.info()
# print('*'*100)
# rr = Record()
# rr.info()
# print(rc==rr)

r1 = Record()
r2 = Record()
r1.item = 'db'
r2.item = 'db'
print(r1==r2)
print(r1>=r2)
print(r1>r2)
print(r1<=r2)
print(r1<r2)


