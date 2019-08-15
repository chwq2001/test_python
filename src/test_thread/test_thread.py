#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import threading
# 定义一个普通的action函数，该函数准备作为线程执行体
class TestRunner:
    def action(self,min,max):
        name = threading.current_thread().getName()
        for i in range(min,max):
            # 调用threading模块current_thread()函数获取当前线程
            # 线程对象的getName()方法获取当前线程的名字
            print(name + " " + str(i))
        print('子线程 '+name+' 执行完成!')


# 通过继承threading.Thread类来创建线程类
class FkThread(threading.Thread):
    def __init__(self,name,min,max):
        super().__init__(name=name)
        self.min = min
        self.max = max
    # 重写run()方法作为线程执行体
    def run(self):
        for i in range(self.min,self.max):
            # 调用threading模块current_thread()函数获取当前线程
            # 线程对象的getName()方法获取当前线程的名字
            print(threading.current_thread().getName() +  " " + str(i))
        print('子线程 ' + super().getName() + ' 执行完成!')


# 下面是主程序（也就是主线程的执行体）
for i in range(100):
    # 调用threading模块current_thread()函数获取当前线程
    print(threading.current_thread().getName() +  " " + str(i))
    if i == 20:
        # 创建并启动第一个线程
        t = TestRunner()
        t1 =threading.Thread(target=t.action,name='第一个子线程',args=(1,101))
        t1.start()

        # 创建并启动第二个线程
        #t2 =threading.Thread(target=t.action,name='第二个子线程',args=(101,201))
        kwargs = {}
        kwargs['min'] = 101
        kwargs['max'] = 201
        t2 = threading.Thread(target=t.action, name='第二个子线程', kwargs=kwargs)
        t2.start()

        # 创建并启动第一个线程
        ft1 = FkThread('第三个子线程', 201, 301)
        ft1.start()

        # 创建并启动第二个线程
        ft2 = FkThread('第四个子线程', 501, 601)
        ft2.start()

print('主线程执行完成!')

