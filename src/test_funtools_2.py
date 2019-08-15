#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from functools import *
from decimal import Decimal
@singledispatch
def test(arg, verbose):
    if verbose:
        print("默认参数为：", end=" ")
    print(arg)
# 限制test函数第一个参数为int型的函数版本
@test.register(int)
def _a(argu, verbose):
    if verbose:
        print("整型参数为：", end=" ")
    print(argu)
@test.register(list)
def _b(argb, verbose=False):
    if verbose:
        print("列表中所有元素为:")
    for i, elem in enumerate(argb):
        print(i, elem, end=" ")

def nothing(arg, verbose=False):
    print("~~None参数~~")
@test.register(float)
@test.register(Decimal)
def test_num(arg, verbose=False):
    if verbose:
        print("参数的一半为:", end=" ")
    print(arg / 2)


test('Python', True)  # ①
# 调用第一个参数为int型的版本
test(20, True)  # ②
test([20, 10, 16, 30, 14], True) # ③
print("\n---------------")
test.register(type(None), nothing)
test(None,True)
test(10.0,True)
test(Decimal(11),True)
print("---------------")
# test.dispatch(类型)即可获取它转向的函数
# 当test()函数第一个参数为float时将转向到调用test_num
print(test_num is test.dispatch(float)) # True
# 当test()函数第一个参数为Decimal时将转向到调用test_num
print(test_num is test.dispatch(Decimal)) # True
# 直接调用test并不等于test_num
print(test_num is test) # False
print(test.dispatch(list))
# 获取test函数所绑定的全部类型
#print(test.registry.keys())
for e in test.registry.keys():
    print(e,', ',sep='',end='')
# 获取test函数为int类型绑定的函数
print(test.registry[list] is test.dispatch(list))