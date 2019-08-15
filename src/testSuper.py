#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


class Employee:
    sf='323'
    def __init__ (self, salary):
        self.salary = salary

    def work(self):
        print('普通员工正在写代码，工资是:', self.salary)


class Customer:
    def __init__ (self, favorite, address):
        self.favorite = favorite
        self.address = address

    def info(self):
        print('我是一个顾客，我的爱好是: %s,地址是%s' % (self.favorite, self.address))
    def work(self):
        print('我是一个顾客 on work')

# Manager继承了Employee、Customer
class Manager(Customer):
    # 重写父类的构造方法
    def __init__(self, salary, favorite, address):
        print('--Manager的构造方法--')
        # 通过super()函数调用父类的构造方法
        e = super()
        e.__init__(favorite, address)
        # 与上一行代码的效果相同
        #super(Manager, self).__init__(salary)
        # 使用未绑定方法调用父类的构造方法
        #e.__init__(self,favorite, address)
        #Employee.__init__(self, salary)

    def info(self):
        print("Manager info")
    def work(self):
        super().work()
        print('Manager.work run',self)
        super().info()
# 创建Manager对象
m = Manager(25000, 'IT产品', '广州')
m.work()  #①
m.info()  #②

