#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import threading
import time
class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号、账户余额的两个成员变量
        self.account_no = account_no
        self._balance = balance
        self.lock = threading.RLock()
        self.event = threading.Event()
    # 因为账户余额不允许随便修改，所以只为self._balance提供getter方法
    def getBalance(self):
        return self._balance
    # 提供一个线程安全的draw()方法来完成取钱操作
    def draw(self, draw_amount):
        # 加锁
        self.lock.acquire()
        # 如果Event内部旗标为True，表明账户中已有人存钱进去
        if self.event.is_set():
            # 执行取钱操作
            print(threading.current_thread().name
                + " 取钱:" +  str(draw_amount))
            self._balance -= draw_amount
            print("账户余额为：" + str(self._balance))
            # 将Event内部旗标设为False
            self.event.clear()
            # 释放加锁
            self.lock.release()
            # 阻塞当前线程阻塞
            self.event.wait()
        else:
            print('那边没有存好钱，等待。。。。')
            # 释放加锁
            self.lock.release()
            # 阻塞当前线程阻塞
            self.event.wait()
            print('那边存好钱了，可以取钱了')

    def deposit(self, deposit_amount):
        # 加锁
        self.lock.acquire()
        # 如果Event内部旗标为False，表明账户中还没有人存钱进去
        if not self.event.is_set():
            # 执行存款操作
            print(threading.current_thread().name\
                + " 存款:" +  str(deposit_amount))
            self._balance += deposit_amount
            print("账户余额为：" + str(self._balance))
            # 将Event内部旗标设为True
            self.event.set()
            # 释放加锁
            self.lock.release()
            # 阻塞当前线程阻塞,在event.is_set()为True的情况下，实际不wait
            self.event.wait()
        else:
            # 释放加锁
            print(threading.current_thread().name + '：那边没有取走钱，等待。。。。')
            self.lock.release()
            # 阻塞当前线程阻塞
            self.event.wait()
            print(threading.current_thread().name + '：那边取走钱了，可以存钱了')

#定义一个函数，模拟重复max次执行取钱操作
def draw_many(account, draw_amount, max):
    for i in range(max):
        account.draw(draw_amount)
#  定义一个函数，模拟重复max次执行存款操作
def deposit_many(account, deposit_amount, max):
    for i in range(max):
        account.deposit(deposit_amount)
# 创建一个账户
acct = Account("1234567" , 0)
# 创建、并启动一个“取钱”线程
threading.Thread(name="取钱者", target=draw_many,
    args=(acct, 800, 100)).start()
# 创建、并启动一个“存款”线程
threading.Thread(name="存款者甲", target=deposit_many,
    args=(acct , 800, 100)).start()
threading.Thread(name="存款者乙", target=deposit_many,
    args=(acct , 800, 100)).start()
threading.Thread(name="存款者丙", target=deposit_many,
    args=(acct , 800, 100)).start()

# event = threading.Event()
# def cal(name):
#     # 等待事件，进入等待阻塞状态
#     print('%s 启动' % threading.currentThread().getName())
#     print('%s 准备开始计算状态' % name)
#     event.wait()    # ①
#     # 收到事件后进入运行状态
#     print('%s 收到通知了.' % threading.currentThread().getName())
#     print('%s 正式开始计算！'% name)
# # 创建并启动两条，它们都会①号代码处等待
# threading.Thread(target=cal, args=('甲', )).start()
# threading.Thread(target=cal, args=("乙", )).start()
# time.sleep(2)    #②
# print('------------------')
# # 发出事件
# print('主线程发出事件')
# event.set()

