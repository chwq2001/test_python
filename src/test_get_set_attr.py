class ClassA:
    x = 'a'
    def __init__(self):
        self.y = 'b'
    def __getattr__(self, item):
        return '__getattr__'

    def __setattr__(self, item, v):
        print("__setattr__",item, v)
        #self.item=v  会引发RecursionError
        super().__setattr__(item, v)

    def __getattribute__(self, item):
        # print('item='+item)
        #self.x  会引发RecursionError
        return super().__getattribute__(item)

    def foo(self):
        print('foo')


a = ClassA()
print(a.x)
a.x='gsdgsdg'
ClassA.x='gggggg'
print(a.x)
print(getattr(a,'x'))
print(a.y)
print(getattr(a,'y'))
print(a.z)
print(getattr(a,'z'))
setattr(a,'newv','ajjk')
a.foo()
