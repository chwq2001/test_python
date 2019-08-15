#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import threading
import time
import queue
def product(bq):
    str_tuple = ("Python", "Kotlin", "Swift")
    for i in range(10):
        print(threading.current_thread().name + "生产者准备生产元组元素！")
        time.sleep(0.2);
        # 尝试放入元素，如果队列已满，则线程被阻塞
        p = str_tuple[i % 3]
        bq.put(p)
        print(threading.current_thread().name \
              + "生产者生产元组元素完成！生产出了"+str(i)+' '+p)
def consume(bq):
    while True:
        print(threading.current_thread().name + "消费者准备消费元组元素！")
        time.sleep(0.2)
        # 尝试取出元素，如果队列已空，则线程被阻塞
        t = bq.get(block=True,timeout=5)
        print(threading.current_thread().name \
            + "消费者消费[ %s ]元素完成！" % t)
# 创建一个容量为1的Queue
bq = queue.Queue(maxsize=1)
# 启动3个生产者线程
threading.Thread(target=product,name='第一个生产者',args=(bq, )).start()
threading.Thread(target=product,name='第二个生产者', args=(bq, )).start()
threading.Thread(target=product, name='第三个生产者',args=(bq, )).start()
# 启动一个消费者线程
threading.Thread(target=consume,name='第一个消费者', args=(bq, )).start()