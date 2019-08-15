#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# 定义ItemMetaClass，继承type
class ItemMetaClass(type):
    # cls代表动态修改的类
    # name代表动态修改的类名
    # bases代表被动态修改的类的所有父类
    # attr代表被动态修改的类的所有属性、方法组成的字典
    def __new__(cls, name, bases, attrs):
        # 动态为该类添加一个cal_price方法
        attrs['cal_price'] = lambda self: self.price * self.discount
        print(cls,cls.__name__,cls.__module__,ItemMetaClass==cls)
        print(name)
        print(attrs)
        return type.__new__(cls, name, bases, attrs)
# 定义Book类
'''
当我们传入关键字参数metaclass时，它指示Python解释器在创建MyList时，要通过ItemMetaClass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
'''
class Book(metaclass=ItemMetaClass):
    __slots__ = ('name', 'price', '_discount')
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self, discount):
        self._discount = discount

b = Book("Python基础教程", 89)
b.discount = 0.76
# 创建Book对象的cal_price()方法
print(b.cal_price())
