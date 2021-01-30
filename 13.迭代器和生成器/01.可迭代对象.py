# 很多可迭代对象： list/tuple/dict/set/str/range/filter/map
# for i in 可迭代对象
from collections.abc import Iterable


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
print(isinstance(d, Iterable))  # isinstance： 用来判断一个实例对象是否是有指定的类创建出来的
# for  in 循环的本质就是调用可迭代对象的__iter__方法，获取这个方法的返回值
# 这个返回值需要的是一个对象，然后再调用这个对象的__next__方法
for i in d:
    print(i)

name = list(('zhangsan', 'lisi'))
print(isinstance(name, Iterable))

#Demo 这个类和range的功能类似
for i in Demo(10): 
    print(i)