#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# import random as rd
import numpy as nm
from concurrent.futures import ThreadPoolExecutor
import time


BET_COUNT = 100
INIT = 10
WANT = 1000
betResult = dict()


def action(n):
    # print("Enter ", n)
    begin = INIT
    to = WANT
    k = 0
    while True:
        # begin += (1 if rd.randint(0, 1) > 0 else -1)
        begin += (1 if nm.random.randint(2) > 0 else -1)
        k = k + 1
        if begin >= to:
            # print(n,"win at", k)
            return n, 1
        elif begin <= 0:
            # print(n,'lost at', k)
            return n, 0


def get_result(the_future):
    this_result = the_future.result()
    betResult[this_result[0]] = this_result[1]
    # print(this_result[0],this_result[1])


win,lost = 0, 0
t = time.perf_counter()
with ThreadPoolExecutor(max_workers=BET_COUNT) as pool:
    for i in range(0, BET_COUNT):
        future = pool.submit(action, i)
        future.add_done_callback(get_result)

for i,j in betResult.items():
    if j == 1:
        win = win + 1
    else:
        lost = lost +1
print("total win:",win,",lost:",lost)
print('cost time {tm:.3f}'.format(tm=time.perf_counter()-t))
