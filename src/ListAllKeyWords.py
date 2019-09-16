#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import keyword as kw,sys
last_version_kw = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
new_version_added_kw = []
print('current version is',sys.version)
for k in kw.kwlist:
    print(k)
    if k not in last_version_kw:
        new_version_added_kw.append(k)
print("new_version_added_kw:",new_version_added_kw)

