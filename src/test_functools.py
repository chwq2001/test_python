#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from functools import *
# 以初始值（默认为0）为x，以当前序列元素为y，x+y的和作为下一次的初始值
print(reduce(lambda x,y: x + y, range(5))) # 10
print(reduce(lambda x,y: x + y, range(6))) # 15
# 设初始值为10
print(reduce(lambda x,y: x + y, range(6), 10)) # 25
print('----------------')
class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'User[name=%s' % self.name
# 定义一个老式的大小比较函数，User的name越长，该User越大
def old_cmp(u1 , u2):
    return len(u1.name) - len(u2.name)

my_data = [User('Kotlin'), User('Swift'), User('Go'), User('Java')]
# 对my_data排序，需要关键字参数（调用cmp_to_key将old_cmp转换为关键字参数

my_data.sort(key=cmp_to_key(old_cmp))
print(my_data)
print('----------------')

@lru_cache(maxsize=32)
def factorial(n):
    print('~~计算%d的阶乘~~' % n)
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# 只有这行会计算，然后会缓存5、4、3、2、1的解乘
print(factorial(5))
print(factorial(3))
print(factorial(4))
print(factorial(2))
print(factorial(5))
print('----------------')
# int函数默认将10进制的字符串转换为整数
print(int('12345'))
# 为int函数的base参数指定参数值
basetwo = partial(int, base=2)
basetwo.__doc__ = '将二进制的字符串转换成整数'
# 相当于执行base为2的int()函数
print(basetwo('10010'))
print(int('10010', 2))
print('----------------')

@total_ordering
class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'User[name=%s' % self.name
    # 根据是否有name属性来决定是否可比较
    def _is_valid_operand(self, other):
        return hasattr(other, "name")
    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        # 根据name判断是否相等（都转成小写比较、忽略大小写）
        return self.name.lower()  == other.name.lower()
    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        # 根据name判断是否相等（都转成小写比较、忽略大小写）
        return self.name.lower() < other.name.lower()
# 打印被装饰之后的User类中的__gt__方法
print(User.__gt__)
print(User('Tim')>User('Tam'))