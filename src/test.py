d=2
g={'a':6, 'b':8,'__builtins__':None} #定义一个字典
t={'b':100, 'c':10} #定义一个字典
print(exec('d=2',g,t))
print(g.items())
print(t.items())