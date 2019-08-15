
def _odd_iter():
    n = 1
    while True:
        #print('enter  _odd_iter,', n)
        n = n + 1
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def _can_divisible(x):
    #print('enter  _not_divisible,', x)
    return x % 2 == 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    print(it.__iter__())
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), Ti(it, n))  # 构造新序列

#构建这个类来测试生成器的递归调用
class Ti:
    cnt = 0
    d = dict()
    def __init__(self,it,name):
        self.it = it
        self.name = name
    def __iter__(self):
        return self
    def __next__(self):
        Ti.cnt += 1
        #Ti.d[self.name] = (Ti.d[self.name] + 1) if self.name in Ti.d else 1
        if self.name in Ti.d:
            Ti.d[self.name] += 1
        else:
            Ti.d[self.name] = 1
        return self.it.__next__()


def testtt():
    it = Ti(_odd_iter(),'aa') # 初始序列
    # n = next(it)  # 返回序列的第一个数
    print(next(it))
    print("Ti.cnt,", Ti.cnt)
    it = filter(lambda x: x, Ti(it,'bb'))  # 构造新序列
    # print(next(it))
    # print("Ti.cnt,", Ti.cnt)
    # print(next(it))
    # print("Ti.cnt,", Ti.cnt)
    it = filter(lambda x: x, Ti(it,'cc'))  # 构造新序列
    # print(next(it))
    # print("Ti.cnt,", Ti.cnt)
    it = filter(lambda x: x, Ti(it,'dd'))  # 构造新序列
    print(next(it))
    print("Ti.cnt,", Ti.cnt)
    for k,v in sorted(Ti.d.items()):
        print(k, v)

# testtt()
#
#打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
print('@'*15)
for k,v in sorted(Ti.d.items()):
    print(k, v)