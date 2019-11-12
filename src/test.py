
class AClass:
    def __init__(self):
        pass

    def fn(self,hint):
        print(str(hint))

a = AClass()
a.fn(2)
a.fn.__func__(a,22)
