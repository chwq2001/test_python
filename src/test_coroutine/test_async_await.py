#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import asyncio,threading,contextlib


async def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = await asyncio.sleep(1)
    print("Hello again!")


async def hello2():
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(5)
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
with contextlib.closing(asyncio.get_event_loop()) as loop1:
    tasks = (hello2(), hello2())
    loop1.run_until_complete(asyncio.wait(tasks))
    # loop1.close()

# from Python 3.7, support  asyncio.run，代替 loop1 = asyncio.get_event_loop() ～ loop1.run_until_complete(asyncio.wait(tasks))
# asyncio.run( asyncio.wait((hello2(), hello2())) )
print("main2")
