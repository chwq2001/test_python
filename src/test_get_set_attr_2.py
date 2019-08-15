class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        # if callable(self.path):
        #     s = '%s(%s)' % (self,path)
        # else:
        s = '%s/%s' % (self, path)
        return Chain(s)

    def users(self, str):
        print('name call,', str)
        return self

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)
print(Chain().status.users('michael').repos)
