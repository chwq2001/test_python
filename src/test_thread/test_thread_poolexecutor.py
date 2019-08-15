#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor
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


test_callback = True
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
        print(future1.result())
        # 查看future2代表的任务返回的结果       °
        print(future2.result())
    else:
        future1.add_done_callback(get_result)
        future2.add_done_callback(get_result)
    print('~'*100)
    # 关闭线程池
    # pool.shutdown()  #放在with块中会被自动调用
    print('done')

# 创建一个包含4条线程的线程池
def test_map(list):
    with ThreadPoolExecutor(len(list)) as pool:
        # 使用线程执行map计算
        # 后面元组有3个元素，因此程序启动3条线程来执行action函数
        results = pool.map(action, list)
        return zip(list,results)

def get_map_result(the_future):
    for i,j in the_future.result():
        print(f"{i}!={j}")
with ThreadPoolExecutor(max_workers=1) as pool:
    # 向线程池提交一个task, 50会作为action()函数的参数
    future = pool.submit(test_map, (5,6,8))
    future.add_done_callback(get_map_result)
    print('done')
