#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import math
def next_pi():
    pi,n = 0,1
    while True:
        pi,n = pi + 6/n**2, n+1
        yield pi**0.5,n

class pi_cal:
    pi,n = 0,1
    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        self.pi, self.n = self.pi + 6 / self.n ** 2, self.n + 1
        return self.pi**0.5,self.n

if __name__ == '__main__':
    x = next_pi()
    for i in x:
        print(i)
        if 3.14-i[0] < 0:
            break

    input('then iterator...')

    y = pi_cal()
    for i in y:
        print(i)
        if 3.14-i[0] < 0:
            break
else:
    print('not in')