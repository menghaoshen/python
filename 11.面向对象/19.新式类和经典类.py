#手动的指定Person 类继承object
class Person(object):
    pass

#没有指定Dog的父类，python3里默认继承object
class Dog:
    pass

#新式类和经典类的概念
#1. 新式类：继承自object的类，我们称之为新式类
#2. 经典类，不继承自object的类

#在python2里，如果不手动的指定一个类的父类是object，这个类就是经典类
#python3 不在支持经典类，都是新式类，
