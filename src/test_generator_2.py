#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


def square_gen(val):
    i = 0
    val_from_send = None
    print("\nsquare_gen begin")
    while True:
        # 使用yield语句生成值，使用out_val接收send()方法发送的参数值
        print("before yield val_from_send =", val_from_send,',i =',i)
        val_from_send = (yield val_from_send ** 2) if val_from_send is not None else (yield i ** 2)
        # 如果程序使用send()方法获取下一个值，out_val会获取send()方法的参数
        i += 1
        print("after yield val_from_send =", val_from_send, ',i =', i)


sg = square_gen(5)
print("============================")
# 第一次调用send()方法获取值，只能传入None作为参数
print("sg.send first,",end=' ')
print(sg.send(None))  # 0
print("next first,",end=' ')
print(next(sg))  # 1
print("next second,,",end=' ')
print(next(sg))  # 4
print("next third,,",end=' ')
print(next(sg))  # 9
print('--------------')
# 调用send()方法获取生成器的下一个值，参数9会被发送给生成器
print("sg.send second,",end=' ')
print(sg.send(900))  # 810000
# 再次调用next()函数获取生成器的下一个值
print("next fourth,",end=' ')
print(next(sg))  # 25
print("sg.send third,",end=' ')
print(sg.send(100))  # 10000
# sg.close()
# print(next(sg))
