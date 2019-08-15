#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# 定义函数类型的形参，其中fn是一个函数

def map(data, fn) :
    result = [0]*len(data)
    # 遍历data列表中每个元素，并用fn函数对每个元素进行计算
    # 然后将计算结果作为新数组的元素
    for i in range(len(data)):
        result[i] = fn(data[i])
    return result

def get_math_func(type) :
    # 返回局部函数
    if type == "square":
        return square
    if type == "cube":
        return cube
    if type == "factorial":
        return factorial
    if type == 'sum':
        return lambda n: n**0.5

# 定义一个计算平方的局部函数
def square(n):  # ①
    return n**2

# 定义一个计算立方的局部函数
def cube(n):  # ②
    return n **3

# 定义一个计算阶乘的局部函数
def factorial(n):   # ③
    result = 1
    for index in range(2 , n + 1):
        result *= index
    return result

__all__ = ['map', 'get_math_func']
if(__name__=='__main__'):
    # 调用get_math_func()，程序返回一个嵌套函数
    math_func = get_math_func("cube") # 得到cube函数
    print(math_func(5)) # 输出125
    math_func = get_math_func("square") # 得到square函数
    print(math_func(5)) # 输出25
    math_func = get_math_func("factorial") # 得到factorial函数
    print(math_func(5)) # 输出120
    math_func = get_math_func("sum") # 得到factorial函数
    print(math_func(3)) # 输出120

    data = [3, 4, 9, 5, 8]
    print("原数据: ", data)
    # 下面程序代码3次调用map()函数，每次调用时传入不同的函数
    print("计算数组元素的平方")
    print(map(data, get_math_func('square')))
    print("计算数组元素的立方")
    print(map(data, get_math_func('cube')))
    print("计算数组元素的阶乘")
    print(map(data, get_math_func('factorial')))
    print("计算数组元素的平方根")
    print(map(data, get_math_func('sum')))
