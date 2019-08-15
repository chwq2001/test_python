#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import importlib
model = importlib.import_module('test_iterator')
print('model.__name__',model.__name__)
cls = getattr(model,'Fibs')
fibs = cls(10)
print(next(fibs))
# 使用for循环遍历迭代器
for el in fibs:
    print(el, end=' ')
print()
print(tuple(cls(5)))
