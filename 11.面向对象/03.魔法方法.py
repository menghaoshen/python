# 魔法方法，也叫魔法方法，是类里面的特殊的一些方法
# 特点，
# 1. 不需要手动调用，会在合适的时机自动调用
# 2. 这些方法都是__开始__ ，使用__ 结束
# 3. 方法名都是系统规定好的，在合适的时机自己调用
import time


class Person(object):
    def __init__(self, name, age):
        # 在创建对象时，会自动调用这个方法
        print('__init__被调用了')
        self.name = name
        self.age = age

    def __del__(self):
        # 当对象被销毁时，会自动调用这个方法
        print('__del__方法被调用了')

    def __repr__(self):
        # return  'hello'
        return '姓名：{}，年龄{}'.format(self.name, self.age)

    def __str__(self):
        return 'good'

    def __call__(self, *args, **kwargs):
        print('call方法被调用了')
        # args 是一个元组
        # kwargs 是一个字典
        print('args={},kwargs={}'.format(args, kwargs))
        fn = kwargs['fn']
        return fn(args[0], args[1])


P = Person('张三', 18)
# 如果不做任何修改，直接打印一个对象，是文件的__name__类型，内存地址
print(P)  # 对象类型和，内存地址  <__main__.Person object at 0x000002335F83DB08>
# 当打印一个对象的时候，会调用这个对象的__str__或者__repr__方法
# 如果两个方法都写了，选择__str__
# del P
# time.sleep(10)
print(repr(P))  # 调用内置函数repr，会触发对象的__repr__方法
print(P.__repr__())  # 手动调用魔法方法,一般不手动调用
# P()  # 对象名 ==》 嗲用的是对象P.call 方法，如果没有回报错
n = P(1, 2, fn=lambda x, y: x + y)  #把一个对象当做一个对象调用
print(n)
# 比较str 和repr方法
import datetime

x = datetime.datetime(2020, 2, 24, 16, 17, 45, 200)
print(x)  # str 方法 #可读性比较好
print(repr(x))  # repr 方法
