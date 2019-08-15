#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import traceback
import sys

class My1Exception(Exception): pass


def foo():
    fis = None
    try:
        fis = open("a.txt")
        #My1Exception().x
    except Exception as e:
        print(e)
        # 访问异常的错误编号和详细信息
        print(e.args)
        # 访问异常的错误编号
        print(e.errno)
        # 访问异常的详细信息
        print(e.strerror)
        #e.with_traceback(sys.exc_info())
        #raise My1Exception(e)
    finally:
        # 关闭磁盘文件，回收资源
        if fis is not None:
            try:
                # 关闭资源
                fis.close()
            except OSError as ioe:
                print(ioe.strerror)
        print("执行finally块里的资源回收!")


# def amain():
#     try:
#         foo()
#
#     except Exception as ex:
#         ec = sys.exc_info()
#         a,b,c = ec
#         print((a))
#         print((b))
#         print((c))
#         print(isinstance(ex,object))
#         traceback.print_exc(file=open('/Users/chweiqiang/Downloads/out.log','w'))


foo()
