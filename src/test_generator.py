#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from collections.abc import Iterable
def test(val, step):
    print("--------test函数开始执行------")
    cur = 0
    # 遍历0～val

    for i in range(1,val+1):
        # cur添加i*step
        cur += i * step
        yield cur


def teststr(val):
    print("--------teststr函数开始执行------")
    cur = ord('A')
    # 遍历0～val

    for i in range(val):
        # cur添加i*step
        cur += i
        yield chr(cur)

# 执行函数，返回生成器
t = test(10, 2)
print('=================')
# # 获取生成器的第一个值
print(type(t),'has __iter__ and __next__',hasattr(t,'__iter__'),hasattr(t,'__next__'),',and Iterable is: ',isinstance(t,Iterable)) # <class 'generator'>
print(next(t)) # 0，生成器“冻结”在yield处
print(next(t)) # 2，生成器再次“冻结”在yield处
print("send begin")
print(t.send(None))
print(t.send(10))
print('send end')
#print('t is Iterable: ',isinstance(t,Iterable))
for i in t:
    print(i)

#继上，再次创建生成器
t = test(10, 1)
#将生成器转换成列表
print (list (t))
#再次创建生成器
t = test(10, 3)
#将生成器转换成元组
print(tuple(t))
print(tuple(t)) #迭代已结束，返回空tuple

t = test(10, 1)
t1 = teststr(10)
#将生成器转换成元组
print(dict(zip(tuple(t),list(t1))))

