#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import asyncio,threading,time


@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    x = asyncio.sleep(1)
    print('r=' + type(x))
    r = yield from asyncio.sleep(1)

    print("Hello again!")


@asyncio.coroutine
def hello2():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(5)
    print('Hello again! (%s)' % threading.currentThread())

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
h = hello()
loop.run_until_complete(h)
print("main")
# loop.close()

print("#"*100)
loop1 = asyncio.get_event_loop()   # actually, this loop is loop above
tasks = (hello2(), hello2())
loop1.run_until_complete(asyncio.wait(tasks))
loop1.close()
print("main2")
