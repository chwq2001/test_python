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

# 创建一个包含多条线程的线程池
def test_map(list):
    with ThreadPoolExecutor(len(list)) as pool:
        # 使用线程执行map计算
        # 后面元组有3个元素，因此程序启动3条线程来执行action函数
        results = pool.map(action, list)
        l = zip(list, results)
        return l

def get_map_result(the_future):
    print("get_map_result")
    for i,j in the_future.result():
        print(f"{i}!={j}")


with ThreadPoolExecutor(max_workers=1) as pool:
    # 向线程池提交一个task, 50会作为action()函数的参数
    future = pool.submit(test_map, (5,6,8))

    future.add_done_callback(get_map_result)
    print('done')
