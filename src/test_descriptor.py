#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

class NotNegative():
    def __init__(self,name):
        self.name = name

    def __set__(self, instance, value):
        print("__set__", instance, value)
        if value < 0:
            raise ValueError(self.name+' must be >= 0')
        else:
            instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        print("__get__", instance, owner)
        return instance.__dict__[self.name]

class Product():
    quantity = NotNegative('quantity')
    price = NotNegative('price')

    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price

book = Product('mybook',2,5)
print(book.quantity)
print(book.price)