#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import threading
import time


class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号、账户余额的两个成员变量
        self.account_no = account_no
        self.__balance = balance
        self.lock = threading.RLock()

    # 因为账户余额不允许随便修改，所以只为self._balance提供getter方法
    def getBalance(self):
        return self.__balance

    balance = property(getBalance,None, None,'账户余额')

    # 提供一个线程安全的draw()方法来完成取钱操作
    def draw(self, draw_amount):
        # 加锁
        self.lock.acquire()
        try:
            # 账户余额大于取钱数目
            if self.__balance >= draw_amount:
                # 吐出钞票
                print(threading.current_thread().name\
                    + "取钱成功！吐出钞票:" + str(draw_amount))
                time.sleep(3)
                # 修改余额
                self.__balance -= draw_amount
                print("\t余额为: " + str(self.__balance))
            else:
                print(threading.current_thread().name\
                    + "取钱失败！余额不足！")
        finally:
            # 修改完成，释放锁
            self.lock.release()
            pass
# 定义一个函数来模拟取钱操作
def draw(account, draw_amount):
    # 直接调用account对象的draw()方法来执行取钱操作
    account.draw(draw_amount)
# 创建一个账户
acct = Account("1234567" , 1000)
acct1 = Account("1234567" , 1000)
# 模拟两个线程对同一个账户取钱
threading.Thread(name='甲1', target=draw , args=(acct , 800)).start()
threading.Thread(name='乙', target=draw , args=(acct , 100)).start()
threading.Thread(name='甲2', target=draw , args=(acct , 200)).start()
