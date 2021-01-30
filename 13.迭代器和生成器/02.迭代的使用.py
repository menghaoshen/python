class Demo(object):
    def __init__(self, x):
        self.x = x
        self.cout = 0

    def __iter__(self):  # 只要重写了__iter__方法就是一个可迭代对象
        return self  # 自己返回自己的结果

    def __next__(self):
        # 每次for in 都会调用一次__next__方法，获取返回值
        self.cout += 1
        if self.cout <= self.x:
            # return  'hello'
            return self.cout - 1
        else:
            raise StopIteration  # 到10次就停止
d = Demo(10)
i = iter(d)  #内置函数iter可以获取到一个迭代对象的迭代器
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i    ))