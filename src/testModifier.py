#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import functools
#带参数的装饰器
import functools
import  time

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            print(args)
            print(kw)
            func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now(mmm,nnn,a,b):
    print(mmm,nnn,a,b)


now('rrr','eeeee',a='aa',b='bb')
print(now.__name__)