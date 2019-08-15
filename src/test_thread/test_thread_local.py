#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import time,threading
from concurrent.futures import ThreadPoolExecutor
# 定义线程局部变量


class TT:
    pass


mydata1 = threading.local()
mydata2 = TT()


# 定义准备作为线程执行体使用的函数
def action (max):
    # if not hasattr(mydata,'x'):
    time.sleep(1)
    print(threading.current_thread())
    if not hasattr(mydata1, 'x'):
        mydata1.x = 0
    if not hasattr(mydata2, 'x'):
        mydata2.x = 0
    for i in range(max):
        mydata1.x += i
        mydata2.x += i
        # 访问mydata的x的值
        # print('%s mydata.x的值为: %d' %
        #     (threading.current_thread().name, mydata.x))
    return mydata1.x,mydata2.x
# 使用线程池启动两个子线程
with ThreadPoolExecutor(max_workers=2) as pool:
    future1 = pool.submit(action, 10)
    future2 = pool.submit(action, 10)
    print("future1="+str(future1.result()))
    print("future2=" + str(future2.result()))

