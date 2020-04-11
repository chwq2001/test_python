#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor,as_completed
import threading
import time
# 定义一个准备作为线程任务的函数
def action(max):
    my_sum = 1
    for i in range(1,max+1):
        #print(threading.current_thread().name + '  ' + str(i))
        my_sum *= i
    time.sleep(5)
    return my_sum


def get_result(the_future):
    print('call back get_result: '+str(the_future.result()))


test_callback = 1
# 创建一个包含2条线程的线程池，同时他也是一个上下文管理器
with ThreadPoolExecutor(max_workers=2) as pool:
    # 向线程池提交一个task, 50会作为action()函数的参数
    future1 = pool.submit(action, 10)
    # 向线程池再提交一个task, 100会作为action()函数的参数
    future2 = pool.submit(action, 11)
    # 判断future1代表的任务是否结束
    print(future1.done(),future1.running())
    # 判断future2代表的任务是否结束
    print(future2.done(),future2.running())
    if not test_callback:
        # 查看future1代表的任务返回的结果
        print(as_completed(future1))
        # 查看future2代表的任务返回的结果
        print(future2.result())
    else:
        future1.add_done_callback(get_result)
        future2.add_done_callback(get_result)
    print('~'*100)
    # 关闭线程池
    # pool.shutdown()  #放在with块中会被自动调用
    print('done')


