#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

class Mycontex:
    def __init__(self,name):
        self.name=name
        print('init....', self.name)
    def __enter__(self):
        print("进入enter",self.name)
        self.fn()
        return self, Mycontex('test 222')
    def do_self(self):
        print('do_self', self.name)
        fis = open("a.txt");
    def __exit__(self,exc_type,exc_value,traceback):
        print("退出exit",self.name)
        print(exc_type,exc_value)
        return False
    def fn(self):
        pass

#end def fn

from contextlib import contextmanager
class Query(object):
    def __init__(self, name):
        self.name = name
    def query(self):
        print('Query info about %s...' % self.name)
        # fis = open("a.txt");

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    try:
        yield q
    finally:
        print('End')


if __name__ == '__main__':
    try:
        with Mycontex('test 111') as mc:
            print(type(mc))
            print(hasattr(mc[0], '__exit__'))
            mc[0].do_self()
            mc[1].do_self()
            print(type(mc))
            print('with finish')
    except FileNotFoundError as ex:
        print('ffsfsd',ex.strerror)
    ss = create_query('Bob')
    print(hasattr(ss, '__enter__'),hasattr(ss, '__exit__'))
    with ss as q:
        print(ss,q)
        print(hasattr(q, '__enter__'))
        q.query()
